# Código criado com auxílio de I.A Google Gemini 2.5
import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from comum import carregar_noticias_raspadas # Importa do seu arquivo comum

noticias = carregar_noticias_raspadas()

def toggle_dados():
    st.session_state['mostrar_dados'] = not st.session_state['mostrar_dados']

st.title("🚌 SmartTransit IA: Dashboard")
st.markdown("**ODS 11 & ODS 13** | Integração de Dados Urbanos e Análise de Sentimento")
st.divider()

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🌍 Panorama Climático (Agência Brasil)")
    st.metric(label="Total de Manchetes Analisadas", value=len(noticias))
    
    if len(noticias) > 1:
        texto_completo = " ".join(noticias)
        wordcloud = WordCloud(width=800, height=400, background_color='white', colormap='viridis').generate(texto_completo)
        fig, ax = plt.subplots(figsize=(10, 5))
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis('off')
        st.pyplot(fig)
    else:
        st.warning("Dados insuficientes para gerar a nuvem de palavras.")

with col2:
    st.subheader("⚙️ Painel de Controle")
    st.checkbox("Mostrar manchetes na íntegra", value=st.session_state['mostrar_dados'], on_change=toggle_dados)
    
    if st.session_state['mostrar_dados']:
        st.info("Últimas atualizações:")
        for noticia in noticias[:5]:
            st.write(f"- {noticia.strip()}")