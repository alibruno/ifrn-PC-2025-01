# Escreva um programa que leia dois números reais a e b e mostre a média entre os dois.

# Input
# A entrada é composta de duas linhas. Cada uma das linhas contém um número real de precisão dupla.

# Output
# Seu programa deve mostrar a média aritmética entre valores lidos e deve conter exatamente 5 (cinco) casas decimais.

num1 = float(input())
num2 = float(input())
arithmeticMean = (num1+num2)/2
print("{:.5f}".format(arithmeticMean))