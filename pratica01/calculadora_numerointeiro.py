"""
Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula:
 DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.

"""
# Variáveis 
numero_a = int(input("Digite o valor de A: "))
numero_b = int(input("Digite o valor de B: "))
numero_c = int(input("Digite o valor de C: "))
numero_d = int(input("Digite o valor de D: "))

# calculo da diferença
diferenca = (numero_a * numero_b - numero_c * numero_d)

print(f"A fórmula para a Diferença (A * B) - (C * D) é ")
print(f"Substituindo os valores fornecidos ({numero_a}*{numero_b})-({numero_c}*{numero_d}) ")
print(f"O resultado da DIFERENÇA = {diferenca}")
