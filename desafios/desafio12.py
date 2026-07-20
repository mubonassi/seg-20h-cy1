print("| Cadastrando um Filme |")

filme = []
filme.append(input("Digite o nome do filme: "))
filme.append(input("Digite o ano de lançamento: "))
filme.append(input("Digite o(s) gênero(s): "))

print("---------------------")
print(f"Nome: {filme[0]}")
print(f"Ano de Lançamento: {filme[1]}")
print(f"Gênero: {filme[2]}")

print(filme)