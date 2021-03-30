tupla = ('APRENDER','PROGRAMAR','LINGUAGEM','PYTHON','CURSO','GRATIS','ESTUDAR','PRATICAR','TRABALHAR',
         'MERCADO','PROGRAMADOR','FUTURO')

for dados in tupla:
    print(f'Na palavra {dados} nós temos as vogais', end = ' ')
    for letras in dados:
        if letras in 'AEIOU':
            print(letras, end = ' ')

    print()