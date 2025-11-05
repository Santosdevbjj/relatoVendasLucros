# Testes de Verificação de Dados

## Objetivo
Garantir que os dados utilizados no projeto estejam íntegros, completos e consistentes.

---

### 1. Estrutura dos Arquivos
| Arquivo | Colunas Esperadas | Status |
|----------|-------------------|---------|
| vendas.csv | id_venda, id_cliente, id_produto, id_regiao, data_venda, quantidade, preco_unitario | ✅ |
| produtos.csv | id_produto, nome_produto, categoria | ✅ |
| clientes.csv | id_cliente, nome_cliente, idade, segmento | ✅ |
| regioes.csv | id_regiao, nome_regiao | ✅ |

---

### 2. Integridade Referencial
- Todas as chaves estrangeiras de `vendas.csv` existem nas tabelas de dimensão correspondentes → **OK**

---

### 3. Consistência Numérica
- Quantidades e preços positivos → **OK**  
- Lucro calculado corretamente → **OK**

---

### 4. Dados Faltantes
- 0 registros nulos → **OK**

---

### 5. Conclusão
Os dados estão prontos para uso em análises e visualizações.
