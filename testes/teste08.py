#Estruturas de Repetição
#Uma estrutura que irá repetir em loop (contínuo ou contado) um bloco de código

#Repetição Contada (quantidade definida)
#Estrutura For com a função Range(x) -> Que define quantas vezes o loop será feito
for i in range(5): #O código irá se repetir 5x
    print("Teste de Repetição!")
print("Fim da Repetição!")

#Utilizando a variável da repetição no contexto do código
for i in range(5):
    print(f"Repetição #{i}")
print("Fim da Repetição")

#Determinando em qual número irá começar no range(x)
for i in range(1,6):
    print(f"Repetição #{i}")
print("Fim da repetição")

#Determinar os intervalos contados do range(x)
for i in range(10,101,10):
    print(f"Repetição #{i}")
print("Fim da Repetição!")

#Repetindo dentro da lista/variável/string
lista = ["a","b","c","d","e"]

for i in lista:
    print(i)
print("Fim da Repetição!")

for i in "banana":
    print(i)
print("Fim da repetição")