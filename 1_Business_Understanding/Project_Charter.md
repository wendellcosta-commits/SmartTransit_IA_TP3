# Project Charter: SmartTransit IA

## 1. Problema de Negócio e Pilar ESG
**Problema:** A ineficiência no roteamento do transporte público em grandes centros urbanos gera alta emissão de gases de efeito estufa (GEE) e cria "desertos de mobilidade" em áreas periféricas, dificultando o acesso da população a serviços básicos.
**Pilar ESG:** Ambiental (Redução de emissões) e Social (Democratização do acesso ao transporte).
**ODS Alinhado:** ODS 11 (Cidades e Comunidades Sustentáveis) e ODS 13 (Ação contra a mudança global do clima).

## 2. Metas e Indicadores de Sucesso
* **Metas:** Desenvolver um modelo preditivo para otimizar as frotas de ônibus com base na demanda em tempo real e sugerir rotas que minimizem a pegada de carbono.
* **Indicadores (KPIs):** 
  - Percentual estimado de redução de CO2 nas rotas otimizadas.
  - Aumento na cobertura de atendimento em bairros periféricos.

## 3. Público-Alvo e Stakeholders
* **Público-Alvo:** Gestores públicos de mobilidade urbana, prefeituras e secretarias de transporte.
* **Stakeholders:** População usuária do transporte público, empresas de ônibus e ONGs focadas em sustentabilidade urbana.

## 4. Escopo do Projeto

**O que está incluído (In-Scope):**
* O desenvolvimento de uma aplicação web interativa utilizando Python e Streamlit.
* A extração de dados públicos (via APIs e bases do IBGE/SPTrans) focados em mobilidade urbana e emissão de carbono.
* A integração de um modelo de Inteligência Artificial (LLM) para interpretar os dados e sugerir otimizações de rotas alinhadas ao ODS 11 e ODS 13.

**O que NÃO está incluído (Out-of-Scope):**
* A implementação física das rotas, alteração do trânsito ou compra de novos ônibus.
* O desenvolvimento de aplicativos de celular (Android/iOS) para o usuário final.
* Integração com sensores de IoT em tempo real nos pontos de ônibus nesta fase inicial (MVP).

## 5. Evolução do TP3 
**A arquitetura do sistema foi refatorada para suportar múltiplas páginas com estado de sessão (st.session_state). Além disso, uma API própria foi desenvolvida utilizando FastAPI para consultar os dados e o Selenium foi implementado para raspar alertas de trânsito em páginas dinâmicas (renderizadas via JavaScript), fortalecendo a base para a entrada da Inteligência Artificial.**