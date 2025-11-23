# 🤖 Lancelot Briefing Bot (Leitor de E-mail com IA)

> **Automação de Inteligência de Mercado: Do Gmail ao Telegram em segundos.**

![Python](https://img.shields.io/badge/Python-3.12%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/AI-Google%20Gemini-orange?style=for-the-badge&logo=google&logoColor=white)
![Telegram](https://img.shields.io/badge/Bot-Telegram-blue?style=for-the-badge&logo=telegram&logoColor=white)
![Status](https://img.shields.io/badge/Status-Functional-brightgreen?style=for-the-badge)

## 📖 Sobre o Projeto

O **Lancelot Briefing Bot** é um robô de automação (RPA) desenhado para profissionais que precisam filtrar o ruído e focar no que importa. 

Ele monitora silenciosamente sua caixa de entrada (Gmail), identifica e-mails de remetentes estratégicos (como McKinsey, Harvard, MIT ou Newsletters técnicas), utiliza a IA do **Google Gemini** para ler e resumir o conteúdo, e envia um *briefing* executivo em Português diretamente para o seu Telegram.

---

## ✨ Funcionalidades

* **🕵️‍♂️ Monitoramento VIP:** Varredura automática via protocolo IMAP focada apenas na sua *Watchlist* (Lista de Vigilância).
* **🧠 Leitura com IA:** Utiliza o modelo `Gemini 2.5 Flash` para interpretar textos técnicos e longos.
* **📝 Resumo Executivo:** Transforma e-mails complexos em *bullet points* acionáveis em PT-BR.
* **📱 Notificação Push:** Entrega o relatório formatado no Telegram em tempo real.
* **🔒 Segurança:** Zero exposição de senhas no código (uso de variáveis de ambiente).
* **⚙️ Automação:** Pronto para execução em background ou via Agendador de Tarefas do Windows.

---

## 🛠️ Tech Stack

* **Linguagem:** `Python 3.12`
* **Inteligência Artificial:** `Google Generative AI` (Gemini API)
* **Conectividade:** `imap-tools` (E-mail) & `Requests` (Telegram API)
* **Segurança:** `python-dotenv` (Gestão de Credenciais)

---

## 📂 Estrutura do Projeto

```text
/
├── .venv/               # Ambiente Virtual (Ignorado pelo Git)
├── .env                 # Arquivo de Credenciais (CRIE ESTE ARQUIVO)
├── .gitignore           # Lista de arquivos ignorados
├── main.py              # 🏠 Código Principal do Robô
├── requirements.txt     # Dependências do projeto
└── README.md            # Documentação
🚀 Guia de Instalação
1. Clone o repositório
Bash

git clone [https://github.com/SEU-USUARIO/lancelot-briefing-bot.git](https://github.com/SEU-USUARIO/lancelot-briefing-bot.git)
cd lancelot-briefing-bot
2. Configure o Ambiente Virtual
Recomendado para isolar as dependências do projeto.

Windows:

Bash

python -m venv .venv
.\.venv\Scripts\activate
Linux/Mac:

Bash

python3 -m venv .venv
source .venv/bin/activate
3. Instale as Dependências
Bash

pip install -r requirements.txt
🔐 Configuração de Segurança (.env)
Este projeto requer chaves de acesso. Crie um arquivo chamado .env na raiz do projeto e preencha conforme o modelo abaixo:

Ini, TOML

# Configurações do Gmail
EMAIL_USER=seu_email@gmail.com
EMAIL_PASS=senha_de_app_de_16_digitos

# Configurações de IA e Bot
GOOGLE_API_KEY=sua_chave_api_gemini
TELEGRAM_TOKEN=seu_token_do_botfather
TELEGRAM_CHAT_ID=seu_id_numerico
⚠️ Como obter a EMAIL_PASS (Senha de App do Google)
Por segurança, o Google não permite usar sua senha de login normal. Siga os passos:

Acesse sua Conta Google > Segurança.

Ative a Verificação em duas etapas (2FA).

Busque por "Senhas de App" (App Passwords).

Crie uma nova senha (dê o nome de "BriefingBot").

Copie o código de 16 letras gerado e cole no .env.

⚙️ Personalização (Lista VIP)
Para definir quais e-mails o robô deve ler, abra o arquivo main.py e edite a lista VIPS. O robô buscará por qualquer e-mail que contenha esses termos no remetente.

Python

VIPS = [
    "mckinsey.com",
    "harvard.edu",
    "newsletter@dados.com.br",
    "medium.com",
    "chefe@empresa.com"
]
▶️ Como Executar
Com tudo configurado, basta rodar o script:

Bash

python main.py
Dica: Você pode usar o "Agendador de Tarefas" do Windows (Task Scheduler) para rodar esse script automaticamente todo dia às 08:00 da manhã.

⚠️ Aviso Legal
Este software processa dados sensíveis (e-mails). O código roda localmente na sua máquina e nenhum dado é enviado para servidores externos além das APIs oficiais do Google e Telegram. Jamais suba seu arquivo .env para repositórios públicos.

Desenvolvido com 💙 por Portal dos Dados.