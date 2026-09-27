programa_ligado = True

while programa_ligado == True:

    # ----- TELA DE LOGIN -----
    logado = False

    print("========================================")
    print("SISTEMA DE CADASTRO DE USUÁRIOS")
    print("========================================")
    print("--- LOGIN ---")

    while logado == False:
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        if usuario == "admin" and senha == "123":
            print("Login realizado com sucesso!")
            logado = True
        else:
            print("Usuário ou senha inválidos. Tente novamente.")

    # ----- TELA DE MENU -----
    print("")
    print("")  # linhas em branco para simular a tela "limpa"

    no_menu = True

    while no_menu == True:
        print("========================================")
        print("MENU PRINCIPAL")
        print("========================================")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Editar usuário")
        print("4 - Excluir usuário")
        print("5 - Logout")
        print("6 - Encerrar")

        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo da conta...")
            no_menu = False  # volta para a tela de login
        elif opcao == "6":
            print("Encerrando o programa...")
            no_menu = False
            programa_ligado = False  # encerra tudo
        elif opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4":
            print("Essa funcionalidade ainda não foi implementada.")
        else:
            print("Opção inválida!")

print("Programa encerrado.")
