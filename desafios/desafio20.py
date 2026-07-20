print("| SISTEMA DE CADASTRO |")
cadUsuario = input("Digite o nome do usuário: ").lower()
cadSenha = input("Digite a senha: ")

print("**CADASTRADO COM SUCESSO**")
print("-"*30)

print("| LOGIN DA CONTA |")
loginUsuario = input("Usuário: ").lower()
loginSenha = input("Senha: ")

if loginUsuario == cadUsuario and loginSenha == cadSenha:
    print(f"Usuário {loginUsuario} autenticado com sucesso! Seja bem vindo!")
else:
    print(f"Usuário {loginUsuario} não encontrado, verifique se o nome ou a senha estão incorretos!")