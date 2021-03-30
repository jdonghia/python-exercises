n1 = float(input("Digite um valor: "))
n2 = float(input("Digite outro valor: "))

opcao = 0

while opcao != 5:
    print("[1] Somar\n"
          "[2] Multiplicar\n"
          "[3] Maior\n"
          "[4] Novos números\n"
          "[5] Sair do programa")
    opcao = int(input("O que deseja fazer?: "))
    if opcao == 1:
        print(f"A soma entre {n1} e {n2} vale {n1+n2}")
    elif opcao == 2:
        print(f"Multiplicando {n1} por {n2} nós temos {n1*n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior número é {n1}")
        elif n2 > n1:
            print(f"O maior número é {n2}")
    elif opcao == 4:
        n1 = float(input("Digite um valor: "))
        n2 = float(input("Digite outro valor: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Operação inválida, tente novamente!")

print("Obrigado, volte sempre!")







