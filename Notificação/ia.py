from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key="AIzaSyCfYWl3wYcnu94LqNxeeRzdjfNCCzJoP7c")
pergunta = input("Digite sua duvida aqui, a IA do Google ira responder: ")


resposta = client.models.generate_content(
    model="gemini-3-flash-preview", 
    contents= pergunta
)
print(resposta.text)