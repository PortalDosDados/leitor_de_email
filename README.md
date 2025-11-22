# 🛡️ Lancelot Briefing Bot (Leitor de E-mail com IA)

> "Quando não se agrega valor, se agrega custo."

Este projeto é um robô de automação que monitora uma caixa de entrada (Gmail), filtra e-mails de remetentes estratégicos (como McKinsey, Harvard, MIT), lê o conteúdo utilizando Inteligência Artificial (Google Gemini) e envia um resumo executivo traduzido para o Telegram.

## 🚀 Funcionalidades

* **Monitoramento VIP:** Varre a caixa de entrada buscando apenas remetentes configurados na lista de vigilância.
* **IA Integrada:** Utiliza o modelo `Gemini 2.5 Flash` (Google) para leitura rápida e contextual.
* **Resumo Executivo:** Transforma e-mails longos e técnicos em bullet points estratégicos em Português (PT-BR).
* **Notificação Mobile:** Envia o relatório formatado diretamente para um bot no Telegram.
* **Segurança:** Credenciais protegidas via variáveis de ambiente (`.env`).
* **Automação:** Pronto para rodar via Agendador de Tarefas do Windows.

## 🛠️ Tecnologias Utilizadas

* **Python 3.12**
* **Google Generative AI** (Gemini API)
* **imap-tools** (Leitura de e-mails)
* **Requests** (API do Telegram)
* **python-dotenv** (Gestão de segurança)

---

## ⚙️ Configuração e Instalação

## 1. Clone o repositório

git clone [https://github.com/SEU-USUARIO/leitor-mckinsey.git](https://github.com/SEU-USUARIO/leitor-mckinsey.git)
cd leitor-mckinsey


## 2. Crie o Ambiente Virtual
python -m venv venv

* **No Windows:**
    * .\venv\Scripts\activate

* **No Linux/Mac:**
    * source venv/bin/activate

## 3. Instale as dependências
pip install -r requirements.txt

## 4. Configuração das Credenciais (.env)
Crie um arquivo chamado .env na raiz do projeto (ele não será enviado ao GitHub). Preencha com suas chaves:

* EMAIL_USER=seu_email@gmail.com
* EMAIL_PASS=senha_de_app_do_google_16_digitos
* GOOGLE_API_KEY=sua_chave_api_gemini
* TELEGRAM_TOKEN=seu_token_botfather
* TELEGRAM_CHAT_ID=seu_id_numerico_telegram

Nota: Para obter a EMAIL_PASS, ative a autenticação de dois fatores no Google e gere uma "Senha de App". Não use sua senha de login habitual.

## Personalizar a Lista VIP
Abra o arquivo main.py e edite a lista VIPS para adicionar ou remover remetentes que deseja monitorar:

VIPS = [
    "mckinsey",
    "harvard",
    "mit.edu",
    "newsletter@dados",
    "medium"
]
