'''
Supondo que a população de um país A seja da ordem de 80000 habitantes
com uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
calcule e escreva o número de anos necessários para que a população
do país A ultrapasse ou iguale
a população do país B, mantidas as taxas de crescimento.
'''

pA = 80000
pB = 200000
cA = 0.03
cB = 0.015
anos = 0
while pA < pB:
    pA = pA + (pA*cA)
    pB = pB + (pB*cB)
    anos+=1

print(f'População A: {int(pA)} \n População B: {int(pB)} \n Anos: {anos}')

