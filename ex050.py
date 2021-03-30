soma = 0

for c in range(1,7):
    n = int(input(f"Digite o {c} número inteiro: "))
    if n % 2 == 0:
        soma = soma + n

print(f"A soma dos números pares é de {soma}")