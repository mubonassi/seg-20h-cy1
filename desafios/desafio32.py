print("| AUTENTICAÇÃO DO SISTEMA |")
usuario = "admin"
senha = "adm123"

for i in range(1,4):
    loginUsu = input("Usuário: ")
    loginSen = input("Senha: ")

    if loginUsu == usuario and loginSen == senha:
        print("Sistema autenticado com sucesso!")
        break
    else:
        print(f"Usuário incorreto! Tentativa {i} de 3")
        if i >= 3:
            print("Encerrando sistema...")
            quit()

print("- Verificador de Média -")
n1 = float(input("Digite a 1ª Nota: "))
n3 = float(input("Digite a 2ª Nota: "))
n2 = float(input("Digite a 3ª Nota: "))

m = (n1+n2+n3) / 3

print(f"Sua média deu {m}")

if m >= 6:
    print("Situação: Aprovado")
else:
    print("Situação: Reprovado")