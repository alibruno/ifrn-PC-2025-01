'''
Escreva um programa que leia 2 números inteiros e informe se o maior é múltiplo do menor.

Input

A entrada é composta de dois números inteiros a eb (1 ≤ a, b ≤ 10^9), cada um em uma linha.

Output

A saída deve conter uma única linha com o texto "Multiplos" caso o maior seja múltiplo do 
menor ou "Nao multiplos" caso contrário. Observe que não há acentos no texto.
'''

a = int(input())
b = int(input())
    
if(a%b == 0 or b%a == 0):
    print("Multiplos")
else:
    print("Nao multiplos")