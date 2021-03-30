def fatorial(num,show):
    c = num
    f = 1
    while c > 1:
        f *= c
        c -= 1
        if show == True:
            if f == 1:
                print(num, end=" x ")
            if c > 1:
                print(c, end=" x ")
            else:
                print(c, end=" = ")
    print(f)

fatorial(int(input('Digite um número inteiro para visualizar seu fatorial: ')),
         bool(input('Deseja visualizar a conta? [Digite para S/Enter para N]: ')))

