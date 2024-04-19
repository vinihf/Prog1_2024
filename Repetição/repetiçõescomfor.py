def consoantes(palavra):
    soma = 0
    for letra in palavra:
        if letra not in 'aeiou':
            soma+=1
    return soma

qtd = consoantes("python")