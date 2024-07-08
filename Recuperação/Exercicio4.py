def divisoes(x):
    div = 0
    while x>2:
        x = x/2
        div+=1
    return div

while True:
    valor = int(input("Informe um valor:"))
    if valor >=120 and valor<1002:
        qtd = divisoes(valor)
        print(f'{valor} foi dividido {qtd} por 2.')
        break
    else:
        print("Valor inválido!")