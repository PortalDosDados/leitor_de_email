import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

print(f"Token: {TOKEN[:10]}...") # Mostra o começo pra conferir
print(f"Chat ID: {CHAT_ID}")

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID, 
    "text": "🔔 Teste de conexão do Lancelot.", 
    # Tirei o parse_mode para testar sem formatação primeiro
}

response = requests.post(url, data=data)

print(f"\nStatus Code: {response.status_code}")
print(f"Resposta do Telegram: {response.text}")