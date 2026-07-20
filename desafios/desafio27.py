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