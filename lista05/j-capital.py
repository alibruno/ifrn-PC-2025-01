'''
O governo do estado de Queensland está com problemas sérios de trânsito na 
capital Brisbane, onde estão os prédios administrativos. Para desafogar o 
trânsito, o prefeito de Brisbane e o governador de Queensland decidiram que 
uma nova capital administrativa deve ser construída em uma área fora de Brisbane. 
Para projetar a nova capital, o renomado arquiteto minimalista Joe Bloggs foi 
contratado.

Bloggs foi informado de que o terreno destinado à nova capital ainda não foi 
demarcado, mas será retangular. Além disso, a cidade deverá ser dividida em 
quatro zonas, uma delas destinada a uma reserva ambiental e cada uma das outras 
três receberá os novos prédios de cada um dos três poderes (Executivo, Legislativo 
e Judiciário). Em um arroubo de criatividade, Bloggs decidiu que duas avenidas, 
perpendiculares entre si, cada uma paralela a dois dos lados do terreno retangular, 
dividirão a capital nas quatro zonas.

Bloggs recebeu do governo as áreas de cada uma das zonas e, após muito esforço, 
encontrou um retângulo que pode ser dividido conforme seus planos e de forma a 
respeitar as áreas delimitadas. No entanto, a Fundação de Conservação dos Cangurus 
determinou que a área destinada à reserva ambiental era muito pequena, o que 
obrigou o governo a alterar as áreas das quatro zonas. Após receber as novas 
medidas, Bloggs tentou encontrar um novo retângulo que viabilizasse seu projeto, 
porém sem sucesso. Cansado de fazer testes, ele pensou que talvez tenha que 
abandonar sua brilhante ideia. Por isso, ele pediu para você escrever um programa 
que, dadas as áreas das quatro zonas, determine se ele poderá ou não manter seu 
projeto (ou seja, se existe um retângulo que possa ser dividido por duas retas 
perpendiculares, cada uma paralela a dois dos lados do retângulo, tal que as 
quatro áreas formadas obedeçam às exigências do governo).

Input

A entrada consiste de uma única linha contendo quatro inteiros A1, A2, A3, A4, 
indicando área de casa uma das zonas.

Output

Imprima uma única linha contendo um único caractere: 'S' se Bloggs pode preservar 
seu projeto e 'N' caso contrário.
'''

A1, A2, A3, A4 = map(int, input().split())

if(A1*A2 == A3*A4 or A1*A3 == A2*A4 or A1*A4 == A2*A3):
    print('S')
else:
    print('N')