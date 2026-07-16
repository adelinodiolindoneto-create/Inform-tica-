while True:
    valor = float(input("Digite o valor da compra: "))
    print('-' * 50)
    
    opcao = int(input(f"""[1] À vista 15% de desconto
[2] Cartão de débito 10% de desconto
[3] Cartão de crédito 5% de desconto
[0] Sair do programa
Selecione a opção desejada: """))
    print('-' * 50)
    
    if opcao == 0:
        print("Programa encerrado. Obrigado!")
        break
    
    if opcao == 1:
        desconto = valor * 0.15
        valor_final = valor * 0.85
        print(f"O valor do desconto é de R${desconto:.2f} e o valor final a ser pago é de R${valor_final:.2f}")
    elif opcao == 2:
        desconto = valor * 0.10
        valor_final = valor * 0.90
        print(f"O valor do desconto é de R${desconto:.2f} e o valor final a ser pago é de R${valor_final:.2f}")