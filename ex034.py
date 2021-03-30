salario = float(input("Digite seu salário R$"))
if salario > 1250:
    salario = salario*1.10
else:
    salario = salario*1.15
print(f"Seu salário passará a valer R${salario:.2f}")