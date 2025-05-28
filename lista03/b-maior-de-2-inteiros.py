'''
Escreva um programa que leia 2 (dois) números inteiros a e b e mostre o maior dos 2.

Input

A entrada é composta por duas linhas. A primeira linha contém apenas um inteiro 
a (1 ≤ a ≤ 10^9) e a segunda um inteiro b (1 ≤ b ≤ 10^9).

Output

Seu programa deve mostrar uma única linha contendo o valor do maior inteiro.
'''

a = int(input())
b = int(input())
    
if (a > b):
    print(a)
else:
    print(b)