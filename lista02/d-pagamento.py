'''
Escreva um programa que leia o valor de um item a venda, a quantidade 
de itens que você vai comprar e o valor que você tem para pagar. Todos 
os valores são inteiros. O programa deve então informar o valor total 
a ser pago e o valor do troco que você vai receber.

Input

A entrada é composta de 3 linhas, cada uma com um número inteiro. 
A primeira linha contém o valor do item V (1 ≤ V ≤ 10^5). 
A segunda linha contém a quantidade de itens comprado Q (1 ≤ Q ≤ 10^3). 
A terceira linha contém o valor total pago T (1 ≤ T ≤ 10^8).

Output

Seu programa deve mostrar 2 linhas. A primeira com o valor total dos 
itens comprado, no format 'A pagar: 84' e a segunda com o troco a ser 
devolvido no formato 'Troco : 16'.
'''

V = int(input())
Q = int(input())
T = int(input())
    
print("A pagar:", (V*Q))
print("Troco  :", (T - (V*Q)))