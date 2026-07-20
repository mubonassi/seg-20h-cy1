#Listas (Array)

#Lista em String
items = ["item1","item2","item3","item4"]

#Lista Mista de Tipos de Dados (Aviso: Deve-se tomar cuidado com os tipos)
items2 = ["item1",2,2.4,True]

#Exibindo a lista completa
print(items)
print(items2)

#Exibindo items especificos da lista
#Ordem: 0 1 2 3 4...
print(f"Item 1 da 1ª Lista: {items[0]}")
print(f"Item 3 da 2ª Lista: {items2[2]}")

#Declarando a lista e depois alimentando (Método Fácil)
numeros = [0,0,0]
numeros[0] = int(input("Digite o número 1: "))
numeros[1] = int(input("Digite o número 2: "))
numeros[2] = int(input("Digite o número 3: "))
resultado = numeros[0] + numeros[1] + numeros[2]
print(f"{numeros[0]} + {numeros[1]} + {numeros[2]} = {resultado}")

#Declarando a lista e adicionando os items depois (Método mais avançado)
frutas = []
#Função .append() adiciona um item dentro da lista
frutas.append("Maracuja")

#Usando .append() com input()
frutas.append(input("Digite uma fruta: "))
frutas.append(input("Digite outra fruta: "))
print(frutas)

#Usando input() para buscar um item
item = int(input("Agora digite qual a sua fruta favorita (de 0 a 2): "))
print(f"Então, sua fruta favorita é {frutas[item]}")