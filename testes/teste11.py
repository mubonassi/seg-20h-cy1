#Importando Bibliotecas
#import -> Importando bibliotecas prontas

import math #Importa uma biblioteca de funções matemáticas especificas

num1 = 400
num2 = 35
divisao = num1/num2
arredondado = math.floor(divisao)
raizQuadrada = math.sqrt(num1)
pi = math.pi

print(f"Divisão: {divisao} | Arredondado: {arredondado}")
print(f"Raiz Quadrada: {raizQuadrada} | Pi: {pi}")

import random #importa funções que geram valores aleatórios

valor = random.randint(1,100)
print(f"Valor aleatório: {valor}")

lista = ["a","b","c","d","e","f"]
itemAleatorio = random.choice(lista)
print(f"Item Escolhido: {itemAleatorio}")