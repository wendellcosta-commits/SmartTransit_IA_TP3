from fastapi import FastAPI
import pandas as pd
import os

app = FastAPI(title="API SmartTransit IA")

@app.get("/")
def home():
    return {"mensagem": "API SmartTransit IA está rodando!"}

@app.get("/dados-dinamicos")
def ler_dados_dinamicos():
    caminho = "data/dados_dinamicos_selenium.csv"
    if os.path.exists(caminho):
        df = pd.read_csv(caminho)
        return df.to_dict(orient="records")
    return {"erro": "Arquivo não encontrado. Execute o coleta_dinamica.py primeiro."}

@app.post("/enviar-alerta")
def receber_novo_alerta(alerta: str, fonte: str):
    return {
        "status": "sucesso", 
        "mensagem": "Novo alerta recebido e processado na fila.",
        "dado_recebido": {"Alerta/Notícia": alerta, "Fonte": fonte}
    }