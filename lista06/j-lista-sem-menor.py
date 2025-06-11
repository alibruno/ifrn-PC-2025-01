'''
Escreva uma função que receba uma lista e retorne uma nova lista com todos os elementos 
da lista recebida, sem o menor.

Input

A função recebe uma lista de n (1 ≤ n ≤ 10^9) números inteiros ai ( - 10^9 ≤ ai ≤ 10^9).

Assinatura da função em Python:

def sublista_sem_menor(lista)

Output

A função deve retornar uma nova lista contendo todos os elementos da lista recebida, na 
mesma ordem, sem o menor elemento da lista.
'''

def sublista_sem_menor(lista):
    lista2 = lista.copy()
    lista2.remove(min(lista))
    return lista2