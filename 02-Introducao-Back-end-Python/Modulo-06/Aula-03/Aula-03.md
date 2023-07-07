## 📝 Aula 03: Configurando um novo projeto Django e como gerenciar migrações de banco de dados com Django
Na aula anterior após ter sido criado o app ``blog``, se faz necessário ir em settings.py dentro do nosso projeto ``mysite`` e adicionar o app que foi criado para que o Django saiba que ele deve incluir o aplicativo em seu processo de inicialização.

settings.py
```
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
```

<br>

### migrations
O comando ``migrate`` é um dos comandos mais importantes da camada Model do Django. Quando executamos o comando ``makemigrations``, o Django cria o banco de dados e as migrações, mas não as executa, isto é: não realmente aplica as alterações no banco de dados. Para que o Django as aplique, são necessárias três coisas, basicamente: 1. Que a configuração da interface com o banco de dados esteja descrita no arquivo de configurações ``settings.py``. 2. Que os modelos e migrações estejam definidos para esse projeto. 3. Execução do comando migrate .

Para executar o comando migrate, vamos para a raíz do projeto e executamos: ``python manage.py migrate``. A saída deve ser algo como:
```
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

> Por padrão, o Django utiliza um banco de dados leve e compacto chamado SQLite. É o banco de dados padrão que o Django usa se não for especificado e configurado.

<br>

### runserver
O comando python manage.py runserver é usado para executar o servidor do Django. Por padrão, ele inicia o servidor no endereço ``http://localhost:8000``, que pode ser usado para executar o projeto. Você também pode especificar um endereço IP e uma porta para o servidor se vincular, por exemplo: ``python manage.py runserver 192.168.23.12:8000``.