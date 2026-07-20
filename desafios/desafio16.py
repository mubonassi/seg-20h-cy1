numero1 = int(input("Digite o 1o Número: "))
numero2 = int(input("Digite o 2o Número: "))
resultado = numero1+numero2

print(f"Resultado deu: {resultado}")
if resultado > 0:
    print("O resultado deu positivo")
else:
    if resultado == 0:
        print("Resultado deu neutro")
    else:
        print("O resultado deu negativo")