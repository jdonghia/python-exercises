def escreva(frase):
    tam = len(frase) + 4
    print('~'* tam)
    print(f'  {frase}')
    print('~' * tam)

frase = str(input('Digite uma frase: ')).strip().title()
escreva(frase)