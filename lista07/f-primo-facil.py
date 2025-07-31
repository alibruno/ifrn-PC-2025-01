'''
Escreva um programa que leia um número natural n e informe se o mesmo é primo.
Input

A entrada é composta de uma única linha contendo um número inteiro n (1 ≤ n ≤ 10^6).
Output

Seu programa deve mostra, em uma linha, a palavra 'Sim' se o n for primo ou 'Nao' 
(observe que a palavra não está sem o til) caso contrário. 
'''

n = int(input())
is_primo = True
    
if n < 2:
    is_primo = False
else:
    for i in range (2, n+1):
        if n % i == 0 and n != i:
            is_primo = False
    
print("Sim" if is_primo else "Nao")