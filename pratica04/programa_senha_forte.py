"""
Crie um programa que verifique se uma senha é forte. Uma senha forte deve ter pelo menos 8 caracteres e conter pelo menos um número. O programa deve continuar pedindo senhas até que uma válida seja inserida ou o usuário digite 'sair'.
"""
while True:
    senha = input("Digite a senha ou 'Sair'para encerrar ")
    # Verifica se usuário quer Sair 
    if senha.lower() == "Sair":
        break
    # Verifica o comprimento da senha 
    if len(senha) < 8:
        print("Senha Fraca. A senha precisa conter pelo menos 8 caracteres")
        continue
    # Verifica se a Senha contém um número
    if not any (caracter.isdigit()for caracter in senha):
        print("Senha Fraca: Deve conter pelo menos um número.")
        continue
     # Verifica se a Senha contém um letra
    if not any (caracter.isalpha()for caracter in senha):
        print("Senha Fraca: Deve conter pelo menos uma letra.")
        continue
     # Verifica se a Senha contém uma Letra Maiúscula
    if not any (caracter.isupper()for caracter in senha):
        print("Senha Fraca: Deve conter pelo menos uma Letra Maiúscula.")
        continue

    # Se chegou até aqui, a senha é Válida.
    print("Senha É Forte e Válida.")




