import random
cont = 0
maior = -100000
while cont<7487659:
    valor = random.randint(1,1000)
    if valor > maior:
        maior = valor
    cont+=1
    print(cont)
print(f'O maior valor é: {maior}')