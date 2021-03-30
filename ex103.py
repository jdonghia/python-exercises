def ficha(nome=0,gols=0):
    if nome.isalpha() == False:
        nome = '<desconhecido>'
    else:
        nome = str(nome).strip().title()
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return (f'O jogador {nome} fez {gols} gol(s) no campeonato')

nome = input('Nome do jogador: ')
gols = input('Número de gols: ')
print(ficha(nome,gols))

 