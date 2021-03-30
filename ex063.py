print("~" * 25)
print("SEQUÊNCIA DE FIBONACCI")
print("~" * 25)

termo = int(input("Quantos termos você deseja visualizar?: "))

t1 = 0
t2 = 1

c = 3
#os 3 primeiros termos são necessários ser declarados

print(t1,t2, end = " ")
while c <= termo:
    t3 = t1 + t2
    t1 = t2
    t2 = t3
    c += 1
    print(t3, end = " ")



