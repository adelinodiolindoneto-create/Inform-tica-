usuarios = []
logado = False
usuario_logado = ""

while True:
    print("##############################")
    print("SISTEMA DE CADASTRO DE USUARIO   ")
    print("##############################\n")

    if not logado:
        print("=====Login=====")
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")

        if login == "admin" and senha == "123":
            print(
                f"login realizado com  sucesso!Bem vindo, {login}!\n")
            input("Enter para continuar...")
            logado = True
            usuario_logado = login
        else:
            input("\n login ou senha incorretos! Enter para tentar novamente.")

    else:
        print("Menu principal")
        print(f"Usuario logado: {usuario_logado}")
        print("1 - Inserir usuario")
        print("2 - Pesquisar usuario")
        print("3 - Remover Usuario")
        print("4 - Lista de todos os Usuarios")
        print("5 - Logout")
        print("6 - Encerrar")
        opcao = input("Escolha uma opcao: ")

        if opcao == "1":
            print("\n--- INSERIR NOVO USUARIO ---")
            usuario = input("Digite o nome do usuario: ")

            if usuario in usuarios:
                print("este usuarios ja esta cadastrado!")
            else:
                usuarios.append(usuario)
                print(f"Usuario ' {usuario} ' cadastrado com sucesso")

            input("\nENTER para continuar...")

        elif opcao == "2":
            print("\n--- PESQUISAR USUARIO ---")
            usuario = input(
                "digite o nome do usuario que proucura: ")
            if usuario in usuarios:
                print(f"O usuario '{usuario}' foi encontrado no sistema")
            else:
                print(f"O usuario ' {usuario} ' nao foi encontrado")

            input("\nENTER para continuar...")

        elif opcao == "3":
            print("\n --- REMOVER USUARIO --- ")
            usuario = input("Digite o nome do usuario que deseja remover: ")

            if usuario in usuarios:
                usuarios.remove(usuario)
                print(f"Usuario ' {usuario}' removido com sucesso!")

            else:
                print("usuario nao encontrado na lista")

            input("\n ENTER para continuar...")

        elif opcao == "4":
            print("\n Lista de usuarios CADASTRADO")
            for usuario in usuarios:
                print(f"- {usuario}")

            input("\nENTER para continuar...")

        elif opcao == "5":
            print("Fazendo logout...")
            input("ENTER para voltar para o login.")
            usuario_logado = ""
            logado = False

        elif opcao == "6":
            print("Encerrando o sistema....Ate logo!")
            break

        else:
            input(
                "opcao invalida! ENTER para continuar;...")
