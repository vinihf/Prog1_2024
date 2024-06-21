'''
def piramide(n):
    for i in range(0,n+1):
            #print(i * "*")
        texto = " "
        for x in range(0,i):
            texto+="*"
        print(texto)

piramide(4)
'''

def piramide(n):
    #x = 1
    #while x < n+1:
    for x in range(1,n+1):
        linha = ""
        for y in range(0,x):
            linha +="*"
        print(linha)
        #x+=1
piramide(4)



