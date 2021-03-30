from datetime import date

maioridade = 0
menoridade = 0

for c in range(1,8):
    nasc = int(input(f"Digite o ano de nascimento da {c}ª pessoa: "))
    idade = date.today().year - nasc
    if idade >= 18:
        maioridade += 1
    elif idade < 18:
        menoridade += 1

print(f"{menoridade} pessoas são menores de idade.")
print(f"{maioridade} pessoas ja são maiores de idade.")