'''
Escreva uma função que receba uma lista e troque de lugar o menor elemento com o 
primeiro elemento da lista.

Input

A função recebe uma lista de n (1 ≤ n ≤ 10^9) números inteiros ai ( - 10^9 ≤ ai ≤ 10^9).

Assinatura da função em Python:

def lista_troca_menor_primeiro(lista)
Output

A função deve retornar um inteiro, com a quantidade total de trocas realizadas, ou seja, 
0 se não houve troca ou 1 se houve troca.
'''

def lista_troca_menor_primeiro(lista):
    indice_menor_elem = lista.index(min(lista))
    if indice_menor_elem == 0:
        return 0
    else:
        menor_elemento = min(lista)
        elemento_indice_zero = lista[0]
        lista.remove(menor_elemento)
        lista.insert(0, menor_elemento)
        lista.remove(lista[1])
        lista.insert(indice_menor_elem, elemento_indice_zero)
        return 1