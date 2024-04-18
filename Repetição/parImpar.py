p1 = 0
p2 = 0
contador = 1

while contador <=3:
    j1 = int(input(f'J1 - Informe sua jogada {contador}:'))
    j2 = int(input(f'J2 - Informe sua jogada {contador}:'))
    if (j1+j2)%2==0:
        print("par")
        p1+=1
    else:
        print("ímpar")
        p2+=1
    contador+=1

if p1>p2:
    print("Venceu P1")
else:
    print("Venceu P2")