print("| CALCULADORA COMPLETA |")
print("-"*30)
numero1 = float(input("Digite o número 1: "))
numero2 = float(input("Digite o número 2: "))
print("-- Lista de operadores: + - / * **")
operador = input("Digite o operador: ")

operadores = ["+","-","*","/","**"]

if operador in operadores:
    if operador == "+":
        resultado = numero1 + numero2
    elif operador == "-":
        resultado = numero1 - numero2
    elif operador == "/":
        if numero2 != 0:
            resultado = numero1 / numero2
        else:
            resultado = "N/D"
    elif operador == "*":
        resultado = numero1 * numero2
    elif operador == "**":
        resultado = numero1 ** numero2

    print(f"{numero1} {operador} {numero2} = {resultado}")
else:
    print("ERRO: Operador inválido! Reinicie o programa e escolha um correto!")