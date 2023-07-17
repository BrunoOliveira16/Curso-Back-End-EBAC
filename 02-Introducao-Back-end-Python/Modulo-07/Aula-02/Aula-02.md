## 📝 Aula 02: Construindo modelos de entidade com Django Models e como utilizar querysets para manipulação de dados
### Criando um modelo no Django ORM
Para criar um modelo no Django ORM, você precisa definir uma classe que herda de ``models.Model`` dentro do arquivo ``models.py`` de sua aplicação Django. Cada atributo da classe representa um campo na tabela do banco de dados e deve ser instanciado com um tipo de campo apropriado, como ``models.CharField`` para campos de texto ou ``models.IntegerField`` para campos numéricos.

Aqui está um exemplo de como criar um modelo simples para representar uma pessoa com nome e idade:

```
from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
```

Depois de definir o modelo, você precisa executar o comando ``makemigrations`` para criar as migrações necessárias e, em seguida, o comando ``migrate`` para aplicar as migrações e criar a tabela no banco de dados.

```
python manage.py makemigrations
python manage.py migrate
```

Isso é tudo que você precisa fazer para criar um modelo no Django ORM. Você pode então usar o modelo para criar, ler, atualizar e excluir registros no banco de dados.

<br>

### Migrações de banco de dados
Migrações de banco de dados são uma maneira de gerenciar alterações na estrutura do banco de dados ao longo do tempo. Elas permitem que você modifique a estrutura do banco de dados de maneira controlada e consistente, sem perder dados existentes.

No contexto do Django ORM, quando você cria ou modifica um modelo, o Django gera automaticamente migrações para refletir essas alterações na estrutura do banco de dados. Essas migrações são armazenadas em arquivos Python dentro da pasta migrations de sua aplicação Django.

Para aplicar as migrações e atualizar a estrutura do banco de dados, você precisa executar o comando migrate. Esse comando verifica quais migrações ainda não foram aplicadas e as executa em ordem para atualizar a estrutura do banco de dados.

As migrações são uma parte importante do desenvolvimento com o Django ORM, pois permitem que você evolua a estrutura do banco de dados de maneira segura e controlada.

<br>

### Prática - Criando e aplicando migrações para o modelo Post no Django ORM
Para criar um pacote de modelo que inclua o modelo ``Post`` definido, sigua os seguintes passos:

1. Crie uma nova pasta dentro da pasta da sua aplicação Django(``mysite``) para armazenar seus modelos. Com o nome de ``models``.

2. Dentro da pasta ``models``, crie um novo arquivo chamado ``__init__.py`` e deixe-o vazio.

3. Crie um novo arquivo chamado ``post.py`` dentro da pasta ``models``, dentro do arquivo ``post.py`` o código abaixo deste passo a passo foi desenvolvido.

4. Abra o arquivo ``__init__.py`` e adicione a seguinte linha de importação: ``from .post import Post``.

5. Execute o comando ``makemigrations`` para criar as migrações necessárias para o novo modelo: ``python manage.py makemigrations``.

6. Execute o comando ``migrate`` para aplicar as migrações e atualizar a estrutura do banco de dados: ``python manage.py migrate``.

> Ao executar o comando migrate, você aplica essas migrações ao banco de dados, atualizando sua estrutura para refletir as alterações feitas nos modelos. Isso permite que você evolua a estrutura do banco de dados ao longo do tempo sem perder dados existentes.

Essas etapas são uma parte importante do desenvolvimento com o Django ORM, pois permitem que você gerencie alterações na estrutura do banco de dados de maneira segura e controlada.

Depois de seguir esses passos, você terá criado um pacote de modelo que inclui o modelo ``Post`` e aplicado as migrações necessárias para atualizar a estrutura do banco de dados.

<br>

 > Código de post.py
```
from django.db import models
from django.contrib.auth.models import User

STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_post')
    update_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.ImageField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
```

Agora, vamos analisar o código fornecido para entender alguns dos conceitos importantes utilizados nele:

- O modelo Post herda de models.Model, o que significa que ele é um modelo Django que pode ser usado para interagir com o banco de dados.

- O modelo define vários campos, como title, slug, author, etc., que representam as colunas na tabela do banco de dados. Cada campo é instanciado com um tipo de campo apropriado, como models.CharField para campos de texto ou models.DateTimeField para campos de data/hora.

- O campo author é um campo de chave estrangeira que cria uma relação entre o modelo Post e o modelo User do Django. Isso significa que cada postagem está associada a um usuário específico que é o autor da postagem.

- O campo status é um campo de imagem com opções definidas pela tupla STATUS. Isso significa que o valor desse campo deve ser um dos valores definidos em STATUS.

- A classe interna Meta define opções adicionais para o modelo, como a ordem padrão dos registros quando eles são recuperados do banco de dados.

- O método especial __str__ define como os objetos desse modelo serão representados como strings. Nesse caso, ele retorna o título da postagem.

- As etapas 5 e 6 do passo a passo são importantes porque permitem que você crie e aplique migrações para atualizar a estrutura do banco de dados de maneira controlada e consistente. Quando você cria ou modifica um modelo, o Django gera automaticamente migrações para refletir essas alterações na estrutura do banco de dados. Essas migrações são armazenadas em arquivos Python dentro da pasta migrations de sua aplicação Django.

<br>

### Modelos Abstratos em Django
Modelos abstratos no Django são uma maneira de definir campos e comportamentos comuns que podem ser reutilizados por vários modelos diferentes. Eles funcionam como uma espécie de modelo base que pode ser herdado por outros modelos, mas não são criados como tabelas separadas no banco de dados.

Para criar um modelo abstrato, você precisa definir uma classe que herda de models.Model e incluir a opção abstract = True na classe Meta interna. Aqui está um exemplo de como criar um modelo abstrato chamado BaseModel que define campos comuns para data de criação e data de atualização:

```
from django.db import models

class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
```

Depois de definir o modelo abstrato, você pode usá-lo como base para outros modelos, herdando seus campos e comportamentos. Aqui está um exemplo de como criar um modelo Post que herda do modelo abstrato BaseModel:

```
from django.db import models
from django.contrib.auth.models import User

class Post(BaseModel):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
```

Nesse exemplo, o modelo Post herda os campos created_on e updated_on do modelo abstrato BaseModel, além de definir seus próprios campos para título, conteúdo e autor. Quando você cria e aplica migrações para o modelo Post, o Django cria uma tabela no banco de dados que inclui todos esses campos.

Os modelos abstratos são úteis quando você tem vários modelos que compartilham campos e comportamentos comuns, pois permitem que você reutilize esse código em vez de repeti-lo em cada modelo individualmente. Eles também ajudam a manter seu código mais organizado e fácil de manter.