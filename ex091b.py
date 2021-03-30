from random import randint

dic = {'Jogador 1': randint(1,6),
       'Jogador 2': randint(1,6),
       'Jogador 3': randint(1,6),
       'Jogador 4': randint(1,6)}

for k,v in dic.items():
    print(f'Jogador {k} tirou {v}')







