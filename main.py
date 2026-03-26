from openai import OpenAI

# Pega aquí el token que copiaste en el paso 1
GITHUB_TOKEN = "tu_token_aqui"

client = OpenAI(
    base_url="https://models.inference.ai.azure.com",
    api_key=GITHUB_TOKEN,
)

def chat_con_ia(mensaje_usuario):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "Eres un asistente de ventas para WhatsApp."},
            {"role": "user", "content": mensaje_usuario},
        ],
        model="gpt-4o",
    )
    return response.choices[0].message.content

# Prueba tu demo
print(chat_con_ia("Hola, ¿qué servicios ofreces?"))
