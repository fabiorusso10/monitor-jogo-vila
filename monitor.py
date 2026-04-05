import requests
import os

url = "https://www.jogueinavila.com.br"

# Pega dados do GitHub Secrets (NÃO fica no código)
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

ARQUIVO_ESTADO = "estado.txt"


def enviar_telegram(mensagem):
    link = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(link, data=data)


def ja_enviado():
    try:
        with open(ARQUIVO_ESTADO, "r") as f:
            return f.read().strip() == "enviado"
    except:
        return False


def salvar_estado():
    with open(ARQUIVO_ESTADO, "w") as f:
        f.write("enviado")


try:
    response = requests.get(url)
    content = response.text.lower()

    if "novidades em breve" in content:
        print("⏳ Ainda não abriu")
    else:
        print("🚨 MUDOU!")

        if not ja_enviado():
            print("📩 Enviando alerta...")

            mensagem = (
                "🚨 ATENÇÃO!\n\n"
                "O site do Jogue na Vila mudou!\n"
                "Pode ter aberto inscrição!\n\n"
                "👉 https://www.jogueinavila.com.br"
            )

            enviar_telegram(mensagem)
            salvar_estado()
        else:
            print("🔁 Já avisado antes")

except Exception as e:
    print(f"Erro: {e}")
