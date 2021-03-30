from random import randint
lista_player = []
lista_jogada = []

for player in range(1,5):
    pc = randint(1,6)
    print(f'O jogador {player} jogou o dado e caiu {pc}')
    lista_player.append(player)
    lista_jogada.append(pc)

dict = {'Jogador':lista_player,'Jogada':lista_jogada}

