## ✅ Introdução a relacionamentos entre tabelas em SQL
### Chaves Primárias e Chaves Compostas
FK ou Chave Estrangeira nada mais é do que a Chave Primária de uma tabela ‘colocada’ em outra tabela.
A Chave Estrangeira, além de conectar tabelas, tem mais esses propósitos:
- Ela impede que você adicione um valor inválido no ID de uma tabela
- Ela impede que você exclua um registro caso ele faça referência em outra tabela

PK ou Chave Primária é usada quando precisamos dos seguintes objetivos em uma tabela:
- Ter unicidade de um registro
- Que esse registro NÃO seja nulo
