soma = 0
quantidade = 0
maior = None

print("Digite números inteiros positivos (digite um número negativo para parar):")

while True:
    numero = int(input("Digite um número: "))
    
    if numero < 0:
        break
    
    soma += numero
    quantidade += 1
    
    if maior is None or numero > maior:
        maior = numero

if quantidade > 0:
    media = soma / quantidade
    print("\n--- Resultados ---")
    print(f"a) A soma de todos os números positivos: {soma}")
    print(f"b) A média aritmética dos números: {media:.2f}")
    print(f"c) O maior dos números positivos: {maior}")
else:
    print("\nNenhum número positivo foi informado.")