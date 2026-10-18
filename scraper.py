# Código criado com auxílio de I.A Gemini 2.5

import os
import requests
from bs4 import BeautifulSoup

def extrair_noticias_ebc():
    print("A iniciar a extração de dados da Agência Brasil (EBC)...")
    
    # Cria a pasta 'data' na raiz do projeto se ela não existir
    os.makedirs('data', exist_ok=True)
    
    url = 'https://agenciabrasil.ebc.com.br/meio-ambiente'
    headers = {
        'User-Agent': 'SmartTransit_IA_Bot_Wendell_TP2/1.0'
    }
    
    try:
        resposta = requests.get(url, headers=headers, timeout=15)
        
        if resposta.status_code == 200:
            print("Página acedida com sucesso. A processar o HTML...")
            
            soup = BeautifulSoup(resposta.content, 'html.parser')
            links = soup.find_all('a')
            manchetes = []
            
            for link in links:
                texto = link.get_text(strip=True)
                href = link.get('href', '')
                
                # Filtra links válidos de notícias
                if texto and len(texto) > 20 and ('noticia' in href or 'meio-ambiente' in href):
                    if texto not in manchetes:
                        manchetes.append(texto)
            
            # Guarda as manchetes no ficheiro TXT
            caminho_arquivo = 'data/noticias_sustentabilidade.txt'
            with open(caminho_arquivo, 'w', encoding='utf-8') as f:
                for manchete in manchetes:
                    f.write(f"{manchete}\n")
                    
            print(f"Extração concluída! {len(manchetes)} manchetes foram guardadas em '{caminho_arquivo}'.")
            
        else:
            print(f"Erro ao aceder à página. Status Code: {resposta.status_code}")
            
    except Exception as e:
        print(f"Ocorreu um erro durante a extração: {e}")

if __name__ == "__main__":
    extrair_noticias_ebc()