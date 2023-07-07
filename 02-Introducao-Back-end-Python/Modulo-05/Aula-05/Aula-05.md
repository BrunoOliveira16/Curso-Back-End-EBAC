## 📝 Aula 05: Usando Git na prática em projetos com diversas contribuições
O Git é uma ferramenta poderosa para gerenciar projetos com diversas contribuições. Ele permite que os desenvolvedores trabalhem em paralelo em diferentes partes do código, sem interferir uns com os outros, e fornece ferramentas para mesclar as alterações de diferentes branches de maneira controlada.

Ao trabalhar em um projeto com diversas contribuições, é importante seguir algumas práticas recomendadas para garantir que o processo de desenvolvimento seja suave e eficiente. Aqui estão algumas dicas para usar o Git na prática em projetos com diversas contribuições:

- Use branches: Crie branches separados para diferentes recursos ou correções de bugs. Isso permite que os desenvolvedores trabalhem em paralelo sem interferir uns com os outros. Quando um recurso ou correção de bug estiver completo, você pode mesclar as alterações de volta ao branch principal usando o comando git merge.

- Escreva mensagens de commit claras: As mensagens de commit devem descrever claramente o que foi alterado e por quê. Isso ajuda outros desenvolvedores a entender o histórico do projeto e facilita a revisão de código.

- Mantenha o histórico limpo: Evite fazer commits com alterações não relacionadas ou incompletas. Use o comando git rebase para reescrever o histórico e agrupar alterações relacionadas em commits lógicos.

- Revise o código: Antes de mesclar as alterações de um branch em outro, revise o código para garantir que ele atenda aos padrões de qualidade do projeto. Você pode usar ferramentas como pull requests no GitHub para facilitar o processo de revisão de código.

- Resolva conflitos de mesclagem: Quando você mescla as alterações de um branch em outro, pode haver conflitos se as mesmas linhas de código foram modificadas nos dois branches. O Git fornecerá ferramentas para ajudá-lo a resolver esses conflitos manualmente. Certifique-se de testar cuidadosamente o código após resolver os conflitos para garantir que ele ainda funcione conforme o esperado.

Seguindo essas práticas recomendadas, você pode usar o Git com eficiência para gerenciar projetos com diversas contribuições.

<br>

### O que é um pull request no GitHub?
Um pull request é uma funcionalidade do GitHub que permite que os desenvolvedores colaborem em um projeto. Ele permite que um desenvolvedor proponha alterações em um repositório e solicite que essas alterações sejam mescladas no branch principal ou em outro branch.

Quando você cria um pull request, está solicitando que o proprietário do repositório ou outros colaboradores revisem suas alterações e as integrem ao projeto. O pull request fornece uma interface para discutir as alterações propostas, fazer comentários e sugestões e eventualmente aprovar ou rejeitar as alterações.

Os pull requests são úteis em projetos com diversas contribuições, pois permitem que os desenvolvedores trabalhem em paralelo em diferentes partes do código e colaborem de maneira controlada. Eles também fornecem um registro das alterações propostas e das discussões relacionadas, o que pode ser útil para entender o histórico do projeto.

Para criar um pull request no GitHub, você precisa ter um fork do repositório em sua própria conta do GitHub e fazer as alterações desejadas em um branch separado. Em seguida, você pode abrir um pull request para propor a mesclagem de suas alterações no repositório original.

<br>

### Como faço para criar um fork de um repositório no GitHub?
Para criar um fork de um repositório no GitHub, siga estas etapas:

1. Faça login em sua conta do GitHub e navegue até a página do repositório que deseja fazer o fork.

2. Clique no botão “Fork” no canto superior direito da página. Isso criará uma cópia do repositório em sua própria conta do GitHub.

3. Agora você pode clonar o repositório forkado para o seu computador local usando o comando git clone e fazer as alterações desejadas.

Depois de fazer as alterações, você pode enviar as alterações para o seu repositório forkado usando os comandos ``git add``, ``git commit`` e ``git push``. Em seguida, você pode abrir um pull request para propor a mesclagem de suas alterações no repositório original.

Lembre-se de manter o seu fork atualizado com as alterações do repositório original. Você pode fazer isso adicionando o repositório original como um remote e fazendo um pull das alterações periodicamente.