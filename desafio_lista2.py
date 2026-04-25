alunos_e_notas = []
quantidade = int(input("Quantos alunos? "))

for i in range(quantidade):
    nome = input(f"Nome do aluno {i+1}: ")
    nota = float(input(f"Nota do aluno {i+1}: "))
    # Adicionamos uma lista com dois valores dentro da lista principal
    alunos_e_notas.append([nome, nota])

print("\n--- REGISTRO FINAL ---")
for registro in alunos_e_notas:
    nome = registro[0]
    nota = registro[1]
    print(f"Aluno: {nome:<10} | Nota: {nota:>5.1f}")