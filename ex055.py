maior = menor = 0

for person in range(1,7):
    peso = float(input(f"Digite o peso da {person}ª pessoa: "))
    if person == 1:
        maior = menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O maior peso digitado foi de {maior}!")
print(f"O menor peso digitado foi de {menor}!")
