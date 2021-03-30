tupla = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez'
       ,'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')


while True:
    n = int(input('Digite um número inteiro entre zero e vinte: '))
    if 0 <= n <= 20:
        break

print(f'Seu número digitado por extenso é {tupla[n]}')
