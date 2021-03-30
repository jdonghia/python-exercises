nome = str(input("Digite seu nome completo: ")).strip().title()

separado = nome.split()

print(f"Seu nome com letras maiúsculas: {nome.upper()}\n"
      f"Seu nome com letras minúsculas: {nome.lower()}\n"
      f"Seu nome possui {len(nome) - nome.count(' ')} letras\n"
      f"Seu primeiro nome possui {len(separado[0])} letras")