'''
Escreva um programa que leia dois números inteiros a e b e mostre todos os 
múltiplos de a menores ou iguais a b.

Input

Uma única linha com 2 números inteiros a e b (1 ≤ a ≤ b ≤ 10^6) separados por 
um espaço.

Output

Uma única linha com os múltiplos de a, separados por espaço.
'''
a, b = map(int, input().split())
multiplos = str(a)
    
for i in range (2, b+1):
    if a*i > b:
        break
    multiplos = multiplos + " " + str(a*i) 
    
print(multiplos)