def calculaValor():
    saudacao = input("Qual foi a saudação:")
    if saudacao == "olá":
        return 0
    elif saudacao[0] == 'o':
        return 20
    else:
        return 100

print(calculaValor())


