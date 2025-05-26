'''
Você foi contactado para escrever um programa que calcule a média ponderada 
entre dois números inteiros v1 e v2. A média ponderada mp é calculada 
através da fórmula a seguir:
mp = (v1*p1 + v2*p2)/(p1+p2)
onde p1 é o peso de v1 e p2 é o peso de v2.

Input

A entrada e composta de duas linhas. 
A primeira linha contém 2 (dois) números inteiros v1 e v2 (1 ≤  v1, v2 ≤ 10^9), 
separados por um espaço. 
A segunda linha contém também dois números inteiros p1 e p2 (1 ≤  v1, v2 ≤ 10^3), 
também separados por um espaço.

Output

A saída deve ter apenas um número inteiro com o valor da média ponderada, 
desprezando-se as casas decimais.
'''

v1, v2 = map(float, input().split())
p1, p2 = map(float, input().split())
weightedMean = (v1*p1 + v2*p2)/(p1+p2)
print(int(weightedMean))