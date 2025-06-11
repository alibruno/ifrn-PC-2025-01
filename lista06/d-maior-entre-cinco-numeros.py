'''
Escreva uma função que receba 5 (cinco) números inteiros e retorne o maior dos 
mesmos.

Input

A função recebe como parâmetros 5 (cinco) números inteiros 
a, b, c, d e e ( - 1000 ≤ a, b, c, d, e ≤ 1000).

Assinatura da função em Python:

def maior5(a, b, c, d, e)

Importante: O código que você enviar não deve mostrar nada na tela (função print()). 
Deve conter apenas a implementação da função.

Output

A função deve retornar um valor inteiro, o maior número entre a, b, c, d e e.
'''

def maior5(a, b, c, d, e):
    if a>=b and a>=c and a>=d and a>=e:
        return a
    elif b>=a and b>=c and b>=d and b>=e:
        return b
    elif c>=a and c>=b and c>=d and c>=e:
        return c
    elif d>=a and d>=b and d>=c and d>=e:
        return d
    else:
        return e