"""Módulo 1 - Váriaveis & Tipos de Dados

**Aula 5: Boleanos**"""

"""**5.1. Motivação**

Em websites (redes sociais, e-commerce, corporativos, etc.) é comum o uso de sistemas de controle de acesso, o famoso login. Em geral, nestes sistemas um usuário fornece dois dados:
*usuario* e *senha*"""

usuario = 'bruno.oliveira'
senha = 'bruno123'

"""Do lado do servidor, o backend do website tem armazenado os dados de usuário e senha fornecidas pelo usuário no momento do cadastro: *usuario_cadastro* e *senha_cadastro* """

usuario_cadastro = 'bruno.oliveira'
usuario_senha = 'bruno321'

"""Como comparamos se as strings ( *usuario , usuario_cadastro* ) e ( *senha , senha_cadastro* ) são iguais para conceder ou bloquear o acesso do usuário?"""

"""**5.2. Definição**

Armazenam **valores lógicos**:
- True (verdadeiro);
- False (falso)."""

verdadeiro = True
print(verdadeiro)

falso = False
print(falso)

"""São do tipo *bool*. """

print(type(True))

"""São resultados de comparações lógicas. Os operadores de comparação lógica são:
- '>(maior);'
- <(menor);
- ==(igual);
- '>=(maior ou igual);'
- <=(menor ou igual);
- !=(diferente).

**Exemplo:** Caixa eletrônico"""

saldo_em_conta = 200
valor_do_saque = 100

pode_executar_saque = valor_do_saque <= saldo_em_conta
print(pode_executar_saque)

"""**Exemplo:** Cartão de crédito"""

codigo_de_seguranca = '852'
codigo_de_seguranca_cadastro = '010'

pode_efetuar_pagamento = codigo_de_seguranca == codigo_de_seguranca_cadastro
print(pode_efetuar_pagamento)

"""**5.3. Operações**

As operações de variáveis booleanas são:

- | (operador ou)
- & (operador e)
- not (operador não)

O conjunto de resultados de operações lógicas geralmente é resumido em uma tabela chamada "tabela da verdade":"""

"""**Exemplo:** Tabela da verdade do operador | (ou)."""

print(True | True)
print(True | False)
print(False | False)
print(False | True)

"""**Exemplo:** Tabela da verdade do operador & (e)."""

print(True & True)
print(True & False)
print(False & False)
print(False & True)

"""**Exemplo:** Tabela da verdade do operador not (não)."""

print(not True)
print(not False)

"""**5.4. Conversão**

Podemos converter tipos numéricos e strings para booleanos através do método nativo bool:"""

idade = 19
tipo_sangue = 'O-'
filhos = 0
telefone_fixo = None
telefone_fixo = ''

print(bool(idade))
print(bool(tipo_sangue))
print(bool(filhos))
print(bool(telefone_fixo))
print(bool(telefone_fixo))

"""**5.5. Revisitando a motivação**

Compara se os dados fornecidos pelo usuário são iguais aos dados do cadastro:"""

usuario_igual = usuario == usuario_cadastro
senha_igual = senha == usuario_senha

print(usuario_igual)
print(senha_igual)

"""Decide se concede o acesso:"""

conceder_acesso = usuario_igual & senha_igual
print(conceder_acesso)