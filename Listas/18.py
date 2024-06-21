def votados(lista):
    votosUnicos = []
    for item in lista:
        if item not in votosUnicos:
            votosUnicos.append(item)
    return votosUnicos

def qtdVotos(jogador,votos):
    return votos.count(jogador)

def percentual(jogador,votos):
    return qtdVotos(jogador,votos)*100/len(votos)

print("Enquete: Quem foi o melhor jogador?")
votos = []
while True:
    voto = int(input("Número do jogador (0=fim):"))
    if voto == 0:
        break
    if voto<0 or voto>23:
        print("Informe um valor entre 1 e 23 ou 0 para sair!")
        continue
    votos.append(voto)



print("Resultado da votação")

print(f'Foram computados {len(votos)} votos')

for jogador in votados(votos):
    print(f'Jogador {jogador} - {qtdVotos(jogador,votos)} votos - {percentual(jogador,votos):.2f} %')
