# IFRN - Programação de Computadores

## Resolução em Python dos exercícios da disciplina "Programação de Computadores" - Codeforces.

## Conteúdo
1. [Enunciados](#enunciados)
      1. [Lista 01](#lista-01)
      2. [Lista 02](#lista-02)
      3. [Lista 03](#lista-03)
      4. [Lista 04](#lista-04)
## Enunciados
### Lista 01
#### [a-soma-simples](lista01/a-soma-simples.py)

Escreva um programa que leia dois números inteiros a e b e mostre a soma dos mesmos.

Input

    A entrada contém duas linhas, cada uma contendo um número inteiro, 
    a e b ( - 1000 ≤ a, b ≤ 1000).

Output

    A saída deve conter uma única linha o resultado da soma a + b.

#### [b-produto-simples](lista01/b-produto-simples.py)

Escreva um programa que leia 2 (dois) números inteiros e 
mostre o produto dos mesmos.

Input

    A entrada contém duas linhas, cada uma contendo um número inteiro, 
    a e b ( - 100000 ≤ a, b ≤ 100000).

Output

    A saída deve conter uma única linha o resultado do produto a × b.

#### [c-area-do-circulo](lista01/c-area-do-circulo.py)

A fórmula para calcular a área de uma circunferência é: 
area = π × raio^2 Considerando para este problema que π = 3.14159:
- Efetue o cálculo da área, elevando o valor de raio ao quadrado e 
multiplicando por π.

Input

    A entrada contém um valor de ponto flutuante de precisão dupla.

Output

    Apresentar a mensagem "A=" seguido pelo valor calculado da área, 
    conforme exemplo, com 4 casas após o ponto decimal. Utilize variáveis 
    de dupla precisão (double). Como todos os problemas, não esqueça 
    de imprimir o fim de linha após o resultado, caso contrário, 
    você receberá "Presentation Error".

#### [d-media-aritmetica](lista01/d-media-aritmetica.py)

Escreva um programa que leia dois números reais a e b 
e mostre a média entre os dois.

Input

    A entrada é composta de duas linhas. 
    Cada uma das linhas contém um número real de precisão dupla.

Output

    Seu programa deve mostrar a média aritmética entre valores lidos 
    e deve conter exatamente 5 (cinco) casas decimais.

#### [e-media-ponderada](lista01/e-media-ponderada.py)

Escreva um programa para calcular a média de uma disciplina 
que possui duas notas, com pesos 2 e 3 respectivamente, considerando 
as notas valores inteiros entre 0 (zero) e 100 (cem), inclusive.

Input

    A entrada contém uma única linha com um dois números inteiro a e b (0 ≤ a, b ≤ 100) 
    separados por um espaço, representando as notas da disciplina.

Output

    A saída contém uma única linha com um número inteiro, mostrando a média da disciplina.

#### [f-media-ponderada-2](lista01/f-media-ponderada-2.py)

Você foi contactado para escrever um programa que calcule a média ponderada 
entre dois números inteiros v1 e v2. A média ponderada mp é calculada 
através da fórmula a seguir:
mp = (v1*p1 + v2*p2)/(p1+p2)
onde p1 é o peso de v1 e p2 é o peso de v2.

Input

    A entrada e composta de duas linhas. 
    A primeira linha contém 2 (dois) números inteiros v1 e v2 (1 ≤  v1, v2 ≤ 109), 
    separados por um espaço. 
    A segunda linha contém também dois números inteiros p1 e p2 (1 ≤  v1, v2 ≤ 103), 
    também separados por um espaço.

Output

    A saída deve ter apenas um número inteiro com o valor da média ponderada, 
    desprezando-se as casas decimais.

#### [g-pneu](lista01/g-pneu.py)

Calibrar os pneus do carro deve ser uma tarefa cotidiana de todos os motoristas. 
Para isto, os postos de gasolina possuem uma bomba de ar. 
A maioria das bombas atuais são eletrônicas, 
permitindo que o motorista indique a pressão desejada num teclado. 
Ao ser ligada ao pneu, a bomba primeiro lê a pressão atual e 
calcula a diferença de pressão entre a desejada e a lida. 
Com esta diferença ela esvazia ou enche o pneu para chegar na pressão correta.

Sua ajuda foi requisitada para desenvolver 
o programa da próxima bomba da SBC - Sistemas de Bombas Computadorizadas.

Escreva um programa que, dada a pressão desejada digitada pelo motorista 
e a pressão do pneu lida pela bomba, 
indica a diferença entre a pressão desejada e a pressão lida.

Input

    A primeira linha da entrada contém um inteiro N que indica a pressão desejada 
    pelo motorista (1 ≤ N ≤ 40). 
    A segunda linha contém um inteiro M que indica a pressão lida pela bomba (1 ≤ M ≤ 40).

Output

    Seu programa deve imprimir uma única linha, 
    contendo a diferença entre a pressão desejada e a pressão lida.

#### [h-cachorros-quentes](lista01/h-cachorros-quentes.py)

Em 2012 foi alcançado um novo recorde mundial na famosa 
Competição de Cachorros-Quentes do Nathan: o campeão, Joey Chestnut, 
devorou 68 cachorros-quentes em dez minutos, 
um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

O restaurante Nathan's Famous Corporation, 
localizado no Brooklyn, NY, é o responsável pela competição. 
Eles produzem deliciosos cachorros-quentes, mundialmente famosos, 
mas quando o assunto é matemática eles não são tão bons. 
Eles desejam ser listados no Livro de Recordes do Guinness, 
mas para isso devem preencher um formulário descrevendo 
os fatos básicos da competição. Em particular, eles devem informar 
o número médio de cachorros-quentes consumidos pelos participantes 
durante a competição.

Você pode ajudá-los? Eles prometeram pagá-lo com um dos seus saborosos
cachorros-quentes. Dados o número total de cachorros-quentes consumidos e
o número total de participantes na competição, 
você deve escrever um programa para determinar 
o número médio de cachorros-quentes consumidos pelos participantes.

Input

    A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) 
    indicando respectivamente o número total de cachorros-quentes consumidos 
    e o número total de participantes na competição.

Output

    Seu programa deve produzir uma única linha com um número racional representando o 
    número médio de cachorros-quentes consumidos pelos participantes. 
    O resultado deve ser escrito como um número racional com exatamente 
    dois dígitos após o ponto decimal, arredondado se necessário.

#### [i-perimetro-do-retangulo](lista01/i-perimetro-do-retangulo.py)

Escreva um programa que leia dois valores L1 e L2, 
que representam os lados de um retângulo e mostre o perímetro do mesmo.

Input

    Uma única linha com dois valores inteiros L1 e L2 (1 ≤ L1, L2 ≤ 109).

Output

    Um único inteiro com o perímetro do retângulo.

#### [j-cedulas](lista01/j-cedulas.py)

Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) 
no qual o valor pode ser decomposto. 
As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. 
A seguir mostre o valor lido e a relação de notas necessárias.

Input

    O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Output

    Imprima o valor lido e, em seguida, 
    a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. 
    Não esqueça de imprimir o fim de linha após cada linha, caso contrário 
    seu programa apresentará a mensagem: "Presentation Error".
