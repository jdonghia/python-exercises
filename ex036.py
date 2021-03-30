vCasa = float(input("Digite o valor da casa R$"))
salario = float(input("Digite seu salário R$"))
anos = float(input("Em quantos anos pagará?: "))
qParcelas = anos*12
vParcelas = vCasa / qParcelas
if vParcelas > salario*0.30:
    print("Empréstimo negado")
else:
    print(f"O valor da prestação mensal será de R${vParcelas:.2f}")