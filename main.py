import os
import requests
from dotenv import load_dotenv
from imap_tools import MailBox, AND
import google.generativeai as genai
import socket

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

# Recupera as credenciais
EMAIL_USER = os.getenv('EMAIL_USER')
EMAIL_PASS = os.getenv('EMAIL_PASS')
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TELEGRAM_CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

# Verificação básica de segurança
if not all([EMAIL_USER, EMAIL_PASS, GOOGLE_API_KEY, TELEGRAM_TOKEN]):
    print("ERRO: Faltam variáveis no arquivo .env!")
    exit()

# 2. Configura a IA (Gemini)
genai.configure(api_key=GOOGLE_API_KEY)
MODEL_NAME = 'models/gemini-2.5-flash' # Modelo rápido e eficiente
model = genai.GenerativeModel(MODEL_NAME)

def enviar_telegram(mensagem):
    """Envia o resumo para o seu Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    # Corta em 4000 caracteres para respeitar o limite do Telegram
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
    Você é um consultor de estratégia industrial. Analise este e-mail da McKinsey.
    
    TAREFAS:
    1. Identifique o TEMA CENTRAL em 1 frase.
    2. Liste 3 a 5 BULLET POINTS com os insights mais valiosos (foco em dados, manutenção ou estratégia).
    3. Traduza tudo para Português (Brasil).
    4. Use formatação Markdown (negrito em palavras-chave).
    
    TEXTO ORIGINAL:
    {conteudo_email[:15000]}
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Erro na análise da IA: {e}"

def main():
    print("🛡️ Iniciando Lancelot Briefing Bot...")
    
    # Define um limite: se o Gmail não responder em 60s, dá erro em vez de travar para sempre
    socket.setdefaulttimeout(60)

    print(f"📩 Conectando ao email: {EMAIL_USER}...")

    try:
        with MailBox('imap.gmail.com').login(EMAIL_USER, EMAIL_PASS) as mailbox:
            
            # CRITÉRIO OTIMIZADO:
            # Busca e-mails da McKinsey NÃO LIDOS.
            criterios = AND(from_="mckinsey", seen=False)
            
            # AQUI ESTÁ A MUDANÇA:
            # 1. limit=1 (Pega só o primeiro para testar rápido)
            # 2. bulk=True (Otimiza o download de dados)
            print("🔍 Buscando e-mails não lidos...")
            
            emails = list(mailbox.fetch(criterios, mark_seen=True, limit=1, bulk=True))
            
            if not emails:
                print("✅ Nenhum e-mail novo encontrado. (Verifique se há e-mails 'Não Lidos' da McKinsey)")
                return

            print(f"🚀 Encontrado(s) {len(emails)} e-mail(s). Processando o primeiro...")

            for msg in emails:
                print(f"Processando: {msg.subject}")
                
                # Tenta pegar texto puro, se falhar pega HTML
                corpo_email = msg.text or msg.html
                
                print("🧠 Enviando para IA (pode levar uns 10s)...")
                resumo_ia = analisar_com_gemini(corpo_email)
                
                mensagem_final = (
                    f"📑 **Lancelot Briefing: McKinsey**\n\n"
                    f"📌 *{msg.subject}*\n"
                    f"📅 {msg.date.strftime('%d/%m/%Y')}\n\n"
                    f"{resumo_ia}\n\n"
                    f"_Processado por IA_"
                )
                
                enviar_telegram(mensagem_final)
                print("--> Resumo enviado para o Telegram.")
                
    except TimeoutError:
        print("❌ Erro: Tempo esgotado (Timeout). A internet ou o servidor demorou demais.")
    except Exception as e:
        print(f"❌ Erro crítico: {e}")

if __name__ == "__main__":
    main()