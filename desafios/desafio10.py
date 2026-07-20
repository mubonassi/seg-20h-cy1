print("|Calculo de Produtos|")
print("-"*20)
produto1 = float(input("Digite o valor do 1º Produto: "))
produto2 = float(input("Digite o valor do 2º Produto: "))
produto3 = float(input("Digite o valor do 3º Produto: "))

total = produto1 + produto2 + produto3
vista = total * 0.95
credito = total * 1.075
print()
print(f"|Total: R${total}")
print()
print("||Formas de Pagamento||")
print(f"À Vista (dinheiro): R${vista}")
print(f"Crédito: R${credito}")
print(f"Débito: R${total}")