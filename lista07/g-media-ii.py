'''
Escreva um programa que leia N números inteiros e calcule a média dos números 
lidos. Depois o programa deve mostrar quantos números estão acima da média e 
quais são, também deve mostrar quantos estação abaixo da média e quais são.

Input

A entrada é composta de 2 (duas) linhas, a primeira linha contém um inteiro 
N (1 ≤ N ≤ 10^6), a quantidade de números a serem lidos. A segunda contém N 
números inteiros Ai (0 ≤ Ai ≤ 10^9), separados por espaço.

Output

Seu programa deve imprimir deve imprimir 3 (três) linhas, onde a primeira linha 
contém um a média dos números lidos, com 1 (uma) casa decimal. A segunda linha 
contém a quantidade de números abaixo da média e a lista dos números, na ordem 
em que foram lidos, separados por espaço. Por fim, na terceira e última linha, 
a quantidade de números igual à média ou acima da média e os números, também 
separados por espaço.
'''
n = int(input())
a = list(map(int, input().split()))
soma = 0
for i in range (n):
    soma = soma + a[i]
    
media = soma/n
countNumerosAbaixoDaMedia = 0
listNumAbMedia = []
countNumerosAcimaOuIgualAMedia = 0
listNumAcIgualMedia = []
    
    
for i in range (n):
    if a[i] < media:
        countNumerosAbaixoDaMedia = countNumerosAbaixoDaMedia + 1
        listNumAbMedia.append(a[i])
    
    else:
        countNumerosAcimaOuIgualAMedia = countNumerosAcimaOuIgualAMedia + 1
        listNumAcIgualMedia.append(a[i])
    
print("{:.1f}".format(media))
print(countNumerosAbaixoDaMedia, *listNumAbMedia,)
print(countNumerosAcimaOuIgualAMedia, *listNumAcIgualMedia)