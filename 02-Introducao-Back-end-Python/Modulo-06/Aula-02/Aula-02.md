## 📝 Aula 02: Iniciando projetos Django
Para iniciar um projeto Django, primeiro você precisa ter o Python e o Django instalados em seu sistema. Você pode verificar se o Django está instalado e qual versão está instalada executando o seguinte comando em um prompt de comando ou terminal:
```
django-admin --version
```

Se o Django estiver instalado, esse comando deve exibir a versão do Django que está instalada em seu sistema. Se você receber uma mensagem de erro informando que o comando django-admin não foi encontrado, isso significa que o Django não está instalado. Nesse caso, você pode instalar o Django usando o gerenciador de pacotes pip:
```
pip install django
```

Depois de instalar o Django, você pode criar um novo projeto Django usando o comando django-admin startproject seguido pelo nome do projeto. Por exemplo, para criar um novo projeto chamado meuprojeto, você pode executar o seguinte comando:
```
django-admin startproject meuprojeto
```

Isso criará um novo diretório chamado ``meuprojeto`` contendo a estrutura básica de um projeto Django. Dentro desse diretório, você encontrará vários arquivos e diretórios importantes, incluindo:


- manage.py: Um utilitário de linha de comando que permite interagir com o projeto de várias maneiras.

- meuprojeto/: Um diretório contendo as configurações do projeto.

- meuprojeto/__init__.py: Um arquivo vazio que indica ao Python que esse diretório deve ser considerado um pacote Python.

- meuprojeto/settings.py: Configurações do projeto Django.

- meuprojeto/urls.py: As declarações de URL para o projeto Django; uma “tabela de conteúdos” do seu site alimentado pelo Django.

- meuprojeto/asgi.py: Um ponto de entrada para servidores ASGI compatíveis com o projeto.

- meuprojeto/wsgi.py: Um ponto de entrada para servidores WSGI compatíveis com o projeto.

Depois de criar o projeto, você pode navegar até o diretório do projeto e iniciar o servidor de desenvolvimento do Django usando o seguinte comando:
```
cd meuprojeto
python manage.py runserver
```

Isso iniciará o servidor de desenvolvimento do Django e você poderá acessar seu aplicativo em ``http://127.0.0.1:8000/``. A partir daí, você pode começar a adicionar aplicativos ao seu projeto e desenvolver seu site usando o Django.

<br>

### criando novo app Django
O comando python ``manage.py startapp`` é usado para criar um novo aplicativo Django dentro de um projeto Django existente. Ele é executado a partir da linha de comando dentro do diretório do projeto Django e requer um argumento adicional que especifica o nome do novo aplicativo.

Por exemplo, para criar um novo aplicativo chamado ``meuapp`` dentro de um projeto Django existente, você pode navegar até o diretório do projeto e executar o seguinte comando:
```
python manage.py startapp meuapp
```

Isso criará um novo diretório chamado meuapp dentro do diretório do projeto, contendo a estrutura básica de um aplicativo Django. Dentro desse diretório, você encontrará vários arquivos importantes, incluindo:


- __init__.py: Um arquivo vazio que indica ao Python que esse diretório deve ser considerado um pacote Python.

- admin.py: Um arquivo para registrar seus modelos no site de administração do Django.

- apps.py: Um arquivo para configurar as configurações específicas do aplicativo.

- models.py: Um arquivo para definir os modelos do aplicativo (a camada de abstração do banco de dados).

- tests.py: Um arquivo para escrever testes para o aplicativo.

- views.py: Um arquivo para definir as views do aplicativo (as funções que lidam com as requisições e retornam respostas).

Depois de criar o aplicativo, você pode começar a adicionar modelos, views e URLs ao aplicativo para implementar a funcionalidade desejada. Lembre-se de adicionar o novo aplicativo à configuração INSTALLED_APPS no arquivo settings.py do projeto para que o Django saiba que ele deve incluir o aplicativo em seu processo de inicialização.