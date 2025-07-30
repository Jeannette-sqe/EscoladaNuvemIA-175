"""
Desenvolva uma calculadora em Python que realize as quatro operações básicas (adição, subtração, multiplicação e divisão) entre dois números. A calculadora deve ser capaz de lidar com diversos tipos de erros de entrada e operação. Siga as especificações abaixo:

A calculadora deve solicitar ao usuário que insira dois números e uma operação.

As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).

O programa deve continuar solicitando entradas até que uma operação válida seja concluída.

Trate os seguintes erros:

Entrada inválida (não numérica) para os números

Divisão por zero

Operação inválida

Use try/except para capturar e tratar os erros apropriadamente.

Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.

Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""
while True:
    try:
        # Solicitar os dois números
        num1 = float(input("Digite o primeiro numero: "))
        num2 = float(input("Digite o segundo numero: "))

        # Solicitar a operação
        operacao = input("Digite o tipo de operação que deseja seguir ( + , - , * , /): ").strip()

        # Verificar a validade da operação 

        if operacao not in ['+', '-', '*' , '/']:
            print ("X Operação Inválida. Tente novamente.")
            continue

        # Verificar divisão por zero
        if operacao == '/' and num2 == 0:
            print("X Erro: Divisão por Zero. Tente novamente")
            continue

        # Realizar os cálculos da operação
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        # Mostrar o resultado 
        print(f"Resultado: {resultado}")
        break # Sair do loop

    except ValueError:
        print("X Erro: Por favor digite números válidos")


