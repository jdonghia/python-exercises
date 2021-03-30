sexo = str(input("Digite seu sexo [M/F]: ")).strip().title()[0]

while sexo not in "MF":
    sexo = str(input("INVÁLIDO! Digite seu sexo [M/F]: ")).strip().title()[0]

print("Obrigado!")