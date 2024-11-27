import requests #Importa a biblioteca requests, usada para fazer requisições HTTP a API
import json #importa a biblioteca json para manipular os dados retornado pela API
from deep_translator import GoogleTranslator # Essa biblioteca permite traduzir texto entre diferentes idiomas


# Função para consumir a API de conselhos
def obter_conselhos(quantidade): #Define uma função, que recebe como parametro o número de conselhos a serem obtidos
    conselhos = [] #Cria uma lista vazia para armazenas os conselhos
    for _ in range(quantidade): #Um loop par buscar o numero especifico de conselhos
        resposta = requests.get("https://api.adviceslip.com/advice") #Faz uma requisição HTTP GET a API de conselhos.
        if resposta.status_code == 200: #Verifica se a requisição foi bem-sucedida
            conselho = json.loads(resposta.text) #Converte a resposta da API(em JSON) para um dicionario Python
            conselhos.append(conselho["slip"]) #Adiciona a lista conselhos um dicionario contendo o ID e o texto
        else:
            print("Erro ao acessar a API.")
            return None
    return conselhos #Retorna a lista de conselhos obtidos 


# Função para exibir conselhos
def mostrar_conselhos(conselhos): #Define uma função para exibir os conselhos no terminal
    for conselho in conselhos:
        print(f"ID: {conselho['id']}, Conselho: {conselho['advice']}") #Imprime o ID e o texto


# Função para salvar conselhos em arquivo
def salvar_conselhos(conselhos, arquivo="conselhos.txt"): #Define uma função para salvar os conselhos em um arquivo
    with open(arquivo, "a", encoding="utf-8") as f: #Abre o arquivo no modo de adição"a", garantido que os novos conselhos sejam adicionados sem apagar os existentes
        for conselho in conselhos:
            f.write(f"ID: {conselho['id']}, Conselho: {conselho['advice']}\n")
    print(f"Conselhos salvos no arquivo {arquivo}.")


# Função para ler conselhos de um arquivo
def ler_conselhos(arquivo="conselhos.txt"): #Define uma função para ler o conteudo
    try: 
        with open(arquivo, "r", encoding="utf-8") as f: #Abre o arquivo em modo leitura "r"
            print(f.read()) #Lê e exibe o conteúdo do arquivo
    except FileNotFoundError: #Captura o erro caso o arquivo não exista 
        print("Arquivo não encontrado.") 


# Função para traduzir conselhos
def traduzir_conselhos(conselhos): #Define uma função para traduzir
    conselhos_traduzidos = [] #Cria uma lista vazia para armazenar os conselhos
    for conselho in conselhos: 
        traduzido = GoogleTranslator(source="auto", target="pt").translate(conselho["advice"]) #Tradução
        conselhos_traduzidos.append({"id": conselho["id"], "advice": traduzido}) #Adiciona o conselho traduzido a lista
    return conselhos_traduzidos


# Função principal
def menu(): #Define a função principal do programa
    conselhos = [] #Cria uma lista vazia para armazenar os conselhos em memória
    while True:
        print("\n--- MENU ---")
        print("1. Ouvir o Seu Zé BUCETA (Obter Conselhos)")
        print("2. Mostrar Conselhos")
        print("3. Guardar a Sabedoria (Salvar Conselhos)")
        print("4. Mostrar Conselhos Guardados")
        print("5. Traduzir Conselhos")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            try:
                quantidade = int(input("Quantos conselhos deseja receber? "))
                conselhos = obter_conselhos(quantidade)
                if conselhos:
                    print("Conselhos obtidos com sucesso!")
            except ValueError:
                print("Por favor, insira um número válido.")
        elif opcao == "2":
            if 'conselhos' in locals():
                mostrar_conselhos(conselhos)
            else:
                print("Nenhum conselho disponível. Obtenha conselhos primeiro.")
        elif opcao == "3":
            if 'conselhos' in locals():
                salvar_conselhos(conselhos)
            else:
                print("Nenhum conselho para salvar. Obtenha conselhos primeiro.")
        elif opcao == "4":
            ler_conselhos()
        elif opcao == "5":
            if 'conselhos' in locals():
                conselhos_traduzidos = traduzir_conselhos(conselhos)
                mostrar_conselhos(conselhos_traduzidos)
            else:
                print("Nenhum conselho para traduzir. Obtenha conselhos primeiro.")
        elif opcao == "6":
            print("Saindo do programa. Até mais, Seu Zé!")
            break
        else:
            print("Opção inválida. Tente novamente.")


# Executar o programa
if __name__ == "__main__":
    menu()
