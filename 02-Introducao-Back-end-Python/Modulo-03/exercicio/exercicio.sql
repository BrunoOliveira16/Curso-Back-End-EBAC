------------------ CRIANDO TABELA E REALIZANDO CONSULTA ------------------------

CREATE TABLE clientes(id SERIAL, nome_cliente TEXT);

INSERT INTO clientes(nome_cliente) SELECT 'Bruno' FROM generate_series(1, 250000);

EXPLAIN ANALYZE SELECT * FROM clientes WHERE ID = 10;


------------------------ CRIANDO INDICE E NOVA CONSULTA ------------------------

CREATE INDEX clientes_idx ON clientes(ID);

EXPLAIN ANALYZE SELECT * FROM clientes WHERE ID = 10;