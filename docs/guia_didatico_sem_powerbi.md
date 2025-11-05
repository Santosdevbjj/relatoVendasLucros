# Guia Didático — Criando o Dashboard sem Power BI

Este guia mostra como **analisar e visualizar os dados** do projeto *Relatório de Vendas e Lucros* **sem precisar instalar o Power BI**.

---

## 1️⃣ Preparar o Ambiente

Instale as bibliotecas necessárias:

```bash
pip install pandas numpy matplotlib seaborn plotly jupyter

---



---

2️⃣ Executar os Notebooks

Abra o arquivo:

/notebooks/simulacao_dashboard_sem_powerbi.ipynb

Ele recria as principais visualizações do Power BI usando:

Plotly Express para gráficos interativos

pandas para cálculos de lucro e receita



---

3️⃣ Métricas Calculadas

Métrica	Fórmula	Descrição

Receita	Quantidade × Preço_Unitário	Valor total vendido
Custo	Quantidade × Custo_Unitário	Custo total
Lucro	Receita - Custo	Margem bruta de venda



---

4️⃣ Gráficos Principais

Gráfico de área: evolução da receita por mês

Gráfico de barras: lucro por categoria de produto

Matriz (tabela): resumo por região

Indicadores (KPIs): total de vendas, lucro total, margem média



---

5️⃣ Ferramentas Alternativas ao Power BI

Alternativa	Descrição

Plotly Dash	Interface web interativa em Python
Google Looker Studio	BI online gratuito
Tableau Public	Ferramenta gratuita de visualização
Excel Power Query	Pode simular parte do processo ETL



---

6️⃣ Conclusão

Mesmo sem o Power BI, é possível desenvolver um projeto completo e didático de Data Analytics, aplicando princípios de:

Design analítico



---



Experiência do usuário

Storytelling de dados



---
