'''
Para se preparar para os outros problemas, vamos fazer um teste. Dado um número X, 
retorne o menor número par maior do que X.

Input

Uma linha contendo um número x (0 < x < 10^7).

Output

Uma linha contendo a resposta do problema.
'''

x = int(input())
    
if (x%2 == 0):
    print(x+2)
else: 
    print(x+1)

