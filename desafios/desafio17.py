print("> POSTO DE GASOLINA <")

sobra = float(input("Digite quanto está sobrando no tanque (L): "))
quantia = float(input("Digite o quanto deseja colocar no tanque (L): "))

if quantia <= sobra:
    print("Tanque abastecido com sucesso!")
else:
    print("Erro! Valor inválido para quantia!")