name: Monitorar Site

on:
  workflow_dispatch:
  schedule:
    - cron: '0 12 * * *'
    - cron: '0 16 * * *'
    - cron: '0 22 * * *'

jobs:
  check-site:
    runs-on: ubuntu-latest

    steps:
      - name: Baixar código
        uses: actions/checkout@v4

      - name: Configurar Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Instalar dependências
        run: pip install requests

      - name: Rodar script
        run: python monitor.py
        env:
          TELEGRAM_TOKEN: ${{ secrets.TELEGRAM_TOKEN }}
          TELEGRAM_CHAT_ID: ${{ secrets.TELEGRAM_CHAT_ID }}
