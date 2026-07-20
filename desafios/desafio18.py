print("> Algoritmo de Entrevista <")
print("-"*30)
print("Responda com 'sim' ou 'não'")
pergunta = input("Então, você deseja trabalhar na empresa?: ")

if pergunta == "sim":
    print("Beleza! Bom saber que deseja trabalhar conosco!")
    pergunta = input("Você trouxe o seu currículo?: ")
    if pergunta == "sim":
        print("Vamos começar a entrevista, então!")
    else:
        print("Desculpa, precisamos do currículo")
else:
    print("Então, por que veio à entrevista?")