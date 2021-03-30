lista = []

while True:
    lista.append(int(input('Digite um valor: ')))

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

lista.sort(reverse = True)

print(f'Foram digitados {len(lista)} números!')
print(f'Lista dos números de forma decrescente: {lista}')

if 5 in lista:
    print(f'O valor 5 foi digitado e está na lista!')


