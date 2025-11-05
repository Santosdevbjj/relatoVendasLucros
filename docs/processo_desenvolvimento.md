# Processo de Desenvolvimento — Relatório de Vendas e Lucros

---

## Etapa 1 — Entendimento do Desafio
Estudo do relatório original e da ementa de aulas.  
Análise de como aplicar princípios de Data Analytics e UX em dashboards financeiros.

---

## Etapa 2 — Preparação dos Dados
- Criação das tabelas `vendas`, `produtos`, `clientes` e `regiões`
- Limpeza de valores nulos
- Criação de métricas (Receita, Custo, Lucro)
- Geração da tabela final `vendas_tratadas.csv`

---

## Etapa 3 — Modelagem Analítica
Relacionamentos entre:
- **FatoVendas**
- **DimProdutos**
- **DimClientes**
- **DimRegioes**

Modelo Estrela criado e documentado em `/docs/diagrama_estrutura_pastas.png`.

---

## Etapa 4 — Construção do Dashboard (Simulado)
Como o Power BI não está instalado, os gráficos foram recriados em **Jupyter Notebook**:
- Gráfico de área (Receita × Tempo)
- Gráfico de barras (Lucro × Categoria)
- Matriz (Receita e Lucro × Região)

---

## Etapa 5 — Design e UX
Aplicados princípios de:
- Contraste e proporção áurea  
- Segmentação de dados  
- Botões de navegação (em conceito)

---

## Etapa 6 — Validação e Testes
Checklist de qualidade em `/tests/checklist_layout.md`  
Validação de consistência dos cálculos e formatações.

---

## Conclusão
O projeto demonstra domínio técnico e conceitual em Data Analytics, desde o ETL até a visualização,  
mesmo sem depender de ferramentas pagas.  
Pode ser facilmente expandido para Power BI, Looker ou Tableau.

---
