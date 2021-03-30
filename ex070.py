total_gasto = produto_maior_1000 = mais_barato = 0
produto_mais_barato = ' '

while True:
    produto = str(input('Digite o nome do produto: ')).strip().title()

    preco = float(input('Digite o preço do produto R$: '))
    total_gasto += preco

    if preco > 1000:
        produto_maior_1000 += 1

    if mais_barato == 0:
        mais_barato = preco

    if preco < mais_barato:
        produto_mais_barato = produto

    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'O total gasto da compra foi de R${total_gasto:.2f}\n'
      f'{produto_maior_1000} produtos custam mais de R$1000,00\n'
      f'{produto_mais_barato} é o produto mais barato.')


