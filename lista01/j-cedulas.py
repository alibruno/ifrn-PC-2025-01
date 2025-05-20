# Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

# Input
# O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

# Output
# Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: "Presentation Error".

N = int(input())
cedulas100 = N // 100
cedulas50 = (N - cedulas100*100) // 50
cedulas20 = (N - (cedulas100*100 + cedulas50*50)) // 20
cedulas10 = (N - (cedulas100*100 + cedulas50*50 + cedulas20*20)) // 10
cedulas5 = (N - (cedulas100*100 + cedulas50*50 + cedulas20*20 + cedulas10*10)) // 5
cedulas2 = (N - (cedulas100*100 + cedulas50*50 + cedulas20*20 + cedulas10*10 + cedulas5*5)) // 2
cedulas1 = (N - (cedulas100*100 + cedulas50*50 + cedulas20*20 + cedulas10*10 + cedulas5*5 + cedulas2*2))
    
print(N)
print(cedulas100, "nota(s) de R$ 100,00")
print(cedulas50, "nota(s) de R$ 50,00")
print(cedulas20, "nota(s) de R$ 20,00")
print(cedulas10, "nota(s) de R$ 10,00")
print(cedulas5, "nota(s) de R$ 5,00")
print(cedulas2, "nota(s) de R$ 2,00")
print(cedulas1, "nota(s) de R$ 1,00")