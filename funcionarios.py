import pandas as pd

# Carrega o arquivo
df = pd.read_excel('dados_funcionarios.xlsx')

# --- O PULO DO GATO ---
# 1. str.strip() remove espaços extras
# 2. str.lower() coloca tudo em minúsculo
df.columns = df.columns.str.strip().str.lower()

# Agora, independentemente de como o aluno digitou na planilha,
# as colunas no seu código serão sempre "registro", "nome" e "horas".

# Agrupar (usando os nomes padronizados)
resultado = df.groupby(["registro", "nome"])["horas"].sum()

# Mostrando o Resultado
for (registro, nome), horas in resultado.items():
    print(f"{registro} - {nome} - {horas} horas")