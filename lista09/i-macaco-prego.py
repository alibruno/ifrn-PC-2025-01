'''
O macaco-prego é um animal irrequieto e barulhento, merecedor também dos adjetivos 
desordeiro e despudorado. A sua cabeça, encimada por uma densa pelagem negra ou 
marrom-escura, semelhante a um gorro, torna seu aspecto inconfundível. Apesar de ser 
o macaco mais comum nas matas do país, uma de suas sub-espécies encontra-se seriamente 
ameaçada de extinção: o macacoprego-do-peito-amarelo, que se distingue das demais pela 
coloração amarelada do peito e da parte anterior dos braços.

Um grande esforço foi feito pelos primatologistas para aumentar a população dos 
macacos-pregodo-peito-amarelo. Sabe-se que eles se alimentam de plantas, das quais 
consomem preferencialmente frutos e brotos. Alimentam-se também de muitos animais, 
preferencialmente lesmas, lagartas e rãs, e preferem as florestas mais densas. Para 
determinar o melhor local do país para criar uma nova reserva ambiental para os macacos-prego-do-peito-amarelo, o governo fez um levantamento das regiões no país onde 
as condições preferidas desses animais ocorrem: regiões de floresta densa, regiões com 
frutos, regiões com muitos brotos, etc. Ajude a salvar os macacos-pregodo-peito-amarelo.

As regiões propícias para o macaco-prego-do-peito-amarelo foram determinadas como 
retângulos cujos lados são todos verticais ou horizontais. Sua tarefa é encontrar o local 
ideal para a reserva ambiental, definida como a interseção de todas as regiões dadas.

As regiões foram divididas de tal forma que uma região não tangencia qualquer outra região. 
Assim, a interseção entre quaisquer duas regiões ou é um retângulo ou é vazia.

Input

Seu programa deve ler vários conjuntos de teste. A primeira linha de um conjunto de teste 
contém um inteiro não negativo, N (0 ≤ N ≤ 10000), que indica o número de regiões (o valor 
N = 0 indica o final da entrada). Seguem-se N linhas, cada uma contendo quatro números 
inteiros X, Y, U e V ( - 10000 ≤ X, Y, U, V ≤ 10000) que descrevem uma região: o par X, Y 
representa a coordenada do canto superior esquerdo e o par U, V representa a coordenada do 
canto inferior direito de um retângulo.

Output

Para cada conjunto de teste da entrada seu programa deve produzir três linhas na saída. 
A primeira linha deve conter um identificador do conjunto de teste, no formato "Teste n", 
onde n é numerado a partir de 1. A segunda linha deve conter as coordenadas do retângulo 
de interseção encontrado pelo seu programa, no mesmo formato utilizado na entrada. Caso a 
interseção seja vazia, a segunda linha deve conter a expressão "nenhum". A terceira linha 
deve ser deixada em branco. A grafia mostrada no Exemplo de Saída, abaixo, deve ser seguida 
rigorosamente. 
'''

teste = 1
while True:
    n = int(input())
    if n == 0:
        break

    todos_x = []
    todos_y = []
    todos_u = []
    todos_v = []

    for i in range(n):
        x,y,u,v = map(int, input().split())
        todos_x.append(x)
        todos_y.append(y)
        todos_u.append(u)
        todos_v.append(v)

    esquerda = max(todos_x)
    direita = min(todos_u)
    topo = min(todos_y)
    base = max(todos_v)

    print("Teste", teste)
    if esquerda<direita and base<topo:
        print(f"{esquerda} {topo} {direita} {base}")
    else:
        print("nenhum")
    print()
    teste += 1