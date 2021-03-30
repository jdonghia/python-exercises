mais_18 = homens = mulheres_20 = 0

while True:

    sexo = continuar = ' '

    idade = int(input('Digite a idade: '))

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Maiores de 18: {mais_18}\n'
      f'Homens castrados: {homens}\n'
      f'Mulheres com menos de 20 anos: {mulheres_20}.')



