import random

print("| MÁQUINA DA SORTE!!! |")

lista = ["Bola","Chiclete","MAIOR PRÊMIO: TELEVISÃO!","Chaveiro","Funko Pop","Carregador"]

for i in range(1,4):
    print("||GERANDO PRÊMIO!!||")
    premio = random.choice(lista)

    print(f"Você ganhou: {premio}")

    if premio == "MAIOR PRÊMIO: TELEVISÃO!":
        print("PARABÉNS! Você atingiu o prêmio máximo!")
        break
    else:
        print("Mas, não foi o prêmio máximo")
        if i < 4:
            print(f"Deseja tentar novamente? (tentativa {i} de 3)")
            escolha = input("Digite aqui: ").lower()
            if escolha == "não":
                print(f"Então, seu prêmio final foi: {premio}")
                break
        else:
            print("E você não tem mais chances!")