# Variáveis 

# Números
velocidade_internet = 10
print(velocidade_internet)
nota_filme = 8.5 # float
# valores boleanos
esta_aberto = True 
# Srings
nome_do_curso = 'Lógica de Programação'

# Como variáveis podem ser usadas em um progrma real ?
# Problema 1 - Valor por hora
# Escreva um programa que retorne o valor por hora de um funcionário com base no seu salário normal e horas trabalhadas por mês.
''''
input salario_mensal
input horas_trabalhadas_por_mes
valor_hora = salario_mensal / horas_trabalhadas_por_mes
print valor_hora
'''
salario_mensal = input ("Qual é o seu salário mensal ?")
horas_trabalhadas_por_mes = input ('Quantas horas trabalha por mês ?')
valor_hora = int (salario_mensal) / int(horas_trabalhadas_por_mes)
print(valor_hora)
