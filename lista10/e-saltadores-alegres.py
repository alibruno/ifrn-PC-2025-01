'''
Uma sequencia de n números inteiros é chamada de Saltadora alegre se a diferença 
entre todos os pares consecutivos formam a sequencia dos números entre 1 e n - 1, 
inclusive.

Por exemplo: a sequencia de números [1, 4, 2, 3] é uma sequencia saltadora alegre, 
já que temos todos os números entre 1 e 3 formados entre a diferença absoluta entre 
pares consecutivos: , e .

Input

A entrada é composta de várias linhas, terminando com EOF. Cada linha começa com um 
número inteiro n (1 ≤ n ≤ 10000) seguido de n inteiros ai ( - 10^8 ≤ ai ≤ 10^8).
Output

Para cada linha da entrada seu programa deve imprimir 'Alegre' ou 'Nao alegre' (sem acentos). 
'''

def modulo(n):
    if n >= 0:
        return n
    return -n

isAlegre = True
while True:
    try: 
        listaDeInteiros = list(map(int, input().split()))
        del listaDeInteiros[0]

        if len(listaDeInteiros) != 1:

            listaSumParesConseq = []
            for i in range (len(listaDeInteiros)-1):
                listaSumParesConseq.append(modulo(listaDeInteiros[i] - listaDeInteiros[i+1]))
            listaSumParesConseq.sort()

            for i in range (len(listaSumParesConseq)):
                if listaSumParesConseq[i] != i+1:
                    isAlegre = False
                    break

            if listaSumParesConseq[-1] != len(listaDeInteiros) - 1 :
                isAlegre = False

        print('Alegre' if isAlegre else 'Nao alegre')
        isAlegre = True
    except EOFError:
        break
