'''
Escreva um programa que leia 5 números e mostre o maior dos 5.

Input

A entrada é composta de 3 números inteiros a, b, c, d e e ( - 10000 ≤ a, b, c, d, e ≤ 10000), 
cada número em uma linha.

Output

A saída deve conter uma única linha com um número inteiro, o maior dos 5 números lidos.
'''

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
    
    
    
if(a>=b and a>=c and a>=d and a>=e):
    print(a)
elif(b>=a and b>=c and b>=d and b>=e):
    print(b)
elif(c>=a and c>=b and c>=d and c>=e):
    print(c)
elif(d>=a and d>=b and d>=c and d>=e):
    print(d)
elif(e>=a and e>=b and e>=c and e>=d):
    print(e)