print("| SOMANDO NO INTERVALO |")
print("-"*30)
intervalo = int(input("Digite o intervalo da quantidade de números: "))
print("-"*30)

resultado = 0
conta = ""

for i in range(1,intervalo+1):
    numero = int(input(f"Digite o #{i} número: "))
    resultado = numero + resultado
    conta = conta + str(numero)
    if i < intervalo:
        conta = conta + "+"
    

print("-"*30)
print(f"Conta Final: {conta} = {resultado}")