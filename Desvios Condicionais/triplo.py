n1 = float(input("Informe N1:"))
n2 = float(input("Informe N2:"))
n3 = float(input("Informe N3:"))
n4 = float(input("Informe N4:"))
media = (n1 + n2 + n3 + n4)/4
print(f'A média das notas é? {media:2.1f}')
if media >= 6:
    print("Aprovado(a) :)")
else:
    print("Reprovado(a) :(")


