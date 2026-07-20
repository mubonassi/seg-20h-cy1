print("LOJA DE JOGOS")

catalogo = ["candy crush","candy crush 2","candy crush HD","candy crush XD","candy crush battle royale", "candy crush open world","candy crush strike"]
print(f"Catalogo de Jogos: {catalogo}")
jogo = input("Escolha um jogo do catalogo: ")

if jogo in catalogo:
    print(f"Você comprou {jogo}, bom jogo!")
else:
    print(f"O produto {jogo} não está no catalogo!")