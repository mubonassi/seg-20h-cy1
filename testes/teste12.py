#Funções
#Funções permitem que possamos criar blocos de códigos que determinamos qual momento serão executados

#Função simples
#estrutura 'def'
def exibirTexto():
    print("Exibindo esse texto!")

exibirTexto()

#Função simples com return
#Return devolve um valor para quem chamou a função
def calcularConta():
    conta = 10+20-30*40/50**60//70
    return conta

resultado = calcularConta()
print(resultado)

#Função com parametros
#Necessita informações externas para se calcular internamente
def somarNumeros(num1,num2):
    resultado = num1 + num2
    print(resultado)

somarNumeros(10,20)

def subtrairNumeros(num1,num2):
    resultado = num1 - num2
    return resultado

valor = subtrairNumeros(10,20)
print(valor)