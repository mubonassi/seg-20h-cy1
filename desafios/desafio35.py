import random

print("| PERSONALIZANDO DADOS |")
print("-"*40)
lados = int(input("Digite quantos lados tem o dado: "))

while True:
    valor = random.randint(1,lados)
    print(f"Dado (D{lados}): {valor}")

    print("Aperte (enter) para gerar um novo ou escreva 'parar' para finalizar")
    escolha = input("Aperte enter ou escreva: ")

    if escolha == "parar":
        break