#Estrutura de Condição - Encadeada e Composta
numero = int(input("Digite um número: "))

#Estrutura de Condição Encadeada -> Elif
#Elif -> else if -> senão se -> outra condição/pergunta caso a anterior retorne negativo
if numero == 1234: #se o número for 1234
    print("Foi digitado 1234")
elif numero > 1234: #ou se o número for maior que 1234
    print("Foi digitado acima de 1234")
else: #senão
    print("Foi digitado abaixo de 1234")

#Estrutura de Condição Composta -> And Or
#Or -> Uma das condições devem ser verdadeiras
if numero == 100 or numero == 200:
    print("Você digitou 100 ou 200")
else:
    print("Você não digitou 100 ou 200")

#And -> Todas as condições devem ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você não digitou um número entre 0 a 10")