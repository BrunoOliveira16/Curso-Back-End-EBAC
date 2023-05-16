## ✅ Como criar relacionamento entre tabelas
```
CREATE TABLE customer (
    id INTEGER PRIMARY KEY,
    value INTEGER,
);
```
```
CREATE TABLE contact (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER REFERENCES customer(id)
);
```

### Adicionando Relacionamento (FK) entre tabelas
```
ALTER TABLE table_name ADD CONSTRAINT <nome-da-constraint> FOREIGN KEY (column_1) REFERENCES customer (ID);

ALTER TABLE customer_order ADD CONSTRAINT fk_order_customer FOREIGN KEY (id) REFERENCES customer (email);
```