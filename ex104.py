def leia_int(str):
    num = input(str)
    if num.isnumeric():
        print(f'O número {num} possui um valor inteiro!')
    else:
        while num.isnumeric() == False:
            return leia_int('Inválido! Digite um valor inteiro: ')

num = leia_int('Digite um número: ')

