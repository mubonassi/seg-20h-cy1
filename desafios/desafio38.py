def calcularMedia(n1,n2,n3):
    m = (n1+n2+n3) / 3
    return m


print("| FUNÇÃO COM RETURN: MÉDIA |")
print("-"*60)

n1 = float(input("Digite a 1ª Nota: "))
n3 = float(input("Digite a 2ª Nota: "))
n2 = float(input("Digite a 3ª Nota: "))

media = calcularMedia(n1,n2,n3)

print(f"Sua média deu {media}")