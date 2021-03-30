from random import randint

pc = randint(0,5)

user = int(input("Pensei em um número entre 0 e 5, tente adivinhar!: "))
print(f"Eu pensei no número {pc}!")

if pc == user:
    print(f"Parabéns, você adivinhou!")
else:
    print(f"Você errou.")


