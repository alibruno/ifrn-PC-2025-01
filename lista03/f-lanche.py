'''
Com base na tabela abaixo, escreva um programa que leia o código de um item e 
a quantidade deste item. A seguir, calcule e mostre o valor da conta a pagar.

Código	    Produto          Preço
1	    Cachorro-quente	    R$ 4,00
2	    X-salada	        R$ 4,50
3	    X-Bacon	            R$ 5,00
4	    Torrada simples	    R$ 2,00
5	    Refrigerante	    R$ 1,50

Input

A entrada contém dois valores inteiros c (1 ≤ c ≤ 5) e q (1 ≤ q ≤ 100), 
correspondentes ao código e à quantidade de um item conforme tabela acima.

Output

A saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, 
com 2 casas após o ponto decimal.
'''

c, q = map(int, input().split())
float(q)
if(c == 1):
    print("Total: R$ {:.2f}".format(4*q))
elif(c == 2):
    print("Total: R$ {:.2f}".format(4.5*q))
elif(c == 3):
    print("Total: R$ {:.2f}".format(5*q))
elif(c == 4):
    print("Total: R$ {:.2f}".format(2*q))
elif(c == 5):
    print("Total: R$ {:.2f}".format(1.5*q))