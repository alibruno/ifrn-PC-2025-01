'''
A empresa local de abastecimento de água, a Saneamento Básico da Cidade (SBC), está 
promovendo uma campanha de conservação de água, distribuindo cartilhas e promovendo 
ações demonstrando a importância da água para a vida e para o meio ambiente.

Para incentivar mais ainda a economia de água, a SBC alterou os preços de seu fornecimento 
de forma que, proporcionalmente, aqueles clientes que consumirem menos água paguem menos 
pelo metro cúbico. Todo cliente paga mensalmente uma assinatura de R$ 7, que inclui uma 
franquia de 10m^3 de água. Isto é, para qualquer consumo entre 0 e 10m^3, o consumidor paga 
a mesma quantia de R$ 7 reais (note que o valor da assinatura deve ser pago mesmo que o 
consumidor não tenha consumido água). Acima de 10m^3, cada metro cúbico subsequente tem um 
valor diferente, dependendo da faixa de consumo. A SBC cobra apenas por quantidades inteiras 
de metros cúbicos consumidos. A tabela abaixo especifica o preço por metro cúbico para cada 
faixa de consumo:

                            Faixa de consumo (m^3)	    Preço (por m^3)
                                até 10	                incluído na franquia
                                11 a 30	                     R$ 1
                                31 a 100	                 R$ 2
                                101 em diante	             R$ 5

Assim, por exemplo, se o consumo foi de 120m^3, o valor da conta é:

    7 reais da assinatura básica;
    20 reais pelo consumo no intervalo 11 – 30m^3;
    140 reais pelo consumo no intervalo 31 – 100m^3;
    100 reais pelo consumo no intervalo 101 – 120m^3. 

Logo o valor total da conta de água é R$ 267.

Escreva um programa que, dado o consumo de uma residência em m^3, calcula o valor da conta 
de água daquela residência.

Input

A única linha da entrada contém um único inteiro N (0 ≤ N ≤ 10^3), indicando o consumo de 
água da residência, em m^3.

Output

Seu programa deve imprimir uma única linha, contendo o valor da conta de água daquela residência
'''

N = int(input())
    
if(N <= 10):
    print(7)
elif(N >= 11 and N <= 30):
    print((N - 10) * 1 + 7)
elif(N >= 31 and N <= 100):
    print((N - 30) * 2 + 20 + 7)
else:
    print((N - 100) * 5 + 140 + 20 + 7)