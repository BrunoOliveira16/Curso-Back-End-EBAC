## ✅ Aula 02: Agrupando dados utilizando o Group By e Having
A cláusula ``GROUP BY`` agrupa linhas baseado em semelhanças entre elas.

O ``GROUP BY`` é útil quando queremos agrupar e calcular informações dentro da nossa tabela:
```
SELECT customer_id FROM payment GROUP BY customer_id;
```

No exemplo anterior ``GROUP BY`` removeu os dados duplicados da nossa tabela.

Podemos utilizar o ``GROUP BY`` para agregar dados, neste caso podemos utilizar o SUM().

Podemos calcular o valor total de cada pedido utilizando o ``Group By`` juntamente com a função SUM.
```
SELECT customer_id SUM(amount) FROM payment GROUP BY customer_id;
```

### Group By com JOIN
```
SELECT 
    first_name ||''|| last_name full_name,
    SUM(amount) amount
FROM 
    payment 
INNER JOIN customer USING(customer_id)
GROUP BY 
    full_name
ORDER BY amount;
```

### Having
Podemos utilizar o Having para filtrar grupos ou uma agregação.

Diferente do Where onde utilizamos para filtrar dados individuais.

#### Group By e Having
```
SELECT 
    customer_id,
    SUM(amount)
FROM 
    payment 
GROUP BY 
    customer_id
HAVING
    SUM(amount)>200;
```