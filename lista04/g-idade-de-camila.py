'''
Cibele, Camila e Celeste são três irmãs inseparáveis. Estão sempre juntas e adoram 
fazer esportes, ler, cozinhar, jogar no computador... Agora estão aprendendo a 
programar computadores para desenvolverem seus próprios jogos.

Mas nada disso interessa para esta tarefa: estamos interessados apenas nas suas idades. 
Sabemos que Cibele nasceu antes de Camila e Celeste nasceu depois de Camila.

Dados três números inteiros indicando as idades das irmãs, escreva um programa para 
determinar a idade de Camila.

Input

A entrada é composta por três linhas, cada linha contendo um número inteiro N (5 ≤ N ≤ 100), 
a idade de uma das irmãs.

Output

Seu programa deve produzir uma única linha, contendo um único número inteiro, a idade 
de Camila.
'''

N1 = int(input())
N2 = int(input())
N3 = int(input())
 
if(N1> N2 and N1> N3):
    if(N2 > N3):
        print(N2)
    else:
        print(N3)
elif(N2> N1 and N2>N3):
    if(N1>N3):
        print(N1)
    else:
        print(N3)
else:
    if(N1 > N2):
        print(N1)
    else:
        print(N2)