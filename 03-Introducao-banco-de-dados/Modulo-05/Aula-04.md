## ✅ Aula 04: Offset e Limit no Postgres
A cláusula LIMIT do PostgreSQL é usada para limitar a quantidade de dados retornada pela instrução SELECT.
```
SELECT * FROM customer LIMIT 4;
```

Para selecionar ou retornar dados de uma determinada posição, usamos o LIMIT junto com o OFFSET
```
SELECT * FROM customer LIMIT 4 OFFSET 2;
```

### Resumo
Aprendemos um pouco como agregações funcionam, como ordenar e filtrar dados repetidos, além de aprender um pouco sobre o offset e limit para limitar informações no SQL.