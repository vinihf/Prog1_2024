quantidade = 0
soma = 0
mais18 = 0
while True:
    idade = int(input("Informe a sua idade (-1 para sair): "))
    if idade == -1:
        break
    soma += idade
    quantidade += 1
    if idade > 18:
        mais18+=1
media = soma/quantidade
print(f'A média de idade é {media:4.2f} e {mais18} tem mais de 18 anos.')