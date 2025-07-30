"""
Crie um programa que permita a um professor registrar as notas de uma turma. O programa deve continuar solicitando notas até que o professor digite 'fim'. Notas válidas são de 0 a 10. O programa deve ignorar notas inválidas e continuar solicitando. No final, deve exibir a média da turma.
"""
notas = [] # Lista para armazenar as notas 
print("Digite as notas dos alunos(de 0 a 10. Quando encerrar digite 'fim')")

while True: # Manter o programa funcionando até que seja digitado "fim" 
    entrada = input ("Digite a Nota do aluno (ou digite fim para encerrar): ")
    if entrada.lower() == 'fim':
        break # Encerrar o programa
    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print(" Nota Inválida. Digite uma nota entre 0 e 10.")
            continue
    except ValueError:
        print(" Entrada inválida. Digite uma nota ou 'fim'para encerrar.")

# Calcular e exibir a Média
if notas:
    media = sum(notas) / len(notas)
    print(f"Média da turma: {media: .2f}")
    print(f"Total de notas válidas registradas: {len(notas)}")
else:
    print("Nenhuma nota foi lançada.")
    


