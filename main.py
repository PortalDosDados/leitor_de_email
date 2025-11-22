import os
import socket
import requests
from dotenv import load_dotenv
from imap_tools import MailBox, AND
import google.generativeai as genai

# 1. Carrega as variáveis e configurações
load_dotenv()

EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# --- LISTA VIP (Edite aqui para adicionar novos remetentes) ---
# O robô vai buscar e-mails que contenham qualquer um destes nomes no remetente
VIPS = [ 
    "newsletter@mail.datahackers.com.br" 
]

# Configura a IA
if not GOOGLE_API_KEY:
    print("ERRO: GOOGLE_API_KEY não encontrada no .env")
    exit()

genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = 'models/gemini-2.5-flash' 
model = genai.GenerativeModel(MODEL_NAME)

def enviar_telegram(mensagem):
    """Envia o resumo para o seu Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": TELEGRAM_CHAT_ID, 
        "text": mensagem[:4000], 
        "parse_mode": "Markdown"
    }
    try:
        requests.post(url, data=payload)
    except Exception as e:
        print(f"Erro ao enviar Telegram: {e}")

def analisar_com_gemini(conteudo_email):
    """Lê o e-mail e cria o resumo executivo."""
    prompt = f"""
    Você é um consultor de estratégia industrial e dados. Analise este e-mail.
    
    TAREFAS:
    1. Identifique o TEMA CENTRAL em 1 frase.
    2. Liste 3 a 5 BULLET POINTS com os insights mais valiosos.
    3. Traduza tudo para Português (Brasil).
    4. Destaque em negrito dados numéricos ou conclusões chave.
    
    TEXTO ORIGINAL:
    {conteudo_email[:20000]}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro na análise da IA: {e}"

def main():
    print("🛡️ Iniciando Lancelot Briefing Bot (Multi-VIP)...")
    socket.setdefaulttimeout(60) # Evita travamentos longos

    try:
        # Conecta ao Gmail
        with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
            
            print(f"🔍 Varrendo a caixa de entrada para: {VIPS}")

            # --- O NOVO LOOP MÁGICO COMEÇA AQUI ---
            for alvo in VIPS:
                print(f"   > Verificando: {alvo}...")
                
                # Busca e-mails deste alvo que NÃO foram lidos
                # Retirei o 'limit=1' para ele ler TODOS os novos desse remetente
                criterios = AND(from_=alvo, seen=False)
                emails = list(mailbox.fetch(criterios, mark_seen=True, bulk=True))
                
                if not emails:
                    continue # Se não tem nada desse alvo, pula para o próximo

                print(f"   🚀 Encontrado(s) {len(emails)} e-mail(s) de '{alvo}'. Processando...")

                for msg in emails:
                    print(f"      Processando: {msg.subject}")
                    
                    corpo_email = msg.text or msg.html
                    resumo_ia = analisar_com_gemini(corpo_email)
                    
                    mensagem_final = (
                        f"📑 **Lancelot Briefing**\n"
                        f"👤 *Fonte: {alvo.upper()}*\n" # Mostra quem mandou
                        f"📌 *{msg.subject}*\n"
                        f"📅 {msg.date.strftime('%d/%m/%Y')}\n\n"
                        f"{resumo_ia}\n\n"
                        f"_Processado por IA_"
                    )
                    
                    enviar_telegram(mensagem_final)
                    print("      --> Resumo enviado.")
            
            print("✅ Varredura completa.")

    except Exception as e:
        print(f"❌ Erro crítico no script: {e}")

if __name__ == "__main__":
    main()