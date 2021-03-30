from random import shuffle

aluno1 = str(input("Digite o primeiro aluno: "))
aluno2 = str(input("Digite o segundo aluno: "))
aluno3 = str(input("Digite o terceiro aluno: "))
aluno4 = str(input("Digite o quarto aluno: "))

alunos = [aluno1,aluno2,aluno3,aluno4]
shuffle(alunos)
print(f"A ordem será {alunos}")
