import random

nomes = []

nome = input("Nome de quem comprou a rifa (digite fim para parar): ")

while nome != "fim":
    nomes = nomes + [nome]
    nome = input("Nome de quem comprou a rifa (digite fim para parar): ")

if nomes == []:
    print("Ninguém comprou a rifa.")
else:
    ganhador = random.choice(nomes)
    print("O ganhador é:", ganhador)