## ✅ Aula 03: Removendo Dados Repetidos com Distinct
Para remover dados duplicados em SQL, utilizamos comando DISTINCT seguido das colunas que queremos remover dados duplicados:
```
SELECT DISTINCT customer_id FROM customer;
```

### Ordenando Campos com Order By
Quando você consulta dados de uma tabela, a instrução SELECT retorna linhas em uma ordem não especificada. Para classificar as linhas do conjunto de resultados, você usa a cláusula ORDER BY na instrução SELECT.
```
SELECT * FROM customer ORDER BY name ASC ou DESC;
```
- DESC = Decrescente
- ASC = Crescente

```
SELECT * FROM customer ORDER BY name ASC ou DESC;
```
- DESC = Decrescente
- ASC = Crescente

OBS: ASC é a opção default caso não especifiquemos o tipo de ordenação