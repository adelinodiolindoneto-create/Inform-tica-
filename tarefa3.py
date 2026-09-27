

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
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Editar usuário")
        print("4 - Excluir usuário")
        print("5 - Sair da conta")
        print("6 - Encerrar o programa")

        opcao = input("Digite o número da opção: ")

        if opcao == "5":
            print("Saindo da sua conta...")
            break
        elif opcao == "6":
            print("Encerrando o programa, até mais!")
            sair_do_programa = True
            break
        elif opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("Essa opção ainda vai ser feita mais pra frente.")
        else:
            print("Não entendi essa opção, tenta de novo.")

        print("")

    if sair_do_programa == True:
        break
