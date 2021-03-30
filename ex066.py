soma = cont = 0

while True:
    n = int(input('Digite um número inteiro / [999] para parar: '))
    if n == 999:
        break
    soma += n
    cont += 1



print(f'Você digitou {cont} números.\n'
      f'A soma dos valores digitados é de {soma}.')