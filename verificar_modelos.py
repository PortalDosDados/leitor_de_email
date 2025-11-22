import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configura a chave
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

print("🔍 Perguntando ao Google quais modelos você pode usar...")

try:
    for m in genai.list_models():
        # Filtra apenas modelos que geram texto (ignora modelos de 'embedding')
        if 'generateContent' in m.supported_generation_methods:
            print(f"✅ Disponível: {m.name}")
except Exception as e:
    print(f"❌ Erro ao listar: {e}")