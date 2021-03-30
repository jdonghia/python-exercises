def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if idade < 16:
        return f'Com {idade} anos, NÃO É PERMITIDO VOTAR, somente a partir dos 16 anos'
    elif 16 <= idade <= 17:
        return f'Com {idade} anos, o voto é OPCIONAL'
    elif idade >= 18:
        return f'Com {idade} anos, o voto é OBRIGATÓRIO'

nasc = int(input('Digite seu ano de nascimento: '))
print(voto(nasc))

