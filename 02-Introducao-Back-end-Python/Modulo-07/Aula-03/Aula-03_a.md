## 📝 Aula 03: Relacionando entidades com Django e quais os tipos de campos disponiveis em Django
### Relacionando entidades com Django
No Django, você pode relacionar entidades (modelos) usando campos de relacionamento, como ``ForeignKey``, ``OneToOneField`` e ``ManyToManyField``. Esses campos permitem que você defina relações entre modelos, como relações um-para-muitos, um-para-um e muitos-para-muitos.

- ``ForeignKey``: Este campo define uma relação um-para-muitos entre dois modelos. Por exemplo, se você tem um modelo ``Author`` e um modelo ``Book``, você pode usar um campo ``ForeignKey`` no modelo ``Book`` para indicar que cada livro está associado a um autor específico. Isso criará uma coluna na tabela do banco de dados para o modelo ``Book`` que armazenará a chave primária do autor associado.

```
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
```

- ``OneToOneField``: Este campo define uma relação um-para-um entre dois modelos. Por exemplo, se você tem um modelo ``User`` e um modelo ``Profile``, você pode usar um campo ``OneToOneField`` no modelo ``Profile`` para indicar que cada perfil está associado a um usuário específico. Isso criará uma coluna na tabela do banco de dados para o modelo ``Profile`` que armazenará a chave primária do usuário associado.

```
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

- ``ManyToManyField``: Este campo define uma relação muitos-para-muitos entre dois modelos. Por exemplo, se você tem um modelo ``Student`` e um modelo ``Course``, você pode usar um campo ``ManyToManyField`` em ambos os modelos para indicar que cada estudante pode estar matriculado em vários cursos e cada curso pode ter vários estudantes matriculados. Isso criará uma tabela intermediária no banco de dados para armazenar as relações entre estudantes e cursos.

```
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField('Course')

class Course(models.Model):
    title = models.CharField(max_length=200)
```

<br>

### Tipos de campos disponiveis em Django
O Django oferece vários tipos de campos que podem ser usados para definir modelos. Aqui está uma lista de alguns dos tipos de campos mais comuns:


- ``CharField``: campo para armazenar strings de tamanho limitado.

- ``TextField``: campo para armazenar strings de tamanho ilimitado.

- ``IntegerField``: campo para armazenar números inteiros.

- ``FloatField``: campo para armazenar números de ponto flutuante.

- ``DecimalField``: campo para armazenar números decimais com precisão fixa.

- ``BooleanField``: campo para armazenar valores booleanos (verdadeiro/falso).

- ``DateField``: campo para armazenar datas.

- ``TimeField``: campo para armazenar horários.

- ``DateTimeField``: campo para armazenar datas e horários.

- ``DurationField``: campo para armazenar durações de tempo.

- ``EmailField``: campo para armazenar endereços de e-mail.

- ``FileField``: campo para armazenar arquivos.

- ``ImageField``: campo para armazenar imagens.

- ``URLField``: campo para armazenar URLs.

- ``UUIDField``: campo para armazenar UUIDs (identificadores únicos universais).

- ``SlugField``: campo para armazenar strings curtas usadas em URLs.

Esses são apenas alguns dos tipos de campos disponíveis no Django. Cada tipo de campo tem suas próprias opções e comportamentos, e você pode escolher o tipo de campo mais adequado para cada atributo do seu modelo.