## 📌 Como rodar uma aplicação web Django utilizando Gunicorn e Nginx

### Preparando sua aplicação
1 - Atualize seu CentOs
```
sudo yum update
```

2 - Instale o Nginx
```
sudo yum install python-pip python-devel gcc nginx
```

<br>

### configurando o ambiente virtual
3 - Instale o virtualenv
```
sudo yum install python-pip python-devel gcc nginx
```

4 - crie uma pasta para o seu projeto, no meu caso irei criar uma pasta com o nome de ``myproject``
```
mkdir myproject

# acesse sua pasta
cd myproject
```
5 - Instale o Gunicorn e o Flask
Devemos instalar o Gunicorn dentro do Ambiente Virtual! Ou seja, se foi instalado globalmente o Gunicorn, devemos desinstalar ele e instalar novamente.
```
sudo pip3 uninstall gunicorn
```
O comando acima é para certificar que esteja desinstalado globalmente, se ocorre um erro escrito "Cannot uninstall requirement gunicorn, not installed" significa que não há um gunicorn instalado globalmente, poderemos prosseguir.

6 - Construindo o ambiente virtual devemos executar os comandos
```
# rode
virtualenv myprojectenv

# ative o virtualenv
source myprojectenv/bin/activate
```

7 - Instale o Gunicorn e o Flask
```
pip3 install gunicon flask
```

8 - Crie um arquivo dentro da sua pasta no caso o meu se chamara ``myproject.py``
```
nano myproject.py
```
copie e cole o conteúdo abaixo
```
from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "<h1 style='color:blue'>Hello World from seu nome!</h1>"

if __name__ == "__main__":
    application.run(host='0.0.0.0')
```

9 - Teste seu app rodando:
```
python myproject.py
```
Abra o firefox dentro do seu virtualbox e busque por http://localhost:5000

Se você viu seu nome, parabéns sua aplicação está rodando com sucesso.

<br>

### Configurando o Gunicorn
10 - Crie um arquivo chamado ``wsgi.py`` dentro da pasta do seu projeto

E copie o contúdo abaixo:

```
from myproject import application

if __name__ == "__main__":
    application.run()
```

11 - Vamos agora testar o Gunicorn servindo seu app
```
gunicorn --bind 0.0.0.0:8000 wsgi
```

Abra o firefox dentro do seu virtualbox e busque por http://localhost:8000 você deve continuar vendo a mensagem de Hello World + seu nome

12 - Desative o ambiente virtual do seu projeto
```
deactivate
```

<br>

### Configurando nosso app como serviço
13 - Crie um arquivo de serviço dentro do etc/systemd/system/
```
sudo nano /etc/systemd/system/myproject.service
```
E cole o conteúdo abaixo
```
[Unit]
Description=Gunicorn instance to serve myproject
After=network.target

[Service]
User=adminuser
Group=adminuser
WorkingDirectory=/home/adminuser/Documents/python/myproject
Environment="PATH=/home/adminuser/Documents/python/myproject/myprojectenv/bin"
ExecStart=/home/adminuser/Documents/python/myproject/myprojectenv/bin/gunicorn --workers 3 --bind unix:myproject.sock -m 007 wsgi

[Install]
WantedBy=multi-user.target
```
> Lembre de usar o comando ``pwd`` dentro da pasta do seu projeto para pegar o caminho correto e que o ambiente virtual é uma pasta dentro do seu projeto

14 - Execute os comandos abaixo para habilitar o gunicorn + nosso app como serviço:
```
sudo systemctl start myproject

sudo systemctl enable myproject
```

<br>

### Configurando o Nginx
Abra o nginx.conf
```
sudo nano /etc/nginx/nginx.conf
```
Navegue até o ```server { }``` e copie toda a instrução do server abaixo e substitua no seu nginx.conf
```
server {
        listen       80;
        listen       [::]:80 default_server;
	    server_name  myproject www.myproject;

	# Logs
        access_log /var/log/nginx/myproject.access.log;
        error_log /var/log/nginx/myproject.error.log;

        # Load configuration files for the default server block.
        include /etc/nginx/default.d/*.conf;

        location / {
            proxy_pass http://unix:/home/adminuser/Documents/python/myproject/myproject.sock;
        }

        error_page 404 /404.html;
            location = /40x.html {
        }

        error_page 500 502 503 504 /50x.html;
            location = /50x.html {
        }
    }

```

15 - Altere as permissões para o ``nginx`` acessar a pasta do seu projeto
```
sudo usermod -a -G adminuser nginx

sudo chmod 710 /home/adminuser
```

16 - Verifique se as configurações do ``nginx`` estão funcionando`
```
sudo nginx -t
```

16 - Estando tudo certo no passo 10 agora execute os comandos
```
sudo systemctl start nginx

sudo systemctl enable nginx
```

17 - Adicionando a rota no ``/etc/hosts``

Execute o ifconfig na sua maquina e copie o ip que está próximo do inet (primeiro bloco) no meu caso foi 10.0.2.15

Pegue esse IP e cole no ``/etc/hosts``

Seu arquivo deve estar assim

sudo nano /etc/hosts
```
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.0.2.15   myproject
```

18 - Reinicie o Gunicorn e Nginx
```
sudo systemctl restart myproject

sudo service nginx restart
```

19 - Acesse seu virtualbox, abra o firefox e busque por http://myproject

Se você ver a página do hello world com seu nome, parabéns, você configurou seu primeiro ambiente pronto para produção!

para testar o status do seu serviço, digite o comando:
```
sudo systemctl status myproject
```

deverá obter um resultado parecido com esse:

<img src="./assets/img-05.jpg">