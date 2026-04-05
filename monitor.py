import requests
import os

url = "https://www.jogueinavila.com.br"
arquivo_estado = "estado.txt"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")


def enviar_telegram(mensagem):
    link = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(link, data=data)


def ja_notificado():
    try:
        with open(arquivo_estado, "r") as f:
            return f.read() == "enviado"
    except:
        return False


def salvar_estado():
    with open(arquivo_estado, "w") as f:
        f.write("enviado")


try:
    response = requests.get(url)
    content = response.text.lower()

    if "novidades em breve" in content:
        print("⏳ Ainda não abriu")
    else:
        print("🚨 MUDOU!")

        if not ja_notificado():
            print("📩 Enviando alerta...")
            mensagem = "🚨 ATENÇÃO!\n\nO site do Jogue na Vila mudou!\nPode ter aberto inscrição!\n\nhttps://www.jogueinavila.com.br"
            enviar_telegram(mensagem)
            salvar_estado()
        else:
            print("🔁 Já avisado anteriormente")

except Exception as e:
    print(f"Erro: {e}")
