"""
 4- Calculadora de Consumo de Combustível
 Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
 Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""
# Dados das variáveis

distancia_percorrida = 300
combustivel_gasto = 25

# Calculos de consumo de combustível

consumo_medio = distancia_percorrida/combustivel_gasto

# apresentação do resultado final

print("Dados da Viagem:")
print(f"Distância Percorrida: {distancia_percorrida: .2f} Km")
print(f"Combustível Gasto: {combustivel_gasto: .2f} L")
print(f"Consumo Médio: {consumo_medio: .2f} Km/L")






