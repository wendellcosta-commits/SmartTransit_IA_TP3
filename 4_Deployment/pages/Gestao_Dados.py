# Código criado com auxílio de I.A Google Gemini 2.5
import streamlit as st
import pandas as pd
from comum import carregar_noticias_raspadas

noticias = carregar_noticias_raspadas()

st.title("📥 Gestão de Dados")
st.divider()

# ==========================================
# DOWNLOAD DE DADOS
# ==========================================
st.markdown("### Exportar Dados Extraídos")
df_noticias = pd.DataFrame(noticias, columns=["Manchetes"])
csv_dados = df_noticias.to_csv(index=False).encode('utf-8')

st.download_button(
    label="📥 Baixar Dados (CSV)",
    data=csv_dados,
    file_name="noticias_smarttransit.csv",
    mime="text/csv"
)

st.divider()

# ==========================================
# UPLOAD DE ARQUIVOS
# ==========================================
st.header("📤 Integração de Novos Dados (Frota)")
st.write("Faça o upload de um arquivo CSV contendo a emissão de CO2 da frota.")

arquivo_upload = st.file_uploader("Escolha um arquivo CSV", type=['csv'])

if arquivo_upload is not None:
    try:
        df_upload = pd.read_csv(arquivo_upload)
        st.success("Arquivo carregado com sucesso!")
        st.dataframe(df_upload.head())
    except Exception as e:
        st.error(f"Erro ao ler o arquivo: {e}")
else:
    st.caption("Aguardando arquivo.")
    dados_amostra = {
        "ID_Linha": ["8000-10", "875A-10", "6450-10"],
        "Região_Atendida": ["Periferia Oeste", "Centro", "Zona Sul"],
        "Emissão_CO2_Est (kg/dia)": [850, 420, 1100]
    }
    st.dataframe(pd.DataFrame(dados_amostra), use_container_width=True)