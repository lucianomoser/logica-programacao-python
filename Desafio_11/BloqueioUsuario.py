usuario = input("Nome do usuário: ")
senha = input("Senha do usuário: ")


if usuario == "aluno" and senha == "segredo":
    print("Bem vindo")
else:
    print("O login não foi efetuado. Você terá três tentativas, caso contrario você será bloqueado!")
    for i in range(1, 4):
        print(f"Tentativa {i}")
        usuario = input("Nome do usuário: ")
        senha = input("Senha do usuário: ")
        if usuario == "aluno" and senha == "segredo":
            print("Bem vindo")
            break
    if usuario != "aluno" or senha != "segredo":
        print("Seu usuário foi bloqueado!")











