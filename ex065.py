maior = menor = soma = n = cont = 0
ver = 'S'

while ver == 'S':
    n = int(input('Digite um número inteiro: '))
    soma += n
    cont += 1
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    ver = str(input('Quer continuar? [S/N]: ')).strip().upper()

print(f'A média dos valores digitados é {soma / cont:.2f}\n'
      f'O menor valor digitado foi {menor}\n'
      f'O maior valor digitado foi {maior}')


