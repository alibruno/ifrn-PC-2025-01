'''
Escreva um programa que leia um número inteiro n e calcule o seguinte somatório:
                            1/2+1/4+...1/(n-1)+1/n
Input

A entrada é composta de uma única linha, com um valor inteiro n (1 ≤ n ≤ 10^6).

Output

O programa deve mostra uma linha com o valor do somatório com 4 casas decimais.
'''
n = int(input())
soma = 0
for i in range (1, n+1):
    soma = soma + (1/i)
print("{:.4f}".format(soma))