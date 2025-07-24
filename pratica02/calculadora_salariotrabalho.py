"""
6-Calculadora de salário por horas trabalhadas

Leia o número de um funcionário, seu número de horas trabalhadas e o valor que recebe por hora. Calcule o salário do funcionário e exiba o resultado formatado corretamente.

Entrada:

O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:

Número do funcionário (numero_funcionario).

Quantidade de horas trabalhadas (horas_trabalhadas).

Valor recebido por hora (valor_por_hora).

Saída:

Imprima o número do funcionário e o salário calculado com duas casas decimais. Deve haver um espaço em branco antes e depois do sinal de igualdade, e no caso do salário, também um espaço em branco após o R$
"""
# Variáveis

numero_funcionario = int(input("Digite o numero do funcionário: "))
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor por hora: "))

# Calculo das variáveis

salario = horas_trabalhadas * valor_por_hora

# Resultados - apresentação

print("Dados de Salário do Funcionário")
print ("ID Funcionário : ", numero_funcionario)
print("Quantidade de horas trabalhadas: ",horas_trabalhadas)
print(f"Valor da hora: R$  {valor_por_hora: .2f}")
print(f"Salário do funcionário : R$ {salario: .2f}")
