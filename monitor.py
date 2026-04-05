import requests

url = "https://www.jogueinavila.com.br"

try:
    response = requests.get(url)
    content = response.text.lower()

    if "novidades em breve" in content:
        print("⏳ Ainda não abriu (mensagem continua no site)")
    else:
        print("🚨 ATENÇÃO: O site mudou! Pode ter aberto inscrição!!!")

except Exception as e:
    print(f"Erro ao acessar o site: {e}")
