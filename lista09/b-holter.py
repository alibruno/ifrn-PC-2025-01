'''
Professor Edu sentiu-se mal no último final de semana e precisou ir ao hospital.
Durante o atendimento foi observado que ele apresentou um quadro de arritmia 
cardíaca e foi encaminhado para um médico cardiologista. Um dos exames solicitados
pelo médico utiliza um monitor Holter, equipamento que monitora o coração durante 
um determinado período, em geral, 24 horas.

No exame realizado por Edu, foram registrados os batimentos cardíacos a cada 
30 minutos. E, como ele é muito ansioso, decidiu verificar os registros dos seus 
batimentos e anotar algumas informações para a conversa a ser realizada com seu 
cardiologista na próxima consulta médica.

Edu decidiu verificar basicamente duas informações: a quantidade média de batimentos 
cardíacos no exame realizado e a quantidade de medições com batimentos acima ou 
abaixo da média obtida considerando uma diferença de 10% entre cada valor medido e a 
média.

Input

A primeira linha da entrada contém um inteiro N (2 ≤ N ≤ 48) com o número de medições 
realizadas pelo equipamento. As N linhas seguintes possuem valores inteiros 
B (50 ≤ B ≤ 150) referentes às medições dos batimentos cardíacos.
Output

A saída deve conter dois valores inteiros: na primeira linha, o batimento médio obtido
a partir das medições realizadas, e na segunda linha, a quantidade de medições acima 
ou abaixo deste valor médio considerando uma diferença de 10% entre os valores medidos 
e a média.
'''

N = int(input())
lista = []
media = 0
countForaDaMedia = 0
 
for i in range (N):
    B = int(input())
    lista.append(B)
    media += B
 
media //= len(lista)

 
for i in range (N):
    if lista[i] > int(media*1.1) or lista[i] < int(media*0.9):
        countForaDaMedia += 1
        
print(int(media))
print(countForaDaMedia)
