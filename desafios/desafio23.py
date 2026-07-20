print("| HAPPY HOUR |")

funcionarios = ["João","Pedro","Maria","Murilo","Vitor","Rogério","Nadia","Royson","Gabriel"]
banidos = ["Murilo","Vitor"]

nome = input("Digite aqui o seu nome: ").capitalize()

if nome in funcionarios:
    if nome not in banidos:
        print("Seja bem vindo a festa!")
    else:
        print("Você está banido! Você lembra o que aconteceu no natal passado?")
else:
    print("Você precisa ser funcionário!")