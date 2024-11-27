import requests #Importa a biblioteca requests, usada para fazer requisições HTTP a API
import json #importa a biblioteca json para manipular os dados retornado pela API
from deep_translator import GoogleTranslator # Essa biblioteca permite traduzir texto entre diferentes idiomas


# Função para consumir a API de conselhos
def obter_conselhos(quantidade): #Define uma função, que recebe como parametro o número de conselhos a serem obtidos
    conselhos = [] #Cria uma lista vazia para armazenas os conselhos
    for _ in range(quantidade): #Um loop par buscar o numero especifico de conselhos
        resposta = requests.get("https://api.adviceslip.com/advice") #Faz uma requisição HTTP GET a API de conselhos.
        if resposta.status_code == 200:
            conselho = json.loads(resposta.text)
            conselhos.append(conselho["slip"])
        else:
            print("Erro ao acessar a API.")
            return None
    return conselhos


# Função para exibir conselhos
def mostrar_conselhos(conselhos):
    for conselho in conselhos:
        print(f"ID: {conselho['id']}, Conselho: {conselho['advice']}")


# Função para salvar conselhos em arquivo
def salvar_conselhos(conselhos, arquivo="conselhos.txt"):
    with open(arquivo, "a", encoding="utf-8") as f:
        for conselho in conselhos:
            f.write(f"ID: {conselho['id']}, Conselho: {conselho['advice']}\n")
    print(f"Conselhos salvos no arquivo {arquivo}.")


# Função para ler conselhos de um arquivo
def ler_conselhos(arquivo="conselhos.txt"):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            print(f.read())
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# Função para traduzir conselhos
def traduzir_conselhos(conselhos):
    conselhos_traduzidos = []
    for conselho in conselhos:
        traduzido = GoogleTranslator(source="auto", target="pt").translate(conselho["advice"])
        conselhos_traduzidos.append({"id": conselho["id"], "advice": traduzido})
    return conselhos_traduzidos


# Função principal
def menu():
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
