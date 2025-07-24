"""
3- Calculadora de Média Escolar 
Crie um programa que calcula a media escolar de um aluno.
Use as seguintes notas:

Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""
# Dados das Notas
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# Calculo da Média 

media = (nota1 + nota2 + nota3) / 3

# Apresentação das Notas

print("Notas do Aluno:")
print (f"Primeira Nota:  {nota1: .2f}")
print (f"Segunda Nota:  {nota2: .2f}")
print (f"Terceira Nota:  {nota3: .2f}")
print (f"Média Final: {media: .2f}")


