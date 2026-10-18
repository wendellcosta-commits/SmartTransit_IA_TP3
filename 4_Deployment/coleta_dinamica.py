# Código criado com auxílio de I.A Google Gemini 2.5
import os
import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

print("Iniciando prova de conceito de extração dinâmica via Selenium...")

# Configura o navegador Chrome para rodar de forma oculta
opcoes = webdriver.ChromeOptions()
opcoes.add_argument('--headless')

# Inicia o WebDriver
driver = webdriver.Chrome(options=opcoes)

# Acessa um portal dinâmico de testes
url = "https://quotes.toscrape.com/js/"
driver.get(url)

time.sleep(2)

sopa = BeautifulSoup(driver.page_source, 'html.parser')
blocos = sopa.find_all('div', class_='quote')

dados_extraidos = []
for bloco in blocos:
    texto = bloco.find('span', class_='text').text
    autor = bloco.find('small', class_='author').text
    dados_extraidos.append({
        "Alerta/Notícia": texto, 
        "Fonte": autor
    })

driver.quit()

# Salva os dados extraídos em CSV dentro da pasta data/
os.makedirs('data', exist_ok=True)
df = pd.DataFrame(dados_extraidos)
df.to_csv('data/dados_dinamicos_selenium.csv', index=False)

print(f"Sucesso! {len(dados_extraidos)} registros dinâmicos extraídos.")
print("Arquivo salvo em 'data/dados_dinamicos_selenium.csv'.")