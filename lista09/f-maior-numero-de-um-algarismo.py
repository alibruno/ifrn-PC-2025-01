'''
Os habitantes do planeta Uno possuem um terrível problema de detecção de números com 
mais de um algarismo, de modo que, para tudo que vão fazer, transformam qualquer valor 
inteiro em um número de um algarismo, realizando somas sucessivas do número até o mesmo 
ser reduzido a um algarismo. Por exemplo, o número 999999999991, no planeta Uno, soma-se 
todos os algarismos, resultando em 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 9 + 1 = 100. 
Como o número 100 tem mais de um algarismo, o processo se repete, resultando em 
1 + 0 + 0 = 1.

Uma das grandes dificuldades que os habitantes possuem está em comparar dois números e 
verificar qual deles é o maior, segundo as regras do planeta.

Escreva um programa que, dados dois números inteiros, identifique qual deles é o maior 
número de um algarismo.

Input

Haverá diversos casos de teste. Cada caso de teste inicia com dois inteiros N e 
M (0 ≤ N ≤ 10^100, 0 ≤ M ≤ 10^100), indicando os dois números a serem comparados.

O último caso de teste é indicado quando N = M = 0, sendo que este caso não deverá ser 
processado. É garantido que não haverá mais do que 100 casos de teste em cada exemplo.

Output

Para cada caso de teste, imprima uma linha, contendo um inteiro, indicando 1 se o primeiro 
número for o maior de um algarismo, 2 se o segundo número for o maior de um algarismo ou 0 
se ambos os números possuírem o mesmo valor de um algarismo.
'''

def somaAlgarismosUno(n):
    while (n > 9):
        soma = 0
        while(True):
            if n//10 == 0:
                soma += n 
                break
            else:
                soma += (n%10) 
                n = ((n - n%10)//10)
        n = soma
    return n


while (True):
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    if somaAlgarismosUno(n) == somaAlgarismosUno(m):
        print('0')
    elif somaAlgarismosUno(n) > somaAlgarismosUno(m):
        print('1')
    else:
        print('2')