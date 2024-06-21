idades = []
while True:
    idade = int(input("Informe sua idade (-1 para sair):"))
    if idade == -1:
        break
    idades.append(idade)

maior18 = 0

'''
for i in range(0,len(idades)):
    if idades[i] > 18:
        maior18+=1
'''
for age in idades:
    if age > 18:
        maior18+=1

media = sum(idades)/len(idades)

print(f'A média de idade {media} e {maior18} tem mais de 18 anos.')

