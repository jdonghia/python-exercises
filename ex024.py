cidade = str(input("Digite o nome da cidade:")).strip().title()
separado = cidade.split()
print("A cidade começa com Santo ? {}".format(separado[0] == "Santo"))