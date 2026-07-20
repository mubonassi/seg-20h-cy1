#Usando lista(array) com comparadores

items = ["'item1'",'item2','item3','item4']
print(f"Lista: {items}")

#Realizando a comparação
item = input("Digite um item da lista: ")

#Comparador IN -> verifica se está dentro da lista/variavel
if item in items:
    print("Você escolheu um item da lista!")
else:
    print("Você NÃO escolheu um item da lista!")

#Realizando outra comparação
item = input("Digite um item QUE NÃO ESTÁ na lista: ")

#Invertendo uma pergunta
#Comparador NOT IN -> verifica se não está dentro da lista
if item not in items:
    print("O item não está na lista")
else:
    print("O item está na lista, digite novamente!")

numero = 10
if not numero == 10:
    print("O número não é 10")