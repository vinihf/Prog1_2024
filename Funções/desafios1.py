def eTriangulo(a,b,c):
    if a + b >= c and b + c >= a and a + c >= b:
        return True
    else:
        return False
def tipoTriangulo(a,b,c):
    if a == b and b == c:
        return "Equilátero"
    elif a!=b and b!=c and a!=c:
        return "Escaleno"
    else:
        return "Isóceles"

a = 3
b = 4
c = 5

if eTriangulo(a,b,c):
    print(tipoTriangulo(a,b,c))
else:
    print("Não é um triângulo.")




