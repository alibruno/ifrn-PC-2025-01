'''
Escreva um programa que leia dois valores L1 e L2, que representam os 
lados de um retângulo e mostre o perímetro do mesmo.

Input

Uma única linha com dois valores inteiros L1 e L2 (1 ≤ L1, L2 ≤ 10^9).

Output

Um único inteiro com o perímetro do retângulo.
'''

L1, L2 = map(int, input().split())
rectanglePerimeter = L1*2 + L2*2
print(rectanglePerimeter)