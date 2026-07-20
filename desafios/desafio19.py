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