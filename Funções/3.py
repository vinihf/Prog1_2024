def mediaFinal(n1,n2):
    final = (n1+n2)/2
    return final

nota1 = 9.5
nota2 = 5.5

media = mediaFinal(nota1,nota2)
print(f'A média desta avaliação foi {media}')

if mediaFinal(nota1,nota2) >=6:
    print("Aprovado")
else:
    print("Reprovado")

