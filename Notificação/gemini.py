import google.generativeai as genai
import os

try:
    # Coloque sua API Key aqui ou use uma variável de ambiente
    api_key = os.getenv("GOOGLE_API_KEY", "AIzaSyCqgYrJRHgTUGYrQnrziqilhCtCzz_13WQ")
    genai.configure(api_key=api_key)

    print("Buscando modelos disponíveis para sua API Key...")
    print("-" * 50)

    for m in genai.list_models():
      # Vamos verificar quais modelos suportam a geração de conteúdo (texto ou áudio)
     if 'generateContent' in m.supported_generation_methods:
        print(f"""Nome do Modelo: {m.name}
- Nome de Exibição: {m.display_name}
- Descrição: {m.description}
- Versão {m.version}
- Limite: {m.output_token_limit}
-geração {m.supported_generation_methods}
- """)
        
    print("-" * 30 + '\n' )

except Exception as e:
    print(f"Ocorreu um erro: {e}")

