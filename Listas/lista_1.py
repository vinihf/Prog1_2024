lista = [5,1,5,10,8,7,5,5,6,3]
tamanho = len(lista)
maior5 = 0
media = 0
somatorio = 0
for indice in range(0,tamanho):
    if lista[indice] > 5:
        maior5+=1
    somatorio+=lista[indice]
media = sum(lista)/len(lista)
print(f'A média de valores é {media:4.2f} e {maior5} são maiores do que 5.')