a = int(input("Digite a primeira medida: "))
b = int(input("Digite a segunda medida: "))
c = int(input("Digite a terceira medida: "))

if a < b + c and b < a + c and c < b + a:
    print("Essas medidas podem formar um triângulo.")
    if a == b == c:
        print("Este triângulo é equilátero!")
    elif a == b or a == c or b == c:
        print("Este triângulo é isósceles!")
    elif a != b != c != a:
        print("Esté triângulo é escaleno!")
else:
    print("Estas medidas não podem formar um triângulo.")
