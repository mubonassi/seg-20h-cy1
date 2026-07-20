print("| SHOW DO PY-TRILHÃO! |")
print("-"*40)

print("Seja bem vindo ao show do py-trilhão! Responda a pergunta abaixo corretamente! Caso desista, escreva 'Desisto'!")
print("Pergunta: Qual a linguagem de programação esse código está sendo executado?")

resposta = "python"
tentativa = ""
erros = 0

while tentativa != resposta:
    tentativa = input("Digite aqui sua resposta: ").lower()

    if tentativa == resposta:
        print("Você acertou, parabéns!")
        print(f"Total de erros: {erros}")
    elif tentativa == "desisto":
        print("Você desistiu do prêmio!")
        print(f"A resposta era: {resposta}")
        break
    else:
        print("Você errou! Tente novamente!")
        erros = erros + 1