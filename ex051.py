termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razão da PA: "))

print("10 primeiros termos da PA...")

for c in range(1,11):
    pa = termo + (c - 1) * razao
    print(pa, end = " ")


