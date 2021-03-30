lista = []
maior = menor = 0

for c in range(5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > maior:
        maior = menor = n
        print(f'Valor {n} adicionado no fim da lista...')
        lista.insert(4,n)
    if n < menor:
        menor = n
        lista.append(n)







print(lista)