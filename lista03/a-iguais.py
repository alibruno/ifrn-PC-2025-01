'''
Escreva um programa que leia dois números inteiros a e b e escreva se eles são iguais.

Input

A entrada é composta de duas linhas, a primeira linha contém o número inteiro 
a ( - 10^9 ≤ a ≤ 10^9) e a segunda contém um inteiro b ( - 10^9 ≤ b ≤ 10^9).

Output

Seu programa deve escrever uma única linha contendo o texo 'Sim' caso os números 
sejam iguais ou 'Nao', SEM ACENTO, caso os números não sejam iguais. 
'''

a = int(input())
b = int(input())
    
if (a == b):
    print("Sim")
else:
    print("Nao")