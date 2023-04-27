## 📌 Introdução a Servidores de Aplicação

## O Que é um Application Server?
Um servidor de aplicação fornece serviços de infraestrutura para aplicações. Ele gerencia o acesso a recursos como bancos de dados e mensagens, e lida com questões de escalabilidade e failover. Isso permite que os desenvolvedores se concentrem na lógica de negócios da aplicação em vez de se preocupar com questões de infraestrutura.

Um servidor de aplicação pode ser útil para sua aplicação de várias maneiras. Ele pode ajudar a gerenciar o acesso a recursos como bancos de dados e mensagens, permitindo que sua aplicação se comunique de maneira eficiente com esses recursos. Ele também pode lidar com questões de escalabilidade e failover, garantindo que sua aplicação possa lidar com altos volumes de tráfego e continuar funcionando mesmo em caso de falhas. Além disso, um servidor de aplicação pode fornecer serviços adicionais como segurança, gerenciamento de transações e balanceamento de carga.

**Exemplo:** Ao invés do python (flask | django) servir requisições diretamente da camada de negócio da sua aplicação, o application server promove esse acesso oferecendo diversas formas de comunicação adicionais, além de ser mais otimizado e performático.

<br>

## Application Servers disponíveis no mercado
Temos diversos applications servers disponíveis para Python sendo eles:
- https://www.uvicorn.org/
- https://uwsgi-docs.readthedocs.io/en/latest/#
- https://wsgi.readthedocs.io/en/latest/index.html

### O que é o WSGI (Web Service Gateway Interface)?
É uma especificação (https://www.python.org/dev/peps/pep-3333/) de como servidores web precisam se comunicar com aplicações web e como elas podem ser encadeados para processar uma solicitação.

### Principais diferenças entre Applications Servers

| Assíncrono | Não assíncrono |
| --- | --- |
| https://www.uvicorn.org/ | https://wsgi.readthedocs.io/en/latest/ |
| https://uwsgi-docs.readthedocs.io/en/latest/ | Implementa o PEP-3333 ( https://peps.python.org/pep-3333/ )