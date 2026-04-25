alunos  = []
# Pergunta a quantidade
qtde = int(input( "Quantos alunos temos hoje?"))
# laço de repetiçao e armazenamento 
for i in range(qtde):
    nome = input(f"Digite o nome do {i + 1}º Aluno ")
    alunos.append(nome)

alunos.sort(reverse=True)

# Saída
print("-- Lista de presença ---")
for lista_nome in alunos:
     print(f" - {lista_nome}")