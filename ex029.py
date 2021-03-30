vel = float(input("Qual a velocidade do carro em Km/h?: "))
if vel > 80:
    print("Você foi multado!")
    ultrapassado = vel - 80
    multa = ultrapassado * 7
    print(f"A multa será de R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade permitida!")
