print("|Aumento de 10%|")
print("-"*20)

#Solução 1 - Utilizando uma segunda variável para calculo
valor = float(input("Digite um valor para receber acréscimo: "))
acrescimo = valor + (valor/10) #1
acrescimo = valor * 1.10 #2
acrescimo = valor + (valor*0.1) #3

print (f"O Acréscimo foi de: {acrescimo}")

#Solução 2 - Alterando a variável
valor = valor * 1.10