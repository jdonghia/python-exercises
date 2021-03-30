#a medida de um lado precisa ser menor doq a soma das outras 2

a = float(input("Digite a primeira medida: "))
b = float(input("Digite a segunda medida: "))
c = float(input("Digite a terceira medida: "))

if a < b + c and b < a + c and c < a + b:
    print("Essas medidas podem formar um triângulo")
else:
    print("Essas medidas não podem formar um triângulo")
