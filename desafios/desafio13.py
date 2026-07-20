senha = 3556
senhaAdivinhada = int(input("Digite a senha para quebrar: "))

if senhaAdivinhada == senha:
    print("Você acertou a senha!")
else:
    print("Você errou a senha!")
    if senhaAdivinhada > senha:
        print("Você colocou um número acima!")
    else:
        print("Você colocou um número abaixo!")