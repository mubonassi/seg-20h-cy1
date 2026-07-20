print("| CONVITE DE FESTA |")

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
print("Responda com 'sim' ou 'não'")
convite = input("Você tem convite da festa?: ").lower()

if idade < 21:
    print(f"Você não pode entrar na festa, {nome}! Tem restrição de idade!")
else:
    if convite == 'não':
        print(f"Você precisa de convite para entrar na festa, {nome}!")
    else:
        print(f"Seja bem vindo a festa, {nome}!")