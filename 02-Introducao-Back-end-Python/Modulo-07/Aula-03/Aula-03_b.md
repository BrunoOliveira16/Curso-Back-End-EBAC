## 📝 Aula 02: Construindo modelos de entidade com Django Models e como utilizar querysets para manipulação de dados
### Como utilizar querysets para manipulação de dados
QuerySets são uma das principais ferramentas para manipulação de dados no Django. Eles permitem que você crie, leia, atualize e exclua registros no banco de dados usando uma sintaxe intuitiva baseada em Python.

Para criar um novo registro no banco de dados, você pode usar o método ``create`` do gerenciador de objetos do modelo. Por exemplo, para criar um novo autor, você pode fazer o seguinte:

```
author = Author.objects.create(name='J.K. Rowling')
```

Para ler registros do banco de dados, você pode usar vários métodos do gerenciador de objetos, como ``all``, ``get``, ``filter`` e ``exclude``. Por exemplo, para recuperar todos os autores do banco de dados, você pode fazer o seguinte:

```
authors = Author.objects.all()
```

Para atualizar um registro existente, você pode modificar seus atributos e chamar o método ``save`` para persistir as alterações no banco de dados. Por exemplo, para atualizar o nome de um autor, você pode fazer o seguinte:

```
author = Author.objects.get(name='J.K. Rowling')
author.name = 'Joanne Rowling'
author.save()
```

Para excluir um registro do banco de dados, você pode chamar o método delete em um objeto de modelo ou em um QuerySet. Por exemplo, para excluir um autor específico, você pode fazer o seguinte:

```
author = Author.objects.get(name='Joanne Rowling')
author.delete()
```

Além dessas operações básicas, os QuerySets oferecem muitos outros recursos avançados, como ordenação, limitação, agregação e muito mais. Você pode encadear vários métodos juntos para criar consultas complexas e manipular os dados do banco de dados de maneira eficiente.

<br>

Aqui estão alguns exemplos adicionais de como usar QuerySets para manipular dados no Django:

- ``Filtragem``: Você pode usar o método ``filter`` para filtrar os registros do banco de dados com base em critérios específicos. Por exemplo, para recuperar todos os livros publicados por um determinado autor, você pode fazer o seguinte:
```
books = Book.objects.filter(author__name='J.K. Rowling')
```

- ``Ordenação``: Você pode usar o método ``order_by`` para ordenar os registros do banco de dados com base em um ou mais campos. Por exemplo, para recuperar todos os livros ordenados por título, você pode fazer o seguinte:
```
books = Book.objects.order_by('title')
```

- ``Limitação``: Você pode usar os métodos ``first``, ``last`` e ``[:n]`` para limitar o número de registros retornados pelo banco de dados. Por exemplo, para recuperar apenas o primeiro livro de um determinado autor, você pode fazer o seguinte:
```
book = Book.objects.filter(author__name='J.K. Rowling').first()
```

- ``Agregação``: Você pode usar os métodos ``annotate`` e ``aggregate`` para realizar cálculos agregados nos registros do banco de dados. Por exemplo, para calcular o número médio de páginas dos livros de um determinado autor, você pode fazer o seguinte:
```
from django.db.models import Avg

result = Book.objects.filter(author__name='J.K. Rowling').aggregate(Avg('num_pages'))
average_num_pages = result['num_pages__avg']
```

Esses são apenas alguns exemplos de como usar QuerySets para manipular dados no Django. Os QuerySets oferecem muitos outros recursos avançados que permitem que você crie consultas complexas e manipule os dados do banco de dados de maneira eficiente.