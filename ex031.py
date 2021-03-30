km = float(input("Digite a distância da viagem em Km: "))
if km <= 200:
    passagem = km * 0.50
    print(f"A passagem custará R${passagem:.2f}")
else:
    passagem = km * 0.45
    print(f"Viagens acima de 200Km recebem um desconto. A passagem custará {passagem:.2f}")