import streamlit as st

st.title("🤖 Planejamento de IA (LLMs)")
st.divider()

st.markdown("""
### 🧠 Como a Inteligência Artificial será aplicada no SmartTransit:

Nesta etapa do projeto (TP3), estruturamos a base de dados (APIs, Web Scraping Dinâmico via Selenium e arquivos CSV). Na próxima fase, esses dados alimentarão Modelos de Linguagem de Grande Escala (LLMs) como o **Claude** ou o **Gemini** para as seguintes tarefas:

#### 1. Classificação de Sentimentos em Tempo Real
Os dados coletados da Agência Brasil e via Web Scraping Dinâmico serão enviados ao LLM para classificar automaticamente a situação do ambiente/trânsito como:
* 🟢 **Fluido/Positivo**
* 🟡 **Atenção/Moderado**
* 🔴 **Crítico/Urgente**

#### 2. Assistente Q&A (Técnica de RAG)
O usuário não precisará ler as tabelas de emissão de CO2 ou procurar pelas manchetes. Implementaremos um chat na aplicação onde o usuário poderá perguntar: 
> *"Quais vias da Zona Sul estão impactadas pelas chuvas de hoje e qual a emissão estimada de CO2 dessas frotas?"* 

A IA lerá os nossos arquivos `csv` e `txt` como contexto e formulará uma resposta exata, sem inventar dados (evitando alucinações).

#### 3. Geração Automática de Relatórios
Usaremos a IA para cruzar os alertas climáticos com a infraestrutura das rotas de ônibus, gerando um parágrafo diário resumindo as ações necessárias pelos gestores públicos, focando diretamente nas metas do **ODS 11** e **ODS 13**.
""")

st.success("Toda a infraestrutura de Múltiplas Páginas, Roteamento, Cache e FastAPI já foi preparada para suportar estas implementações nas próximas etapas.")