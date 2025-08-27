'''
Neste problemas iremos lidar com sequências de caracteres, muitas vezes chamadas 
de strings. Uma sequência é não-trivial se ela possui ao menos dois elementos.

Dada uma sequência s, dizemos que um trecho si, ... , sj é monótono se todos seus 
caracteres são iguais, e dizemos que ela é maximal se este trecho não pode ser 
estendido à esquerda e nem à direita sem perder a monotonicidade.

Dada uma sequência composta apenas por caracteres "a" e "b", determine quantos 
caracteres "a" ocorrem em trechos monótonos maximais não-triviais.

Input

A entrada é composta por duas linhas. A primeira linha contém um único inteiro N, 
satisfazendo 1 ≤ N ≤ 10^5. A segunda linha contém uma string, com exatamente N 
caracteres, composta apenas pelos caracteres "a" e "b".

Output

A saída é composta por uma única linha contendo um inteiro correspondente à quantidade 
total de vezes que o caractere "a" ocorre em trechos monótonos maximais não-triviais.
'''

n = int(input())
listSeqS = list(input())
countAemTrechosMonotonos = 0
    
for i in range (len(listSeqS)-1):
    if listSeqS[i] == 'a' and listSeqS[i+1] == 'a':
        if i != 0 and listSeqS[i-1] == 'a' and listSeqS[i] == 'a':
            countAemTrechosMonotonos += 1
            continue
        countAemTrechosMonotonos += 2
        
print(countAemTrechosMonotonos)