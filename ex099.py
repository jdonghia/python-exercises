def maior(*n):
    print('Analisando os valores passados...')
    print(f'{n} foram informados {len(n)} valores ao todo')
    print(f'O maior valor informado foi {max(n)}')

maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()

