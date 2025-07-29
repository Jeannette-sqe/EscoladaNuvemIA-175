"""
4- Conversor de Temperatura 

Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin. 

O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""
# Solicitação da Temperatura e Escala de Temperatura

temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem da temperatura (C,F ou K): ").upper()
destino = input("Digite a unidade de conversão da temperatura desejada (C,F ou K): ").upper()

if origem == destino:
    resultado = temperatura

elif origem == "C": # origem Celsius
    if destino == "F": # origem Celsius e destino Fahrenheit
        resultado = (temperatura * 9/5) + 32
    else: # origem Celsius e destino Kelvin
        resultado = temperatura + 273.15

elif origem == "F": # Origem Fahrenheit 
    if destino == "C": # Origem Fahrenheit e destino Celsius
        resultado = (temperatura - 32) * 5/9
    else: # origem Fahrenheit e destino Kelvin
        resultado = (temperatura -32) * 5/9 + 273.15

else: # Origem Kelvin
    if destino == "C": # Origem Kelvin e destino Fahrenheit 
        resultado = temperatura - 273.15
    else: # Origem Kelvin e destino Fahrenheit 
        resultado = (temperatura - 273.15) * 9/5 + 32


print (f"{temperatura} {origem} é igual a {resultado} {destino}")

