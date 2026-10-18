import streamlit as st

st.set_page_config(page_title="SmartTransit IA | TP3", layout="wide")

if 'mostrar_dados' not in st.session_state:
    st.session_state['mostrar_dados'] = False

dashboard = st.Page("pages/Dashboard.py", title="Dashboard Ambiental", icon="🌍")
gestao = st.Page("pages/Gestao_Dados.py", title="Gestão de Dados", icon="📥")
visao_ia = st.Page("pages/Visao_IA.py", title="Visão de IA (LLMs)", icon="🤖") # <- NOVA PÁGINA AQUI

pg = st.navigation([dashboard, gestao, visao_ia]) # <- INCLUÍDA NA NAVEGAÇÃO AQUI

pg.run()