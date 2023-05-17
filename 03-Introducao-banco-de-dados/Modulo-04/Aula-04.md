## ✅ Como unir dados de diferentes tabelas utilizando o SQL Join
Usamos o comando Joins para combinar dados de 2 tabelas.

Normalmente usamos como referencia as chaves primárias e secundárias:
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
INNER JOIN basket_b
    ON fruit_a = fruit_b;
```

<img src="./assets/img-09.jpg">

<br>

### Como unir dados de diferentes tabelas utilizando o SQL Left Join
Também usamos o Left Join para combinar dados de 2 tabelas porém invertemos a tabela de referência:
```
SELECT
    a,
    fruit_a,
    b,
    fruit_b
FROM
    basket_a
LEFT JOIN basket_b
    ON fruit_a = fruit_b;
```

<img src="./assets/img-10.jpg">