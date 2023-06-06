## ✅ Aula 1: Introdução ao módulo de agregação
Agregação de dados é o processo de resumir e apresentar dados em um formato mais compacto. Em SQL, isso é feito usando funções de agregação como SUM, AVG, MIN, MAX e COUNT. Essas funções são usadas em consultas SELECT para calcular valores agregados a partir de colunas de uma tabela.

Por exemplo, a consulta abaixo usa a função de agregação SUM para calcular o total de vendas por país:
```
SELECT
    country,
    SUM(sales) total_sales
FROM
    orders
GROUP BY
    country;
```

Nesta consulta, a cláusula GROUP BY agrupa as linhas da tabela orders por país. A função de agregação SUM é aplicada à coluna sales para cada grupo de linhas e calcula o total de vendas por país. O resultado final da consulta será uma tabela com duas colunas: country e total_sales. Cada linha da tabela representará um país e seu total de vendas.

Funções de agregação podem ser usadas com outras cláusulas SQL como WHERE, HAVING e ORDER BY para filtrar, agrupar e ordenar os resultados da consulta.