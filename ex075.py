n = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

tupla = (n,n2,n3,n4)

print(f'O 9 apareceu {tupla.count(9)} vez(es)')
if 3 in tupla:
    print(f'O primeiro 3 apareceu na {tupla.index(3) + 1}ª posição')
for dados in tupla:
    if dados % 2 == 0:
        print(f'O número {dados} é par')

