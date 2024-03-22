pa = 0
pc = 0

#Jogada 1
ada = int(input())
carol = int(input())
soma = ada+carol
if soma%2==0:
    pc = pc+1
else:
    pa = pa+1

#Jogada 2
ada = int(input())
carol = int(input())
soma = ada+carol
if soma%2==0:
    pc = pc+1
else:
    pa = pa+1

#Jogada 3
ada = int(input())
carol = int(input())
soma = ada+carol
if soma%2==0:
    pc = pc+1
else:
    pa = pa+1

if pa>pc:
    print("Ada venceu!")
else:
    print("Carol venceu!")