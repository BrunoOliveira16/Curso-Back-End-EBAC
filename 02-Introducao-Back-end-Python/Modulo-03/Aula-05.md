## 📌 Aula 05: Pontos positivos e Negativos de índices 
### Vantagens e Desvantagens de Índices
Vantagens
- Melhoria de Performance
- Pode Trazer dados especificos mais rápidos

Desvantagens
- Piora a Performance de Escritas em BD
- Aumenta o Consumo de Espaço

<br>

Os índices podem trazer muitas vantagens para o desempenho de um banco de dados. Eles permitem que o banco de dados localize rapidamente as linhas que correspondem aos critérios de uma consulta, acelerando a execução da consulta. Isso pode ser especialmente útil quando a tabela tem muitas linhas ou quando a consulta é complexa.

No entanto, os índices também têm algumas desvantagens. Eles ocupam espaço em disco e podem afetar a performance de operações de escrita, como inserções, atualizações e exclusões. Isso ocorre porque o banco de dados precisa manter os índices atualizados sempre que os dados são modificados.

Além disso, o uso indiscriminado de índices pode ter um impacto negativo na performance do banco de dados. É importante identificar os campos que são mais utilizados em consultas e criar índices apenas nesses campos. Também é importante monitorar regularmente o desempenho do banco de dados e ajustar os índices conforme necessário.