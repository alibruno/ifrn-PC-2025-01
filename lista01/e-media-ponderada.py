'''
Escreva um programa para calcular a média de uma disciplina que possui duas notas, 
com pesos 2 e 3 respectivamente, considerando as notas valores inteiros entre 0 (zero) 
e 100 (cem), inclusive.

Input

A entrada contém uma única linha com um dois números inteiro a e b (0 ≤ a, b ≤ 100) 
separados por um espaço, representando as notas da disciplina.

Output

A saída contém uma única linha com um número inteiro, mostrando a média da disciplina.
'''

num1, num2 = map(float, input().split())
weightedMean = (num1*2 + num2*3)/5
print(int(weightedMean))