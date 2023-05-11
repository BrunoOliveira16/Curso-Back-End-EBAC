Nesse exercício, vamos criar as tabelas de cliente, estoque e produto,
utilize os desenhos que fizemos no lucidchart como referência:

Script para tabela cliente dentro do schema "store":
```
CREATE TABLE "store".customer1 (
    id SERIAL PRIMARY KEY,
    name varchar(30) NOT NULL,
    email varchar(50) NOT NULL,
    cpf text NOT NULL UNIQUE
);
```
Script para tabela produtos dentro do schema "store":
```
CREATE TABLE "store".products1 (
    cod_product SERIAL PRIMARY KEY,
    name varchar(30) NOT NULL UNIQUE,
    description varchar(50) NOT NULL,
    value numeric NOT NULL
);
```

Script para tabela estoque dentro do schema "store":
```
CREATE TABLE "store".stock (
    cod_stock SERIAL PRIMARY KEY,
    location varchar(30) NOT NULL,
);
```