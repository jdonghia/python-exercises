n = int(input("Digite um número inteiro: "))

cont = 0

for c in range(1, n + 1):
    if n % c == 0:
        cont += 1

if cont == 2:
    print(f"O número {n} É PRIMO!")
else:
    print(f"O número {n} NÃO É PRIMO!")
