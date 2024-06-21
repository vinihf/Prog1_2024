lista1 = []
lista2 = []
lista3 = []

for x in range(0,5):
    valor = input(f'Informe o valor {x}:')
    lista1.append(valor)

for x in range(0,5):
    valor = input(f'Informe o valor {x}:')
    lista2.append(valor)

for x in range(0,5):
    lista3.append(lista1[x])
    lista3.append(lista2[x])

print(lista3)