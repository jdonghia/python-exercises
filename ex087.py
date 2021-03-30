#preferência por listas compostas

matriz = [[],[],[]]
soma_pares = soma_terceira = 0
for x in range(3):
    for y in range(3):
        valor = int(input(f'Digite um valor para a posição [{x,y}]: '))
        matriz[x].append(valor)
        if valor % 2 == 0:
            soma_pares += valor
        if y == 2:
            soma_terceira += valor
print('=-'*30)
for x in range(3):
    for y in range(3):
        print(f'[{matriz[x][y]:^5}]', end = ' ')
    print()

print('=-'*30)
print(f'A soma dos valores pares: {soma_pares}\n'
      f'A soma dos valores da terceira coluna: {soma_terceira}\n'
      f'O maior valor da segunda linha: {max(matriz[1])}')

