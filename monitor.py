import requests

url = "https://www.jogueinavila.com.br"  # depois a gente troca pelo site real

try:
    response = requests.get(url)
    content = response.text.lower()

    if "google" in content:
        print("✅ Palavra encontrada! Site OK")
    else:
        print("❌ Palavra NÃO encontrada!")

except Exception as e:
    print(f"Erro ao acessar o site: {e}")
