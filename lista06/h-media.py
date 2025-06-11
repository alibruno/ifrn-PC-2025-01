'''
Escreva uma função que receba uma lista e retorne a média aritmética dos seus 
elementos.

Input

A função recebe uma lista com n (1 ≤ n ≤ 10^9) elementos inteiros ai (1 ≤ ai ≤ 10^9).

Assinatura da função em Python:

def media_lista(lista)

Output

A função deve retorna um valor inteiro, a média dos elementos da lista.
'''

def media_lista(lista):
    return int(sum(lista)/len(lista))