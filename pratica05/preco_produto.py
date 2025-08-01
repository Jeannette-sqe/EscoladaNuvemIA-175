"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. 
Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""
def calcular_preco_final(preco_produto, percentual_desconto):
    preco_final = preco_produto - (preco_produto * (percentual_desconto / 100))
    return preco_final

preco_produto  = float(input("Informe o preço do produto: R$ "))
percentual_desconto = float(input("Informe o percentual de desconto (%): "))

preco_final = calcular_preco_final(preco_produto, percentual_desconto)

print(f"O preço final do produto de R$ {preco_produto:.2f} ,com um desconto de {percentual_desconto}% ficará em  R$ {preco_final:.2f}")


