times = ('Atlético','Goias','Bragantino','Vasco','Internacional','Ceará','Fluminense','Sport',
         'Botafogo','São Paulo','Coritiba','Santos','Corinthians','Flamengo','Bahia','Palmeiras','Fortaleza',
         'Gremio','Chapecoense','Paraná')

print(f'Os cinco primeiros da colocação: {times[0:5]}')
print(f'Os últimos quatro colocados: {times[-4:]}')
print(f'Em ordem alfabética: {sorted(times)}')
print(f'O time Chapecoense está na {times.index("Chapecoense") + 1}ª posição')