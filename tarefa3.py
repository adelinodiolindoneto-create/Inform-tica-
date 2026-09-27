while True:

    print("Bem-vindo ao sistema de cadastro de usuários!")

    while True:
        usuario = input("Digite seu usuário: ")
        senha = input("Digite sua senha: ")

        if usuario == "admin" and senha == "123":
            print("Login realizado com sucesso!")
            break
        else:
            print("Usuário ou senha incorretos, tente de novo.")

    print("")

    sair_do_programa = False

    while True:
        print("O que você deseja fazer?")
        print("1 - Sair da conta")
        print("2 - Encerrar o programa")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            print("Saindo da sua conta...")
            break
        elif opcao == "2":
            print("Encerrando o programa, até mais!")
            sair_do_programa = True
            break
        else:
            print("Não entendi essa opção, tenta de novo.")

        print("")

    if sair_do_programa == True:
        break
