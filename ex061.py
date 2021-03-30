termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da PA: "))

c = 1
quantT = 10

print("10 primeiros termos da PA...")

while c <= 10:
    pa = termo + (c - 1) * razao
    c += 1
    print(pa, end = " ")