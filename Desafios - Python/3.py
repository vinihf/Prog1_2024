idade1 = int(input())
idade2 = int(input())
preco1 = 0
preco2 = 0
precototal = 0

if idade1 <=17:
    preco1 = 15.0
elif idade1>=18 and idade1<=59:
    preco1 = 30.0
else:
    preco1 = 20.0

if idade2 <=17:
    preco2 = 15.0
elif idade2>=18 and idade2<=59:
    preco2 = 30.0
else:
    preco2 = 20.0

precototal = preco1+preco2

print(f'{precototal:.2f}')

