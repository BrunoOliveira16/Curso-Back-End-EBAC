## 📝 Aula 04: Gerenciando mudanças com git branches e git tags
O Git permite gerenciar mudanças em seu código-fonte usando branches e tags.

### Branches 
Permitem que você crie linhas independentes de desenvolvimento em seu repositório. Quando você cria um branch, ele funciona como uma abstração para o processo de edição/estágio/confirmação. Você pode pensar neles como uma forma de solicitar um diretório de trabalho, uma área de staging e um histórico do projeto totalmente novos. Novas confirmações são registradas no histórico para o branch atual, o que resulta em uma bifurcação na história do projeto.

O comando ``git branch`` permite criar, listar, renomear e excluir branches. Ele não permite alternar entre branches ou reunir um histórico bifurcado novamente. Por esse motivo, o comando ``git branch`` é muito integrado com os comandos ``git checkout`` e ``git merge``.

<br>

### Tags 
são referências que apontam para pontos específicos no histórico do Git. O comando ``git tag`` é usado para capturar um ponto no histórico que é usado para uma versão marcada (por exemplo, v1.0.1). Um tag é como um branch que não muda - depois de criado, ele não tem mais histórico de commits.

O Git suporta dois tipos diferentes de tags: anotadas e leves. As tags anotadas armazenam metadados extras, como o nome de quem criou a tag, e-mail e data. As tags leves são basicamente “marcadores” em um commit - elas são apenas um nome e um ponteiro para um commit.

O comando git tag permite criar, listar e excluir tags. Você pode usar tags para marcar pontos importantes no histórico do seu projeto, como lançamentos de versões.

<br>

### Criando uma nova branch no Git
Para criar um novo branch no Git, você pode usar o comando ``git branch`` seguido pelo nome do novo branch. Por exemplo, para criar um novo branch chamado ``meu-novo-branch``, você pode executar o seguinte comando:
```
git branch meu-novo-branch
```

Isso criará um novo branch chamado ``meu-novo-branch`` que aponta para o mesmo commit que o branch atual. Observe que esse comando apenas cria o novo branch, mas não muda para ele. Para mudar para o novo branch, você pode usar o comando ``git checkout`` seguido pelo nome do branch:
```
git checkout meu-novo-branch
```

Isso mudará para o branch meu-novo-branch e atualizará o diretório de trabalho para refletir o estado do projeto nesse branch.

Você também pode criar e mudar para um novo branch em um único comando usando a opção -b com o comando git checkout:
```
git checkout -b meu-novo-branch
```

Isso criará um novo branch chamado meu-novo-branch e mudará para ele imediatamente.

<br>

### git merge
O comando ``git merge`` é usado para mesclar as alterações de um branch em outro branch. Isso permite que você incorpore as alterações feitas em um branch separado de volta ao branch principal ou a qualquer outro branch.

Por exemplo, suponha que você tenha criado um novo branch chamado ``meu-novo-branch`` para trabalhar em um novo recurso. Depois de concluir o trabalho nesse branch, você pode querer mesclar as alterações de volta ao branch principal (geralmente chamado de master ou main). Para fazer isso, você primeiro mudaria para o branch principal usando o comando ``git checkout``:
```
git checkout main
```

Em seguida, você usaria o comando ``git merge`` para mesclar as alterações do branch ``meu-novo-branch`` no branch principal:
```
git merge meu-novo-branch
```

Isso mesclará as alterações do branch ``meu-novo-branch`` no branch principal. Se houver conflitos entre os dois branches (ou seja, se as mesmas linhas de código foram modificadas nos dois branches), o Git solicitará que você resolva os conflitos manualmente antes de concluir a mesclagem.

Depois que a mesclagem for concluída com sucesso, o branch principal terá todas as alterações feitas no branch ``meu-novo-branch``. Você pode continuar trabalhando no branch principal ou mudar para outro branch conforme necessário.

<br>

