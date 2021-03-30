from datetime import date
nasc = int(input("Digite seu ano de nascimento: "))
idade = date.today().year - nasc
if idade <= 9:
    print("Mirim")
elif idade <= 14:
    print("Infantil")
elif idade <= 19:
    print("Júnior")
elif idade <= 25:
    print("Sênior")
elif idade < 25:
    print("Master")