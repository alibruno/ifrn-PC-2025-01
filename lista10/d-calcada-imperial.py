'''
Na calçada em frente ao Palácio Imperial, não se sabe a razão, existe uma sequência de 
N números desenhados no chão. A sequência é composta apenas pelos números de 1 a N. 
Veja um exemplo na coluna (a) da figura, para N = 12.

Ninguém sabe o significado da sequência e, justamente por isso, várias teorias malucas 
surgiram. Uma delas diz que a sequência representa, na verdade, apenas um valor que 
estaria relacionado a um grande segredo dos imperadores. Esse valor é a quantidade máxima 
de números da sequência que poderiam ser marcados com um círculo, de modo que a sequência 
de números marcados não contenha dois números iguais consecutivos e seja composta de no 
máximo dois números distintos. A coluna (b) da figura ilustra uma sequência de 4 números 
marcados que obedece a restrição acima. Você consegue verificar que essa é, de fato, a 
quantidade máxima possível de números numa sequência marcada?

Neste problema, dada a sequência original de números desenhados no chão da calçada, seu 
programa deve computar e imprimir a quantidade máxima de números da sequência que poderiam 
ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência 
marcada e tal que ela seja composta de no máximo dois números distintos.

Input

A primeira linha da entrada contém um inteiro N (1 ≤ N ≤ 500) representando o tamanho da 
sequência. As N linhas seguintes contêm, cada uma, um inteiro Vi (1 ≤ Vi ≤ N), para 1 ≤ i ≤ N, 
definindo a sequência de números desenhados no chão da calçada imperial.

Output

Seu programa deve imprimir uma linha contendo um número inteiro representando a quantidade máxima 
de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais 
consecutivos na sequência marcada e tal que ela seja composta de no máximo dois números distintos.
'''

n = int(input())
v = []
for i in range(n):
    v.append(int(input()))

maiorContagem = 1

for i in range(n):
    for j in range (i+1, n):
        if v[i] == v[j]:
            continue
        n1 = v[i]
        n2 = v[j]
        count = 2
        for k in range(j+1, n):
            if v[k] != n1:
                continue
            count += 1
            n1, n2 = n2, n1
        if count > maiorContagem:
            maiorContagem = count

print(maiorContagem)