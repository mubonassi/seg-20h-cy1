print("| Z-TYPE GENÉRICO PARA TREINAR DIGITAÇÃO! |")
print("-"*30)

lista = ["Banana","Paralelepípedo","Quadrado","Anão","Pneumoultramicroscopicossilicovulcanoconiótico"]
print("Tente digitar todas as palavras abaixo para treinar sua digitação!")

acertos = 0

for i in lista:
    print("-"*30)
    print(f"Palavra: {i}")
    palavra = input("Digite a palavra: ")

    if palavra == i:
        print("Você acertou!")
        acertos = acertos + 1
    else:
        print("Você errou!")

print("-"*30)
print(f"Você acertou {acertos} palavras!")