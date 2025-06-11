'''
Escreva uma função que receba uma data no formato dia/mes/ano, verifique se é 
uma data válida, e retorne a data por extenso.

Input

A função recebe 3 (três) valores inteiros dia (1 ≤ dia ≤ 31 ), mes (1 ≤ mes ≤ 12) 
e ano ( - 10000 ≤ ano ≤ 10000), que representam a data, onde d é o dia, m é o mês 
e a é o ano.

Output

A função deve retornar uma string contendo a data escrita por extenso.

Assinatura da função em Python:

def dia(dia, mes, ano)

O dia deve ser formatado com exatamente dois algarismos. Caso a data não seja 
válida a função deve retornar Data Invalida.

Os nomes dos meses devem ser escritos em minúsculas, sem acentos, sem cedilha.

Considere o mês de fevereiro sempre com 28 dias. Não é necessário verificar se 
é um ano bissexto.
'''

def dia(dia, mes, ano):
    if mes < 1 or mes > 12 or ano < -10000 or ano > 10000:
        return "Data Invalida"
    else:
        if (mes == 2 and (dia < 1 or dia > 28)):
            return "Data Invalida"
        elif (mes == 4 or mes == 6 or mes == 9 or mes == 11) and (dia < 1 or dia > 30):
            return "Data Invalida"
        else:
            if dia < 1 or dia > 31:
                return "Data Invalida"
            else:
                meses_do_ano = ["janeiro", "fevereiro", "marco", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
                data = f"{dia:02d} de {meses_do_ano[mes - 1]} de {ano}"
                return data