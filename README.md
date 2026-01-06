## Otimização de Margens e Diagnóstico de Vendas: Projeto Data Analytics
​ Foco: Business Intelligence & Engenharia de Dados


![Klabin003](https://github.com/user-attachments/assets/3b399c53-2885-423d-9de1-528e7fd00f53)



**Bootcamp Klabin - Excel e Power BI Dashboards**


---


# 🧭 Relatório de Vendas e Lucros — Projeto Data Analytics com Power BI (Simulado via Python) 

![Mockup do Dashboard](assets/mockup_dashboard.png)

---

# ​1. 🎯 Problema de Negócio

​A falta de visibilidade centralizada sobre os indicadores de performance (KPIs) de vendas e lucros impedia a diretoria de identificar quais regiões e categorias de produtos estavam drenando a margem da empresa. 

O desafio era transformar dados brutos e dispersos em um diagnóstico acionável para reduzir a ineficiência operacional e maximizar o ROI por categoria.

## ​2. 💡 Contexto e Estratégia da Solução

​Este projeto simula um ambiente corporativo real onde, por limitações de licenciamento ou infraestrutura, o analista deve entregar resultados de BI (Business Intelligence) utilizando ferramentas de código aberto.

​A estratégia foi construir um ecossistema que espelha o fluxo do Power BI, mas utilizando Python e SQL, garantindo que a lógica de negócio seja independente da ferramenta proprietária.

## ​🛠️ Framework de Desenvolvimento

**​Baseline:** O processo anterior baseava-se em análises manuais e descentralizadas.
​ETL & Limpeza: Tratamento de nulos e padronização de tipos de dados via Pandas.
​EDA (Exploratória): Validação de hipóteses sobre sazonalidade e comportamento de clientes.

​**Modelagem de Dados:** Estruturação em esquema Estrela (Star Schema) com tabelas Fato e Dimensão.

**​Storytelling:** Tradução de métricas técnicas em insights de negócio.

## ​3. 🧠 Decisões Técnicas:

​**Por que Python em vez de apenas Power BI?**

**​Portabilidade:** A lógica de ETL em Python (src/etl_limpeza_dados.py) permite que o pipeline seja migrado para qualquer nuvem ou banco de dados.

​**Escalabilidade:** O uso de SQL para agregações (src/etl_transformacoes.sql) garante performance em volumes de dados maiores que os suportados por planilhas comuns.

**​Custo Zero:** Demonstra capacidade de entregar valor sem depender de custos extras de licenças Pro/Premium.

​4. 📈 Insights e Resultados de Negócio

​A análise não gerou apenas gráficos, mas direcionamentos estratégicos:
​Concentração de Lucro: A região Sudeste detém 42% das vendas, mas 47% do lucro, indicando uma eficiência logística superior que deve ser replicada no Sul.

**​Alavanca de Margem:** Produtos Eletrônicos apresentam margem >20%. Recomendação: Aumentar o investimento em Ads para esta categoria.

**​Retenção:** Clientes recorrentes lucram 18% a mais. Ação: Implementar programa de fidelidade.





---

## 🏗️ Estrutura do Repositório

<img width="953" height="1858" alt="diagrama_estrutura_pastas" src="https://github.com/user-attachments/assets/cd5b63f0-9ec9-4d9e-865a-68e15adb40b5" /> 

---


---

## 📂 Descrição dos Arquivos

### 📁 **assets/**
- **mockup_dashboard.png** — Imagem ilustrativa do painel de vendas e lucros (simulação do Power BI).

---

### 📁 **data/**
- **vendas.csv** — Fato principal com registros de vendas, quantidades e preços unitários.  
- **produtos.csv** — Dimensão contendo produtos e categorias.  
- **clientes.csv** — Dimensão com informações demográficas e de segmento.  
- **regioes.csv** — Dimensão geográfica.  
- **dicionario_dados.xlsx** — Dicionário detalhado de todas as colunas e tipos de dados.

---

### 📁 **src/**
- **etl_limpeza_dados.py** — Script Python para limpeza e padronização dos dados.  
- **etl_transformacoes.sql** — Script SQL para criação de tabelas analíticas e agregações.  
- **export_powerquery_steps.txt** — Equivalente textual ao Power Query (documentação dos passos de transformação).

---

### 📁 **notebooks/**
- **analise_vendas_lucros.ipynb** — Análise principal dos indicadores de vendas, margens e tendências.  
- **simulacao_dashboard_sem_powerbi.ipynb** — Simulação visual do dashboard utilizando Plotly e Matplotlib.  
- **exploracao_estatistica.ipynb** — Estudo exploratório dos dados com correlações e distribuições.

---

### 📁 **docs/**
- **RelatorioCriativo.pbix** — Relatório original criado no Power BI (referência do projeto).  
- **ProjetoDataAnalyticsPowerBi.docx** — Documento explicativo do desafio e metodologia.  
- **ementa_aulas.md** — Ementa das aulas que inspiraram o projeto.  
- **analise_estatistica.md** — Detalhamento das análises estatísticas aplicadas.  
- **processo_desenvolvimento.md** — Guia de desenvolvimento e integração das etapas.  
- **guia_didatico_sem_powerbi.md** — Explicação passo a passo de como reproduzir o dashboard sem Power BI.  
- **diagrama_estrutura_pastas.png** — Diagrama visual da estrutura do repositório.

---

### 📁 **tests/**
- **verificacao_dados.md** — Checklist de integridade e consistência dos dados.  
- **checklist_layout.md** — Itens de verificação do layout e UX do dashboard.  
- **relatorio_ajustes.xlsx** — Relatório de ajustes realizados durante o desenvolvimento.

---


## 6. 🛠️ Tecnologias Utilizadas

• ​Linguagem: Python 3.11 (Pandas, NumPy, SciPy) 

​• Visualização: Plotly (Interatividade), Seaborn (Estatística) 

• ​Banco de Dados: SQL (Agregações analíticas)

• ​BI: Power BI (Referência de Layout e UX)


---

## 💻 Requisitos do Sistema

| Tipo | Requisito |
|------|------------|
| **Sistema Operacional** | Windows 10+, Linux ou macOS |
| **Processador** | Dual-core 2.0 GHz ou superior |
| **Memória RAM** | Mínimo 8 GB |
| **Armazenamento** | 2 GB livres |
| **Software** | Python 3.11+, JupyterLab, Git, Excel |

---



---

## ​7. 🚀 Como Executar e Validar

​Clone: git clone https://github.com/Santosdevbjj/relatoVendasLucros.git

​Ambiente: Crie sua venv e instale as dependências via pip install -r requirements.txt.

​Execução: Explore o notebook notebooks/simulacao_dashboard_sem_powerbi.ipynb para ver a simulação do dashboard.

## ​8. 🔮 Próximos Passos

​[ ] Implementar um modelo de Previsão de Vendas (Time Series) para o próximo trimestre.
​[ ] Automatizar o pipeline de dados via GitHub Actions.
​[ ] Desenvolver um bot no Telegram para envio de alertas de KPIs diários.




---



2️⃣ **Criar ambiente virtual**

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

3️⃣ **Instalar dependências**

pip install pandas numpy matplotlib seaborn plotly jupyter scipy

4️⃣ **Executar as análises**

Abra o Jupyter:

jupyter notebook

E explore:

notebooks/analise_vendas_lucros.ipynb

notebooks/simulacao_dashboard_sem_powerbi.ipynb

notebooks/exploracao_estatistica.ipynb



---

🧪 **Testes e Validação**

A pasta tests/ contém os scripts e planilhas que asseguram:

Integridade dos dados (chaves e valores válidos);

Validação de layout e design;

Registro de ajustes realizados.



---

🧭 **Como Criar o Dashboard sem Power BI**

Mesmo sem o Power BI Desktop instalado, é possível:

1. Utilizar Python + Plotly para criar gráficos interativos;


2. Reproduzir os passos do Power Query com pandas e SQL;


3. Construir painéis dinâmicos em Jupyter Notebooks;


4. Exportar resultados para .html ou .png com visual similar ao Power BI.



Consulte:
📄 docs/guia_didatico_sem_powerbi.md


---

📊 **Principais Insights do Projeto**

Região Sudeste concentra 42% das vendas e 47% do lucro total.

Produtos Eletrônicos e Acessórios possuem margem superior a 20%.

Clientes recorrentes aumentam o lucro médio em até 18%.

As vendas apresentam padrão sazonal crescente no 2º semestre.



---

🧠 **Conclusão**

Este projeto sintetiza o poder da análise de dados aplicada à tomada de decisão empresarial, mesmo sem o uso de ferramentas proprietárias.
O processo reforça o domínio técnico em ETL, estatística, design de dashboards e governança de dados.


---

✨ **Autor**

Sérgio Santos



---

📚 **Licença**

Este projeto é distribuído sob a licença MIT License — uso livre para fins educacionais e profissionais.


---

**Contato:**

[![Portfólio Sérgio Santos](https://img.shields.io/badge/Portfólio-Sérgio_Santos-111827?style=for-the-badge&logo=githubpages&logoColor=00eaff)](https://santosdevbjj.github.io/portfolio/)
[![LinkedIn Sérgio Santos](https://img.shields.io/badge/LinkedIn-Sérgio_Santos-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/santossergioluiz) 


---



