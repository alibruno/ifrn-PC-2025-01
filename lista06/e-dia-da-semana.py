'''
Escreva uma função que receba que dia da semana é hoje e em quantos dias ocorre 
um determinado evento e retorne que dia da semana é o evento.

Input

A função recebe como parâmetros uma string (texto) h, com o nome do dia semana 
(h é um dos seguintes valores: Domingo, Segunda-feira, Terca-feira, Quarta-feira, 
Quinta-feira, Sexta-feira ou Sabado) e um inteiro d (0 ≤ d ≤ 1000), onde d é a 
quantidade de dias que faltam até o evento.

Assinatura da função em Python:

def dia_da_semana(h,d)

Importante: O código que você enviar não deve mostrar nada na tela (função print()). 
Deve conter apenas a implementação da função.

Os dias da semana não possuem acento nem espaços, começam com uma letra maiúscula e 
todas as outras letras são minúsculas.

Output

A função deve retornar uma string, o nome do dia da semana de h a d dias de diferença.
'''

def dia_da_semana (h, d):
    dias_da_semana = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    entrada_indice = dias_da_semana.index(h)
    novo_indice = entrada_indice + d%7
    
    if(novo_indice < 7):
        return dias_da_semana[novo_indice]
    else:
        return dias_da_semana[novo_indice - 7]