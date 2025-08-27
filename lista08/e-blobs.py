'''
No planeta Alpha vive a criatura Blobs, que come precisamente 1/2(metade) de seu
suprimento de comida disponível todos os dias. Escreva um programa que leia a 
capacidade inicial de suprimento de comida C, em Kg, e calcule quantos dias 
passarão antes que Blobs coma todo esse suprimento até restar um quilo ou menos.

Input

A primeira linha de entrada contem um único inteiro N (1 ≤ N ≤ 1000), indicando o 
número de casos de teste. As N linhas seguintes contém um valor de ponto flutuante 
C (1 ≤ C ≤ 1000) correspondente à quantidade de comida disponível para Blobs.

Output

Para cada caso de teste, imprima uma linha contendo o número de dias que Blobs irá 
demorar para comer todo seu suprimento de comida, seguido da palavra "dias".
'''

N = int(input())
dias = []
countDias = 0
for i in range (N):
    C = float(input())
    while C > 1:
        countDias += 1
        C = C/2
    dias.append(countDias)
    countDias = 0
    
for i in range (len(dias)):
    print(dias[i], "dias")