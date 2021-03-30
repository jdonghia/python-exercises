name = str(input('Nome: ')).strip().title()
media = float(input(f'Média de {name}: '))
dict = {'Nome': name, 'Média': media,'Situação':'Aprovado' if media >= 7 else 'Reprovado'}
for v,k in dict.items():
    print(f'{v}: {k}')

#i used the condition estructure in the dictionary to avoid waste and use less code lines,
#but, in another bigger case, the best way to avoid bugs, its using the dict['key'] = 'value'
