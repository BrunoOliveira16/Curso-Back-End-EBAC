## 📌 Aula 01: Estratégias para otimizar a leitura de banco de dados
Como procurar por algum assunto em um livro grande?

Ou para os mais velhos como procurar um telefone na lista telefônica?

Índices nos bancos de dados são utilizados para facilitar a busca de informações em uma tabela com o menor número possível de operações de leituras, tornado assim a busca mais rápida e eficiente.

Existem várias estratégias para otimizar a leitura de um banco de dados. Algumas delas incluem:

- Reescrever a consulta de forma a percorrer um menor caminho, por exemplo, utilizando campos indexados na cláusula WHERE.
- Alterar a ordem de leitura das tabelas de forma a ler sempre a tabela com menos registros.
- Induzir o banco de dados a sempre utilizar um índice.
- Indexar novos campos se necessário.

<br>

### Otimizando a performance de um banco de dados
### Arquitetura
- Read Replica (AWS)
- Multi-AZ (Amazon RDS) - Failover Support
- Master Slave Replication

### Banco de Dados
- Indexes

As réplicas de leitura do Amazon RDS aperfeiçoam a performance e a durabilidade para instâncias de banco de dados (DB) do Amazon RDS. Elas facilitam o aumento da escala na horizontal de maneira elástica além dos limites de capacidade de uma única instância de DB para workloads de banco de dados com uso intenso de leitura. Você pode reduzir a carga na instância de banco de dados primária roteando as consultas de leitura dos aplicativos para a réplica de leitura .