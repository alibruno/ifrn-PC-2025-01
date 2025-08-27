'''
Uma sequencia S de DNA é uma string que contém apenas os caracteres A, C, G e T. 
Sua tarefa é encontrar a repetição de maior tamanho da sequencia, ou seja, a 
substring de tamanho máximo contendo apenas um tipo de caractere.

Input

A entrada é composta de uma única linha contendo a string da sequencia de DNA de 
n (1 ≤ n ≤ 10^6) caracteres.

Output

Seu programa deve mostrar um único inteiro, que representa a quantidade de caracteres 
da repetição de maior tamanho.
'''

s = input()
charS = s[0]
count = 0
listCount = []

for i in range (len(s)):
    if charS == s[i]:
        count += 1
    else:
        listCount.append(count)
        charS = s[i]
        count = 1
    if i == len(s)-1:
        listCount.append(count)

print(max(listCount))