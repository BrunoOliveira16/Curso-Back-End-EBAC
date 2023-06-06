-----------------------DDL-----------------------

--product
CREATE TABLE product (
    product_id serial NOT NULL,
    "name" varchar(25) NOT NULL,
    created_date timestamp NOT NULL DEFAULT now(),
    CONSTRAINT product_pkey PRIMARY KEY (product_id)
);

--stock
CREATE TABLE stock (
    id serial NOT NULL,
    product_id int4 NOT NULL,
    quantity int4 NOT NULL,
    CONSTRAINT stock_pkey PRIMARY KEY(id)
);


-----------------------DML-----------------------

--1
INSERT INTO product (name) values ('celular');
INSERT INTO product (name) values ('livro');
INSERT INTO product (name) values ('tablet');
INSERT INTO product (name) values ('notebook');
INSERT INTO product (name) values ('roteador');

INSERT INTO stock (product_id, quantity) values (1, 5);
INSERT INTO stock (product_id, quantity) values (2, 3);
INSERT INTO stock (product_id, quantity) values (3, 0);
INSERT INTO stock (product_id, quantity) values (4, 1);
INSERT INTO stock (product_id, quantity) values (5, 0);


--2
SELECT
    name product_name,
    stock.quantity product_stock
FROM
    product
INNER JOIN stock USING (product_id)
GROUP BY
    product_name,
    product_stock
ORDER BY product_stock DESC;

--3
SELECT
    SUM(quantity) total_stock
FROM
    stock;


