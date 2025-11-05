-- Script SQL de Transformações e Métricas
-- Autor: Sérgio Santos

-- Exemplo para SQLite ou PostgreSQL

CREATE VIEW vw_vendas_lucros AS
SELECT
    v.ID_Venda,
    v.Data,
    p.Nome_Produto,
    p.Categoria,
    c.Nome_Cliente,
    c.Segmento,
    r.Nome_Regiao,
    v.Quantidade,
    v.Preco_Unitario,
    v.Custo_Unitario,
    (v.Quantidade * v.Preco_Unitario) AS Receita,
    (v.Quantidade * v.Custo_Unitario) AS Custo,
    ((v.Quantidade * v.Preco_Unitario) - (v.Quantidade * v.Custo_Unitario)) AS Lucro
FROM vendas v
JOIN produtos p ON v.ID_Produto = p.ID_Produto
JOIN clientes c ON v.ID_Cliente = c.ID_Cliente
JOIN regioes r ON v.ID_Regiao = r.ID_Regiao;
