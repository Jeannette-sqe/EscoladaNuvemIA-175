"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""

def calcular_idade(ano_nasc,ano_atual):
    idade = (ano_atual - ano_nasc) * 365
    return idade

ano_nasc = int(input("Insira o ano seu nascimento: "))
ano_atual = int(input("Insira o ano atual: "))

idade = calcular_idade(ano_nasc, ano_atual)

print(f"A idade da pessoa em dias é: {idade} ")