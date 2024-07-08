def pares(lista):
    par = 0
    for n in lista:
        if n%2==0:
            par+=1
    return par

l = [1,4,6,7,8,8,2,3,4,4,5,6,7,8]
print(pares(l))