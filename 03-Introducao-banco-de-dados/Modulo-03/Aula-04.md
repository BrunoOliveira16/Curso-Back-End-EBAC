## ✅ Filtrando dados complexos utilizando subqueries
Podemos usar o WHERE ``<campo>`` IN passando uma lista de valores para filtrarmos:
```
SELECT * FROM "store".customer WHERE name IN ('Bruno Oliveira', 'Bianca');
```

<img src="./assets/img-09.jpg">

<br>

Para nosso exemplo, vamos primeiro inserir uma coluna nova na tabela customer_order:
```
ALTER TABLE "store".customer_order ADD user_email_order varchar(30);
```
<img src="./assets/img-06.jpg">

<br><hr>

Agora vamos inserir alguns dados na tabela customer_order:
```
INSERT INTO "store".customer_order (value, user_email_order) VALUES (30, 'bruno@email.com');
```
<img src="./assets/img-07.jpg">

<br><hr>

E agora podemos usar SELECTS dentro de outros SELECTS, note que para essa busca estamos utilizando o email da tabela customer para buscar dentro da tabela customer_order.
```
SELECT * FROM "store".customer_order WHERE user_email_order IN (
    SELECT email FROM "store".customer
);
```

<img src="./assets/img-08.jpg">

<br>

### Resumo
Aprendemos um pouco como manipular dados de um banco de dados e quais são as principais funções do DML como:
- SELECT, INSERT, DELETE E UPDATE
- WHERE, IN
- SELECT dentro de outro SELECT