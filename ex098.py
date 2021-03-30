from time import sleep

def contador(i,f,p):
    if i < f:
        f += 1
    elif i > f:
        f -= 1
    if p > 0 and i > f:
        p = -p
    for c in range(i,f,p):
        print(c,end = ' ')
        sleep(0.2)
    print()

print('De 1 até 10 de 1 em 1...')
contador(1,10,1)
print('De 10 até 0 de 2 em 2...')
contador(10,0,2)

print('=-'*5,'CONTAGEM PERSONALIZADA','=-'*5)
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passos: '))

contador(i,f,p)