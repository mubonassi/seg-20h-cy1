#Estruturas de Condição -> Criam condições para que um bloco de código seja executado
#Tal função() só acontece se a condição determinada for verdadeira
#Condição > Ação
#Ex: Se o numero digitado for 13 acontece a mensagem "você digitou o numero 13"

numero = int(input("Digite um número para ser verificado: "))

#se (condição) então
#   {ação}
#senão
#   {ação}
if numero == 13:
    print("Você digitou o número 13")
else:
    print("Você NÃO digitou o número 13")

#Comparadores
# == -> Igual a (valor == valor)
# > -> Maior que (valor > valor)
# < -> Menor que (valor < valor)
# >= -> Maior ou Igual a (valor >= valor)
# <= -> Menor ou Igual a (valor <= valor)
# != -> Diferente de (valor != valor)

#Diferença entre = e ==
# = -> Atribuição -> Nome = "Gabriel" -> O nome é Gabriel
# == -> Comparação -> Nome == "Gabriel" -> O nome é Gabriel?