## Criando um Relatório Vendas e Lucros com Data Analytics com Power BI.


![Klabin003](https://github.com/user-attachments/assets/3b399c53-2885-423d-9de1-528e7fd00f53)



**Bootcamp Klabin - Excel e Power BI Dashboards**


---


# 🧭 Relatório de Vendas e Lucros — Projeto Data Analytics com Power BI (Simulado via Python)

![Mockup do Dashboard](assets/mockup_dashboard.png)

---

## 📘 Descrição do Projeto

Este projeto tem como objetivo **analisar dados de vendas e lucros corporativos** e construir um **relatório analítico completo**, aplicando conceitos de **Data Analytics**, **estatística descritiva** e **storytelling de dados**.

O diferencial deste repositório é que **todo o processo foi simulado sem a necessidade do Power BI instalado**, utilizando ferramentas abertas como **Python, SQL e Jupyter Notebooks** para reproduzir o comportamento de um dashboard analítico.

O projeto integra:
- Um fluxo **ETL completo (Extração, Transformação e Carga)**;
- Um conjunto de **dados simulados e realistas**;
- **Notebooks interativos** com análises estatísticas e simulação de dashboards;
- **Testes de validação de dados** e documentação técnica detalhada.

---

## 🎯 Objetivos Principais

- Demonstrar o processo de **criação de um relatório de vendas e lucros** com foco em experiência do usuário (UX);
- **Reproduzir o ambiente Power BI** em Python (gráficos, KPIs e insights);
- Aplicar princípios de **contraste, proporção áurea e segmentação de dados**;
- Documentar todas as etapas para que o projeto seja **didático e reprodutível**.

---

## 🏗️ Estrutura do Projeto 

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

## 🧰 Tecnologias Utilizadas

| Categoria | Tecnologia |
|------------|-------------|
| Linguagem principal | **Python 3.11+** |
| Visualização | **Matplotlib**, **Seaborn**, **Plotly** |
| Análise de dados | **Pandas**, **NumPy**, **SciPy** |
| Banco de dados | **SQLite / SQL padrão** |
| Relatórios | **Power BI (referência)** e **Jupyter Notebooks** |
| Versionamento | **Git e GitHub** |
| Documentação | **Markdown, Excel, DOCX** |

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

## 🚀 Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/Santosdevbjj/relatoVendasLucros.git
cd relatoVendasLucros

```

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



