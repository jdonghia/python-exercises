lista_pesos = []
lista_nomes = []
while True:
    lista_nomes.append = str(input('Digite seu nome: ')).strip().title()
    lista_pesos.append = float(input('Digite seu peso: '))
    ver = ' '
    while ver not in 'SN':
        ver = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if ver == 'N':
        break
print(f'{len(lista_nomes)} pessoas foram cadastradas.')
print(f'Maior peso: {max(lista_pesos)}; Peso de : ', end = ' ')
for c in range(len(lista_pesos)):
    if lista_pesos[c] == max(lista_pesos):
        print(lista_nomes[c], end = ' ')
print()
print(f'Menor peso: {min(lista_pesos)}; Peso de : ', end = ' ')
for c in range(len(lista_pesos)):
    if lista_pesos[c] == min(lista_pesos):
        print(lista_nomes[c], end = ' ')

