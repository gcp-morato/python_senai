import customtkinter as ctk

# --- LÓGICA (O "Cérebro" do App) ---
# Criamos uma lista vazia para guardar os nomes
lista_alunos = []

def registrar_aluno():
    # 1. Pegamos o nome que o aluno digitou na caixa
    nome = entrada_nome.get() 
    
    # 2. Verificamos se ele não deixou a caixa vazia
    if nome != "": 
        lista_alunos.append(nome) # Adiciona na lista
        
        # 3. Criamos um texto bonito com todos os nomes
        # O "\n" serve para pular uma linha entre cada nome
        texto_exibicao = "\n".join(lista_alunos)
        
        # 4. Atualizamos o rótulo na tela com a lista nova
        rotulo_lista.configure(text=f"Alunos Presentes:\n{texto_exibicao}")
        
        # 5. Limpamos a caixa de entrada para o próximo nome
        entrada_nome.delete(0, 'end')

# --- INTERFACE (O "Corpo" do App) ---
# Configuramos o tema (opcional)
ctk.set_appearance_mode("dark")  # Modo escuro
ctk.set_default_color_theme("blue") # Cor azul

janela = ctk.CTk() # Cria a janela principal
janela.title("Registro de Frequência - SENAI")
janela.geometry("400x500")

# 1. Título na tela
titulo = ctk.CTkLabel(janela, text="Frequência Digital 📝", font=("Arial", 20, "bold"))
titulo.pack(padx=20, pady=20)

# 2. Campo para o usuário digitar
entrada_nome = ctk.CTkEntry(janela, placeholder_text="Digite o nome do aluno", width=250)
entrada_nome.pack(padx=20, pady=10)

# 3. Botão que chama a função 'registrar_aluno' quando clicado
botao = ctk.CTkButton(janela, text="Registrar Presença", command=registrar_aluno)
botao.pack(padx=20, pady=10)

# 4. Texto que mostrará a lista de nomes registrados
rotulo_lista = ctk.CTkLabel(janela, text="Nenhum aluno registrado ainda.", justify="left")
rotulo_lista.pack(padx=20, pady=20)

# Inicia o aplicativo e impede que ele feche sozinho
janela.mainloop()