import requests
import os

url = "https://www.jogueinavila.com.br"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_telegram(mensagem):
    link = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(link, data=data)


try:
    response = requests.get(url)
    content = response.text.lower()

    if "novidades em breve" in content:
        print("⏳ Ainda não abriu")
    else:
        print("🚨 MUDOU! Enviando alerta...")

        mensagem = (
            "🚨 ATENÇÃO!\n\n"
            "O site do Jogue na Vila mudou!\n"
            "Pode ter aberto inscrição!\n\n"
            "👉 https://www.jogueinavila.com.br"
        )

        enviar_telegram(mensagem)

except Exception as e:
    print(f"Erro: {e}")
