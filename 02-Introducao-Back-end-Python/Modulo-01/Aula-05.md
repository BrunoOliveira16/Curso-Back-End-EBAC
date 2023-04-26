## 📌 Como instalar softwares utilizando a linha de comando

## Comandos yum - CentOS 7 e anteriores
- ``yum`` search string Search for string
- ``yum`` info [package] Display info 
- ``yum`` install [-y] package Install package 
- ``yum`` remove package Remove package 
- ``yum`` upgrade [package] Update package

<br>

## Comandos rpm - Debian... Ubuntu...
- ``apt-get install`` [-y] package Install package
- ``apt-get purge package`` Remove package, deleting configuration
- ``apt-get remove package`` Remove package, leaving configuration

<br>

## Instalando Softwares no CentOS
Para manipular serviços no linux vamos utilizar o ``systemctl`` ele é responsável por controlar pacotes e serviços instalados dentro do ``/etc/``

Ele é um ``atalho`` para não termos que ir no /etc/<nome-do-serviço>/ 
toda vez que precisarmos para ou subir um serviço

Vamos agora instalar o ``Apache`` Web Serve

<br>

