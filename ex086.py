matriz = [[],[],[]]
x = y = 0

for x in range(3):
    for y in range(3):
        matriz[x].append(int(input(f' Digite um valor para a posição [{x,y}]: ')))

print('=-'*30)

for x in range(3):
    for y in range(3):
        print(f'[{matriz[x][y]:^10}]', end = ' ')
    print()
