produtos = []

produto = input("Nome do produto: ")
produtos = produtos + [produto]

resposta = input("Deseja adicionar outro? (s/n): ")

while resposta == "s":
    produto = input("Nome do produto: ")
    produtos = produtos + [produto]
    resposta = input("Deseja adicionar outro? (s/n): ")

print("Lista de produtos:")
print(produtos)