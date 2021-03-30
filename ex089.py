lista = []
cont = 0

while True:
    name = str(input('Digite seu nome:')).strip().title()
    n1 = float(input('Digite a 1a nota: '))
    n2 = float(input('Digte a 2a nota: '))
    media = (n1+n2) / 2
    lista.append([name,n1,n2,media])

    ver = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if ver == 'N':
        for aluno in lista:
            print(f'{cont} {aluno[0]} / Média: {aluno[3]}')
            cont += 1
        while aluno != 999:
            aluno = int(input('Mostrar notas de qual aluno? [999] interrompe: '))
            if aluno != 999:
                print(f'Aluno: {lista[aluno][0]} / 1a Nota: {lista[aluno][1]} / 2a Nota: {lista[aluno][2]}')
        break

#Using another repetition estructure, its possible to realocate the dinamic repetition inside the code
#whatever, im using this kind of estructure to avoid waste on line codes, because once i already have a True loop
#reapeat, its not necessary to use another one.



