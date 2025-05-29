'''
Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que 
precisam formar vários triângulos, numa cartolina, com algumas varetas de 
comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos 
com três varetas de comprimentos quaisquer: se uma das varetas for muito grande 
em relação às outras duas, não dá para formar o triângulo.

Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os 
comprimentos de quatro varetas, é ou não é possível selecionar três varetas, 
dentre as quatro, e formar um triângulo.

Input

A entrada é composta por apenas uma linha contendo quatro números inteiros 
A, B, C e D (1 ≤ A, B, C, D ≤ 100).

Output

Seu programa deve produzir apenas uma linha contendo apenas um caractere, que 
deve ser 'S' caso seja possível formar o triângulo, ou 'N' caso não seja possível 
formar o triângulo.
'''

A, B, C, D = map(int, input().split())
# TRIANGULOS ABC, ABD, ACD, BDC
if ((A+B>C and A+C>B and B+C>A) or (A+B>D and A+D>B and B+D>A) or (A+C>D and A+D>C and C+D>A) or (B+C>D and B+D>C and C+D>B)):
    print('S')
else:
    print('N')