gremio = 0
inter = 0
fgremio =0
finter = 0
while True:
    sexo = input("Informe o sexo: Masculino (1) ou Feminino (2)")
    if sexo == 'sair':
        break
    time = input("Informe o time: Grêmio (1) ou Internacional (2)")
    if time == "1":
        gremio+=1
    elif time == "2":
        inter+=1
    if sexo == "2":
        if time == "1":
            fgremio += 1
        elif time == "2":
            finter += 1

print(f'Por time: Grêmio({gremio}) x Inter({inter})')
print(f'Torcedoras: Grêmio({fgremio}) x Inter({finter})')
