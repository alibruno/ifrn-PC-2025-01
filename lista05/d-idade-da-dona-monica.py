'''
Dona Mônica é mãe de três filhos que têm idades diferentes. Ela notou que, neste ano, a 
soma das idades dos seus três filhos é igual à idade dela. Neste problema, dada a idade 
de dona Mônica e as idades de dois dos filhos, seu programa deve computar e imprimir a 
idade do filho mais velho. Por exemplo, se sabemos que dona Mônica tem 52 anos e as idades 
conhecidas de dois dos filhos são 14 e 18 anos, então a idade do outro filho, que não era 
conhecida, tem que ser 20 anos, pois a soma das três idades tem que ser 52. Portanto, a 
idade do filho mais velho é 20. Em mais um exemplo, se dona Mônica tem 47 anos e as idades 
de dois dos filhos são 21 e 9 anos, então o outro filho tem que ter 17 anos e, portanto, a 
idade do filho mais velho é 21.

Input

A primeira linha da entrada contém um inteiro M (40 ≤ M ≤ 110) representando a idade de dona 
Mônica. A segunda linha da entrada contém um inteiro A (1 ≤ A ≤ M) representando a idade de um 
dos filhos. A terceira linha da entrada contém um inteiro B (1 ≤ B ≤ M) representando a idade 
de outro filho (A ≠ B) .

Output

Seu programa deve imprimir uma linha, contendo um número inteiro, representando a idade do filho 
mais velho de dona Mônica.
'''

M = int(input())
A = int(input())
B = int(input())
    
if((M-(A+B)) >= A and (M-(A+B)) >= B):
    print((M-(A+B)))
elif(A > B):
    print(A)
else:
    print(B)