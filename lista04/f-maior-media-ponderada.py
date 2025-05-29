'''
Ao entrar na faculdade Eduzinho se deparou com um professor que fazia a avaliação 
de forma um pouco diferente dos tradicionais. O semestre na universidade de Eduzinho 
é dividido em exatamente 2 etapas e1 e e2, cada uma com um peso diferente p1 e p2. 
Dessa forma o cálculo da média m é feito pela fórmula

                    m = (e1*p1+e2*p2)//(p1+p2)

Todos os valores usados na universidade de Eduzinho, tanto das notas como das médias, 
são números inteiros.

O professor Faísca, para permitir uma flexibilidade maior aos alunos realiza, em cada 
etapa, 2 avaliações, sendo a11 e a12 as duas avaliações da primeira etapa e a21 e a22 
as duas avaliações da segunda etapa. Assim o professor Faísca permite que o aluno 
escolha qual média será usada entre 2 (duas) possível médias. A primeira média possível, 
m1 ser usada é a utilização da avaliação 1 em cada uma das etapas, sendo calculada pela 
fórmula

                    m1 = (a11*p1+a21*p2)//(p1+p2)

A segunda média, m2 é calculada usando a avaliação 2 em cada uma das etapas, pela fórmula

                    m2 = (a12*p1+a22*p2)//(p1+p2)

Como Eduzinho não gosta de fazer contas e o professor Faísca usa a avaliação de acordo com 
a escolha do aluno, ele pediu sua ajudar para decidir se diz ao professor Faísca para usar 
a avaliação 1 ou a avaliação 2. Caso as médias sejam iguais Eduzinho vai sempre escolher a 
primeira média, m1.

Input

A entrada é composta de 3 (três) linhas. A primeira linha contém dois números inteiros a11 e 
a21 (0 ≤ a11, a21 ≤ 10^8), que são as notas da avaliação 1 para as etapas 1 e 2, respectivamente. 
A segunda linha possui dois inteiros a12 e a22 (0 ≤ a12, a22 ≤ 10^8), que são as notas da 
avaliação 2 pas etapas 1 e 2, respectivamente. A terceira linha contém 2 (dois) números inteiros 
p1 e p2 (1 ≤ p1, p2 ≤ 10^3), os pesos das etapas 1 e 2, respectivamente.

Output

Seu programa deve mostrar uma única linha com um número inteiro a informando qual avaliação 
Eduzinho vai pedir ao professor Faísca para usar. Todos os cálculos devem ser feitos utilizando 
valores inteiros, desprezando-se as casas decimais.
'''

a11, a21 = map(int, input().split())
a12, a22 = map(int, input().split())
p1, p2 = map(int, input().split())
    
if((a11*p1+a21*p2)//(p1+p2) >= (a12*p1+a22*p2)//(p1+p2)):
    a = 1
    print(a)
else:
    a = 2
    print(a)