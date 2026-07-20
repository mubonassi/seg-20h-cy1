print("| VERIFICADOR DO BAR |")
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"Seja bem vindo, {nome}")
else:
    print(f"Desculpa, {nome}, você não pode entrar")