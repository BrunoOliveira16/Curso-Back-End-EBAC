## 📝 Aula 03: Ferramentas para controle de versão 
Existem várias ferramentas de controle de versão disponíveis para ajudar as equipes de desenvolvimento a gerenciar as alterações em seu código-fonte ao longo do tempo. Algumas das ferramentas de controle de versão mais conhecidas incluem Git, Mercurial, Bazaar e Darcs.

O Git é atualmente a ferramenta de controle de versão mais popular e é usado como base para serviços de gerenciamento de repositórios como GitHub e GitLab. Ele é um sistema distribuído, o que significa que cada desenvolvedor tem uma cópia completa do histórico do projeto em seu computador local. Isso permite que os desenvolvedores trabalhem offline e torna o processo de branching e merging mais simples.

Outras ferramentas de controle de versão incluem Mercurial, que é usado por empresas como Facebook e Google, Bazaar e Darcs. Cada ferramenta tem suas próprias características e vantagens, então é importante escolher a ferramenta que melhor atenda às necessidades da sua equipe.

Além das ferramentas de controle de versão em si, existem muitas outras ferramentas e serviços disponíveis para ajudar as equipes a gerenciar seu código-fonte, como serviços de hospedagem de repositórios, ferramentas de revisão de código e integração contínua.

Controle de versão com suporte a Git com hospedagem de código:

- Github

- Gitlab

- Bitbucket

### Criando uma conta no Github
Acesse: https://github.com/join?source=login

### Github SSH
- Usada para aumentar a segurança de quem está usando um determinado repositório.
- Utilizado por diversas empresas.

#### Gerando uma chave SSH
1. Abra seu terminal

2. Digite com ssh-keygen -t ed25519 -C “your_email@example.com” e substua com seu email

3. De um enter caso queira manter o nome padrão do arquivo com a chave SSH

4. Caso não queira dar um outro nome para o passphrase aperte Enter

#### Adicionando o SSH-key no Github
1. Abra o terminal e digite eval “$(ssh-agent -s)”

2. Adicione sua chave na sua conta do Github

#### Criando nosso primeiro repositório
- Vamos criar nosso primeiro repositório.

- Depois de criado vamos clonar nosso repositório usando o comando clone:

- ``git clone git@github.com:<nome-do-user>/<nome-do-repo>.git``

#### Fazendo nosso primeiro commit
Vamos adicionar um arquivo de texto, commitar e enviar essa alteração para
nosso repositório:
1. git add . (para adicionar todos os arquivos que foram alterados)

2. git commit -m “Nome da alteração”

3. git status (para visualizar o que será alterado)

4. git push origin HEAD

#### Gitflow
Sincronizar o trabalho entre equipes requer organização e controle de
mudanças, veremos agora o que o Git oferece para suportar o trabalho em
conjunto e em paralelo em um mesmo projeto.