km = float(input("Quantos KM o carro percorreu?: "))
dias = int(input("Quantos dias ele permaneceu alugado?: "))
preco = (dias*60) + (km*0.15)
print(f"O preço a pagar será de R${preco:.2f}")