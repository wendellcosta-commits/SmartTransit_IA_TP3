# Data Summary Report - Esboço Inicial

Este documento relaciona as fontes de dados preliminares que alimentarão o dashboard de análise de sustentabilidade e infraestrutura urbana.

| Fonte de Dados | Tipo de Dado (Formato) | Objetivo de Uso na Aplicação |
| :--- | :--- | :--- |
| **Portal de Dados Abertos (IBGE / SPTrans)** | CSV / JSON | Fornecer a base de passageiros e rotas de transporte para cruzamento com metas do ODS 11. |
| **APIs Climáticas e Ambientais (ex: OpenWeather)** | API REST (JSON) | Coletar dados sobre clima para estimar o impacto na eficiência da frota e emissões de carbono (ODS 13). |
| **Modelos de Linguagem (LLM via API)** | Texto (Prompt/Response) | Processar os dados estruturados e gerar recomendações dinâmicas de roteamento e redução da pegada de carbono. |
| **Páginas Dinâmicas de Alertas (Web Scraping)** | CSV (Gerado via Selenium) | Teste de conceito simulando a captura de eventos de trânsito locais via JavaScript, para enviar como contexto ao LLM. |