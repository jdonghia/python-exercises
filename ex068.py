from random import randint

print('PAR OU ÍMPAR')

vitorias = 0
escolha_user = ' '

while True:
    numero_user = int(input('Digite um número inteiro: '))

    while escolha_user not in 'PI':
        escolha_user = str(input('PAR OU ÍMPAR? [P/I]: ')).strip().upper()[0]

    pc = randint(1,100)
    soma = numero_user + pc

    print(f'Você jogou {numero_user} e o computador jogou {pc}.')
    print(f'A soma entre os valores é {soma}')
    print('A soma deu PAR!' if soma % 2 == 0 else 'A soma deu ÍMPAR!' )

    if soma % 2 == 0 and escolha_user == 'P' or soma % 2 != 0 and escolha_user == 'I':
        print('Você venceu! Vamos jogar novamente...')
        vitorias += 1
    else:
        print('Você perdeu!')
        break

print(f'Você venceu {vitorias} vez(es) seguida(s)!')




