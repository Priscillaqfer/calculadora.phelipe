
import os
import smtplib
from pathlib import Path
from email.message import EmailMessage

# ==================================
# 1. CONFIGURAÇÕES
# ==================================

REMETENTE = os.getenv("GMAIL_EMAIL")
SENHA = os.getenv("GMAIL_APP_PASSWORD")

DESTINATARIO = REMETENTE

ASSUNTO = "Newsletter ITA - Teste de Layout"

# ==================================
# 2. LEITURA DO HTML
# ==================================

caminho_html = Path(__file__).with_name("email.html")

if not caminho_html.exists():
    raise FileNotFoundError("Arquivo email.html não encontrado!")

with open(caminho_html, "r", encoding="utf-8") as arquivo:
    html = arquivo.read()

print("Arquivo HTML carregado!")
print("Tamanho do HTML:", len(html), "caracteres")

# ==================================
# 3. MONTAGEM DO E-MAIL
# ==================================

mensagem = EmailMessage()

mensagem["Subject"] = ASSUNTO
mensagem["From"] = REMETENTE
mensagem["To"] = DESTINATARIO

mensagem.set_content(
    "Este e-mail contém uma versão HTML. "
    "Abra em um cliente de e-mail compatível para visualizar o layout."
)

mensagem.add_alternative(html, subtype="html")

# ==================================
# 4. ENVIO
# ==================================

try:

    if not REMETENTE or not SENHA:
        raise ValueError("Credenciais do Gmail não configuradas.")

    print("Conectando ao Gmail...")

    with smtplib.SMTP_SSL(
        "smtp.gmail.com",
        465,
        timeout=30
    ) as servidor:

        servidor.login(REMETENTE, SENHA)

        print("Autenticação realizada!")

        servidor.send_message(mensagem)

        print("E-mail enviado com sucesso!")
        print("Destinatário:", DESTINATARIO)

except Exception as erro:

    print(f"Erro no envio: {type(erro).__name__}: {erro}")


