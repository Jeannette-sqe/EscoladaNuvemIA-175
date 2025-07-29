"""
5- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.

Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""
# Verificar se é Bissexto 

ano = int(input("Digite o ano: "))
if ano % 4 == 0: # Se o ano for divisível por 4, ele pode ser bissexto
    if ano % 100 == 0: # Se for divisível por 100, precisa ser analisado
        if ano % 400 == 0:
            print(f"O ano {ano} é bissexto")
        else:
            print (f"O ano {ano} não é ano bissexto")
    else: # Se for divisível por 4, mas não por 100, então é bissexto.
        print(f"O ano {ano} é bissexto")
else: # Se não divisível por 4, então é bissexto 
    print (f"O ano {ano} não é bissexto")




 

