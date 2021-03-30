from random import choice
from time import sleep

print("Vamos jogar pedra, papel ou tesoura!")

user = str(input("Faça sua escolha: ")).strip().title()
print(f"Você escolheu {user}!")

escolhas = ["Pedra","Papel","Tesoura"]

pc = choice(escolhas)
print("Eu escolhi...")
sleep(1)
print(pc)

if user == "Pedra":
    if pc == user:
        print("EMPATE!")
    elif pc == "Papel":
        print("VOCÊ PERDEU!")
    elif pc == "Tesoura":
        print("VOCÊ VENCEU!")

elif user == "Papel":
    if pc == user:
        print("EMPATE!")
    elif pc == "Tesoura":
        print("VOCÊ PERDEU!")
    elif pc == "Pedra":
        print("VOCÊ VENCEU!")

elif user == "Tesoura":
    if pc == user:
        print("EMPATE!")
    elif pc == "Pedra":
        print("VOCÊ PERDEU!")
    elif pc == "Papel":
        print("VOCÊ VENCEU!")



