preco = float(input("Digite o preço do produto R$"))
print("OPÇÕES DE PAGAMENTO\n"
      "[1] Dinheiro / Cheque\n"
      "[2] À vista no cartão\n"
      "[3] 2x no cartão\n"
      "[4] 3x ou mais no cartão")
opcao = int(input("Qual forma de pagamento?: "))

if opcao == 1:
    preco = preco*0.90
    print("Disponibilizamos 10% de desconto para pagamento à vista no dinheiro ou cheque\n"
          f"O valor a pagar será de R${preco:.2f}.")
elif opcao == 2:
    preco = preco*0.95
    print("Disponibilizamos 5% de desconto para pagamentos à vista no cartão\n"
          f"O valor a pagar será de R${preco:.2f}.")
elif opcao == 3:
    print("Não disponibilizamos descontos para pagamento em 2x no cartão\n"
          f"Serão 2 parcelas de R${preco/2:.2f} cada.")
elif opcao == 4:
    parcelas = int(input("Quantos parcelamentos?: "))
    preco = preco*1.20
    print("Parcelas de 3x ou mais possuem um juros de 20% sobre o valor total\n"
          f"Serão {parcelas} parcelas de R${preco/parcelas:.2f} cada.")