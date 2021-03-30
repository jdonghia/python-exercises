print("Digite [1] para conversão binária\n"
      "Digite [2] para conversão octal\n"
      "Digite [3] para conversão hexadecimal ")
n = int(input("Digite um número inteiro: "))
prompt = int(input("Digite o comando: "))
if prompt == 1:
    print(f"Conversão binária {bin(n)}")
elif prompt == 2:
    print(f"Conversão octal {oct(n)}")
elif prompt == 3:
    print(f"Conversão hexadecimal {hex(n)}")
