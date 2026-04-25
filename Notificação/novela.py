import os
from google import genai
from google.genai import types

def save_binary_file(file_name, data):
    with open(file_name, "wb") as f:
        f.write(data)
    print(f"Imagem salva como: {file_name}")

def generate():
    # 1. Use a chave DIRETAMENTE aqui (Troque pela sua nova chave!)
    minha_chave = "AIzaSyCfYWl3wYcnu94LqNxeeRzdjfNCCzJoP7c"
    
    client = genai.Client(api_key=minha_chave)

    # 2. Se você quer que ele se baseie em uma imagem, você precisa carregar o arquivo
    # Se não tiver uma imagem de referência, remova a parte do 'imagem_referencia'
    caminho_da_foto = "image.png" # Nome do arquivo que está na sua pasta
    
    with open(caminho_da_foto, "rb") as f:
        image_bytes = f.read()

    model = "gemini-2.5-flash-image" # Modelo atualizado que suporta geração de imagem

    contents = [
        types.Content(
            role="user",
            parts=[
                # Enviando a imagem de referência
                types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
                # O comando em texto
                types.Part.from_text(text="Quero a imagem de um abacate e de um morango musculosos, seguindo exatamente o estilo desta imagem em anexo."),
            ],
        ),
    ]

    generate_content_config = types.GenerateContentConfig(
        response_modalities=["IMAGE"],
    )

    print("Gerando imagem... aguarde.")
    
    try:
        response = client.models.generate_content(
            model=model,
            contents=contents,
            config=generate_content_config,
        )

        for i, part in enumerate(response.parts):
            if part.inline_data:
                save_binary_file(f"resultado_{i}.png", part.inline_data.data)
    except Exception as e:
        print(f"Erro ao gerar: {e}")

if __name__ == "__main__":
    generate()