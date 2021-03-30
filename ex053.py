frase = str(input("Digite um frase: ")).strip().upper()

lista = list(frase)
reverse = lista[:]
reverse.reverse()

while " " in lista or " " in reverse:
    lista.remove(" ")
    reverse.remove(" ")

if lista == reverse:
    print("A frase É um PALÍNDROMO!")
else:
    print("A frase NÃO é um PALÍNDROMO!")