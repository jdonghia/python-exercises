mediaIdade = contF = 0
maisV = 0

for person in range(1,5):
    nome = str(input(f"Digite o nome da {person}ª pessoa:")).strip().title()
    idade = int(input(f"Digite a idade da {person}ª pessoa: "))
    sexo = str(input(f"Digite o sexo da {person}ª pessoa [M/F]: ")).strip().title()

    if person == 1:
        maior = menor = idade

    elif maisV == 0:
        maisV = nome

    elif sexo[0] == "F" and idade < 20:
        contF += 1

    elif sexo[0] == "M" and idade > maior:
        maisV = nome

    mediaIdade += idade / 4

print(f"A média das idades digitadas é de {mediaIdade}.")
print(f"O nome do homem mais velho é {maisV}.")
print(f"{contF} mulheres possuem menos de 20 anos.")
