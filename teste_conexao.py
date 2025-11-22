import socket

host = "imap.gmail.com"
port = 993

print(f"Testando conexão com {host}:{port}...")

try:
    # Tenta conectar por 5 segundos
    socket.create_connection((host, port), timeout=5)
    print("✅ SUCESSO! A conexão com o Gmail está liberada.")
    print("O problema provável é lentidão na autenticação ou credenciais.")
except Exception as e:
    print(f"❌ BLOQUEADO! O Python não consegue sair para a internet.")
    print(f"Erro: {e}")