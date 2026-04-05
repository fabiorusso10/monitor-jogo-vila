import requests
import os
import hashlib

url = "https://www.jogueinavila.com.br"

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

ARQUIVO_HASH = "hash.txt"


def enviar_telegram(mensagem):
    link = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = {
        "chat_id": CHAT_ID,
        "text": mensagem
    }
    requests.post(link, data=data)


def gerar_hash(conteudo):
    return hashlib.md5(conteudo.encode()).hexdigest()


def ler_hash_salvo():
    try:
        with open(ARQUIVO_HASH, "r") as f:
            return f.read().strip()
    except:
        return None


def salvar_hash(novo_hash):
    with open(ARQUIVO_HASH, "w") as f:
        f.write(novo_hash)


try:
    response = requests.get(url)
    content = response.text

    hash_atual = gerar_hash(content)
    hash_antigo = ler_hash_salvo()

    if hash_antigo is None:
        print("📌 Primeira execução - salvando estado")
        salvar_hash(hash_atual)

    elif hash_atual != hash_antigo:
        print("🚨 SITE MUDOU!")

        mensagem = (
            "🚨 ATENÇÃO!\n\n"
            "O site do Jogue na Vila foi atualizado!\n"
            "Pode ter novidade importante 👀\n\n"
            "👉 https://www.jogueinavila.com.br"
        )

        enviar_telegram(mensagem)
        salvar_hash(hash_atual)

    else:
        print("⏳ Sem mudanças no site")

except Exception as e:
    print(f"Erro: {e}")
