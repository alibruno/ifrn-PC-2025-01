'''
Um determinado material radioativo perde metade de sua massa a cada s segundos.
Escreva um programa que leia o tempo s de perda de massa e a massa inicial mi, 
em gramas, de um material. O programa deve então calcular em quanto tempo a massa 
do material fica menor do que 0, 5 grama. O programa deve mostrar a massa final, 
com 3 casas decimais em uma linha e o tempo gasto para o material chegar a essa 
massa. O tempo deve ser mostrado na forma D dias HH:MM:SS.

Input

A entrada é composta de 1 linha contendo 2 (dois) números inteiros s (1 ≤ s ≤ 10^9), 
o tempo, em segundos, que a massa do material cai pela metadee mi, a massa inicial 
do material radioativo.

Output

Seu programa deve mostrar uma única linha, com o tempo gasto em forma de horas, 
minutos, segundos e milissegundos: D dias HH:MM:SS. 
'''

s, mi = map(int, input().split())
count = 0
    
while (mi>=0.5):
    mi = mi/2
    count += 1
    
tempoGastoSeg = s*count
tempoGastoMin = 0
tempoGastoHoras = 0
tempoGastoDias = 0
    
if tempoGastoSeg > 60:
    tempoGastoMin = tempoGastoSeg//60
    tempoGastoSeg = tempoGastoSeg%60
if tempoGastoMin > 60:
    tempoGastoHoras = tempoGastoMin//60
    tempoGastoMin = tempoGastoMin%60
if tempoGastoHoras > 24:
    tempoGastoDias = tempoGastoHoras//24
    tempoGastoHoras %= 24
    
print(f"{tempoGastoDias} dias {tempoGastoHoras:02d}:{tempoGastoMin:02d}:{tempoGastoSeg:02d}")