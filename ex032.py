ano = int(input("Digite um ano qualquer: "))
if ano % 4 == 0 and ano % 100 != 0:
    print(f"O ano é {ano} é bissexto")