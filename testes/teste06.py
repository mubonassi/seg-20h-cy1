#Formatação e Manipulação de Strings/Print
numero1 = 10
numero2 = 3
resultado = numero1/numero2
print(f"{numero1}/{numero2} = {resultado} << Sem formatação")

#Limitando as casas decimais do float no print
#Função: :.0f
#Obs: Necessita ser usado no 'f' do print -> print(f"")
print(f"{numero1}/{numero2} = {resultado:.2f} << Com formatação")

#Manipulação de texto/string
palavra = input("Digite uma palavra aleatória: ")
frase = input("Digite uma frase aleatória: ")

#Função upper() -> Deixa tudo maiusculo
print(palavra.upper())

#Função lower() -> Deixa tudo minusculo
print(palavra.lower())

#Função capitalize() -> deixa a primeira letra da string maiuscula
print(palavra.capitalize())

#Função title() -> deixa a primeira letra de cada palavra da string maiuscula
print(frase.title())

#Alinhando Texto
#função: :^ alinha o texto colocando espaços vazios
#Obs: Necessita ser usado no 'f' do print -> print(f"")
print(f"{frase:^30}")