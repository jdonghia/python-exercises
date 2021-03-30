from math import sqrt

co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adajacente: "))
h = (co)**2 + (ca)**2
print(f"A hipotenusa vale {sqrt(h):.2f}")