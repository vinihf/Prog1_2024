aux = ['ping','pong']
indice = 0
for i in (range(64,546)):
    if i % 2 == 0:
        print(aux[indice])
        if indice == 1:
            indice = 0
        else:
            indice = 1
    else:
        print(i)



