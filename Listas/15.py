def quantidade(l):
    return len(l)

def naOrdem(l):
    for e in l:
        print(e,end=" ")
    print()

def inverso(l):
    for i in range(len(l)-1,-1,-1):
        print(l[i])
    '''
    for i in l[::-1]:
            print(i)
    
    for e in reversed(l):
        print(e)
    '''
def soma(l):
    total = 0
    for e in l:
        total+=e
    return total

def media(l):
    return soma(l)/quantidade(l)

def maiorMedia(l):
    qtdMaior = 0
    for n in l:
        if n > media(l):
            qtdMaior+=1
            #qtdMaior = qtdMaior+1
    return qtdMaior

def menorSete(l):
    qtdMenor = 0
    for n in l:
        if n < 7:
            qtdMenor+=1
            #qtdMenor = qtdMenor+1
    return qtdMenor

lista = []
while True:
    nota = float(input("Informe uma nota:"))
    if nota == -1:
        break
    lista.append(nota)

print(quantidade(lista))
naOrdem(lista)
inverso(lista)
print(lista)








