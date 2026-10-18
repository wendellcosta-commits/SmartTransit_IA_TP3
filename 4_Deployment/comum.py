import streamlit as st
import pandas as pd

@st.cache_data
def carregar_noticias_raspadas():
    try:
        with open('data/noticias_sustentabilidade.txt', 'r', encoding='utf-8') as f:
            return f.readlines()
    except FileNotFoundError:
        return ["Nenhum dado encontrado."]