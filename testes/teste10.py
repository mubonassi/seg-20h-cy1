#Continuando com Estruturas de Repetição
#While -> Repetição condicionada

numero = 0
while numero == 0:
    numero = int(input("Digite um número que não seja zero: "))
print("Fim da repetição!")

#While True -> Repetição indefinida (loop infinito)

while True:
    resposta = input("Deseja quebrar o loop?: ").lower()

    if resposta == "sim":
        break
    elif resposta == "não":
        print("Vou continuar no loop, então")
    else:
        print("Escreva uma resposta certa")