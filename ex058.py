from random import randint

pc = randint(1,10)

user = int(input("Pensei em um número inteiro entre 0 e 10, tente adivinhar!: "))
palpites = 1

while pc != user:
    user = int(input("Você errou! Tente até adivinhar!:  "))
    palpites += 1

print(f"Eu pensei no número {pc}!")
print("VOCÊ ACERTOU!")
print(f"Foram necessários {palpites} tentativa(s) para você acertar!")

