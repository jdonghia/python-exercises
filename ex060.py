n = int(input("Digite um número inteiro para visualizar seu fatorial: "))

c = n
f = 1

print(n, end = " x ")
while c > 1:
    f *= c
    c -= 1
    if c > 1 :
        print(c, end = " x ")
    else:
        print(c, end = " = ")

print(f)