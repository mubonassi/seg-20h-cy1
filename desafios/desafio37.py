def calcularMedia():
    n1 = float(input("Digite a 1ª Nota: "))
    n3 = float(input("Digite a 2ª Nota: "))
    n2 = float(input("Digite a 3ª Nota: "))

    m = (n1+n2+n3) / 3

    print(f"Sua média deu {m}")

def calcularRank():
    print("| SISTEMA DE RANKING NUSEI |")
    pontos = int(input("> Digite quantos pontos você pontuou: "))

    if pontos > 1000:
        print("Rank: Campeão")
    elif pontos > 700:
        print("Rank: Lendário")
    elif pontos > 500:
        print("Rank: Mestre")
    elif pontos > 200:
        print("Rank: Veterano")
    else:
        print("Rank: Iniciante")

def mostrarParImpar():
    print("| PARES E IMPARES |")
    print("-"*30)

    intervalo = int(input("Digite o intervalo para ser mostrado: "))

    print("-"*30)
    print("| PARES |")
    for i in range(2,intervalo+1,2):
        print(f"#{i}")

    print("-"*30)
    print("| IMPARES |")
    for i in range(1,intervalo+1,2):
        print(f"#{i}")

print("| Ferramenta de Desafios! |")

while True:
    print("-- Escolha um dos desafios abaixo!")

    print("1 - Calcular a Média do Aluno\n2 - Calcular o Rank de Pontos\n3 - Mostrar Pares e Impares\n4 - Sair")

    escolha = int(input("Digite aqui a opção (numero): "))

    if escolha == 1:
        calcularMedia()
    elif escolha == 2:
        calcularRank()
    elif escolha == 3:
        mostrarParImpar()
    elif escolha == 4:
        break
    else:
        print("ERRO! Opção inválida!")