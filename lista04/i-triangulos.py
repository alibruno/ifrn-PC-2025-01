'''
Caio estava brincando de construir triângulos com palitos de diferentes tamanhos. Ele 
fazia isso juntando as pontas de três palitos sobre uma mesa. Ele notou que podia agrupar 
os triângulos formados em três grupos:

Triângulos acutângulos, que são aqueles em que todos os ângulos internos medem menos de 90°; 
Triângulos retângulos, que são aqueles que possuem um ângulo interno que mede exatamente 90°; 
Triângulos obtusângulos, que são aqueles que possuem um ângulo interno que mede mais de 90°. 
Ele também percebeu que nem sempre é possível formar um triângulo com três palitos.

Sua tarefa é, dados os comprimentos A, B e C de três palitos, dizer se é possível formar um 
triângulo com esses palitos e, em caso afirmativo, dizer a qual grupo o triângulo formado 
pertence.

Input

A entrada consiste de uma única linha, contendo três inteiros A, B e C (1 ≤ A, B, C ≤ 10^4) 
separados por espaço.

Output

Imprima uma linha contendo apenas uma letra minúscula:

    'n' se não for possível formar um triângulo;
    'a' se o triângulo formado for acutângulo;
    'r' se o triângulo formado for retângulo;
    'o' se o triângulo formado for obtusângulo. 
'''

A, B, C = map(int, input().split())
if ((A+B>C and A+C>B and B+C>A)):
    if(A*A + B*B == C*C or A*A + C*C == B*B or B*B + C*C == A*A):
        print('r')
    elif(A*A + B*B < C*C or A*A + C*C < B*B or B*B + C*C < A*A ):
        print('o')
    else:
        print('a')
else:
    print('n')