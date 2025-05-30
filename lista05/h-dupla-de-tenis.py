'''
Quatro amigos combinaram de jogar tênis em duplas. Cada um dos amigos tem um nível 
de jogo, que é representado por um número inteiro: quanto maior o número, melhor o 
nível do jogador.

Os quatro amigos querem formar as duplas para iniciar o jogo. De forma a tornar o 
jogo mais interessante, eles querem que os níveis dos dois times formados sejam o 
mais próximo possível. O nível de um time é a soma dos níveis dos jogadores do time.

Embora eles sejam muito bons jogadores de tênis, os quatro amigos não são muito bons 
em algumas outras coisas, como lógica ou matemática. Você pode ajudá-los e encontrar 
a menor diferença possível entre os níveis dos times que podem ser formados?

Input

A entrada contém quatro linhas, cada linha contendo um 
inteiro A, B, C e D (0 ≤ A ≤ B ≤ C ≤ D ≤ 10^4), indicando o nível de jogo dos quatro 
amigos.

Output

Seu programa deve produzir uma única linha, contendo um único inteiro, a menor diferença 
entre os níveis dos dois times formados.
'''

A = int(input())
B = int(input())
C = int(input())
D = int(input())
    
if(((A+D) - (B+C)) > 0):
    print((A+D) - (B+C))
else:
    print((B+C) - (A+D))