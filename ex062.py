termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao da PA: "))

c = 1
quantT = 10

print("10 primeiros termos da PA...")

while c <= 10:
    pa = termo + (c - 1) * razao
    c += 1
    print(pa, end = " ")

    if c > 10:
        print()
        continuar = int(input("Quanto termos você quer mostrar a mais?: "))

        while continuar != 0:

            quantT += continuar

            while c <= quantT:
                pa = termo + (c - 1) * razao
                c += 1
                print(pa, end = " ")

            print()

            continuar = int(input("Quanto termos você quer mostrar a mais?: "))

            if continuar == 0:
                print(f"Progressão finalizada com {quantT} termos mostrados.")








