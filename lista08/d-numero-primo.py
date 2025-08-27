'''
Dado um número inteiro n, encontre o menor número primo maior do que n.

Input

A entrada é composta de uma única linha, contendo um número inteiro n (1 ≤ n ≤ 10^6).

Output

Seu programa deve mostrar um número inteiro p, que é o menor número primo maior do 
que n.
'''

def primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range (2, n):
        if n % i == 0:
            return False
    return True 
        
    
N = int(input())
        
isPrimo = False
count = 0
    
while (isPrimo == False):
    count += 1
    isPrimo = primo(N + count)
    
print(N+count)