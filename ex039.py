nasc = int(input("Digite seu ano de nascimento: "))
idade = 2020 - nasc
if idade < 18:
    print(f"Você deverá se alistar daqui a {18-idade} anos!")
elif idade > 18:
    print(f"Você deveria ter se alistado a {idade-18} anos!")
elif idade == 18:
    print("Você deverá se alistar este ano!")