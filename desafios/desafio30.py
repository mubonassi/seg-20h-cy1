print("| CONTADOR DE LETRAS |")
print("-"*30)

texto = input("Digite uma frase/palavra: ")
contador = 0

for i in texto:
    contador = contador + 1

print(f"A palavra/frase '{texto}' contém {contador} caracteres!")