#Variaveis - Espaços na memória do programa para guardar uma informação
#Declarar Variável - Atribuindo um Valor dentro da Variavel
#exemplo: nome_da_variavel = valor
nome = "Murilo Bonassi" #<- string
idade = 31 #<- int/inteiro
altura = 1.67 #<- float/numero real
trabalha = True #<- binário/boolean (True/False)
calculo = 10*2-(10+3)

#Exibindo as Informações
print(f"Meu nome é {nome}")
print(f"Eu tenho {idade} anos")
print(f"Eu tenho altura de {altura}m")
print(f"Minha situação de trabalho é {trabalha}")
print(f"10*2-(10+3) = {calculo}")

#Tipos de Informações
#Informação de Entrada - Computador recebe informação

#Recebendo as Informações dentro da Variavel
#Comando input() -> recebe informação de entrada como *TEXTO*
#exemplo: variavel = input()
nome = input("Digite o seu nome: ")

#Convertendo Variaveis
#exemplo: variavel = tipo(valor)
#exemplo2: numero = int("32")
idade = int(input("Digite a sua idade: ")) #string para int
altura = float(input("Digite a sua altura: "))#string para float
trabalha = input("Digite se você trabalha (sim/não): ")#NÃO SE CONVERTE PARA BOOLEAN
calculo = eval(input("Digite um calculo para ser realizado: ")) #string para função em python (USE APENAS PARA TESTES)

#Prática - Exiba todas essas variáveis em um ÚNICO PRINT
print(f"Seu nome é {nome}. Você tem {idade} anos. Você {trabalha} trabalha. E o resultado do seu cálculo foi {calculo}")