'''
O Professor Assis fez uma prova com o valor máximo da nota sendo N e 
ele quer normalizar para colocar no sistema do IFRN, que aceita notas de 0 a 100, 
sendo a nota, obrigatoriamente, um número inteiro. 
Dado N, a nota máxima que pode ser obtida na prova, e a nota X do aluno, 
mostrar ela normalizada para o sistema do IFRN.

Input

A entrada consiste de apenas uma linha que contém 
dois números reais N (1.00 ≤ N ≤ 100000.00) e X (0.00 ≤ X ≤ N), 
indicando, respectivamente, a nota máxima determinada pelo professor e 
a nota que aluno obteve na avaliação.

Output

Seu programa deve produzir uma única linha com um número inteiro representando a 
nota do aluno normalizada para as normas do IFRN.
'''

N, X = map(float, input().split())
    
if N/100 < 1:
    FatorMultip = 100/N
    N = N*FatorMultip
    X = X*FatorMultip
elif (N/100 > 1) and (N/100 < 10):
    N = N/(N/100)
    X = X/(N/100)
else:
    FatorMultip = N/100
    N = N/FatorMultip
    X = X/FatorMultip
    
    
print(int(X))