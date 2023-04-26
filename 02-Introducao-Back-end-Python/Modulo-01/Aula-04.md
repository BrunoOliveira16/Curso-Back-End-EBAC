## 📌 Editar arquivos utilizando a linha de comando

## ✅ O Editor de textos Vi
- Possui diversas funcionalidades avançadas
- Não é intuitivo
- Requer um tempo para se familiarizar com os comandos
- ``vi <nome do arquivo>`` -> para abrir o arquivo
- ``vim <nome do arquivo>`` -> mesmo que o vi, mas com mais funcionalidades

## Vi Modo de Inserção
- ``i`` Inserir na posição do cursor.
- ``I`` Inserir no começo da linha. 
- ``a`` Acrescentar depois do cursor. 
- ``A`` Acrescentar no final da linha do cursor. 

## Vi Modo de Alteração
- ``:w`` Writes (saves) the file.
- ``:w!`` Forces the file to be saved. 
- ``:q`` Quit.
- ``:q!`` Quit without saving changes. 
- ``:wq!`` Write and quit.
- ``:x`` Same as :wq. 

<br>

## ✅ Nano Editor de Texto
- Nano é mais simples 
- Fácil de aprender
- Mais intuítivo

## Copiando arquivos e diretórios 

```
cp <nome do arquivo> <nome do diretório de destino>

cp hello-world.py ../Java
```

Para copiar diretórios precisamos incluir o ``-r``
```
cp -r <nome do diretório> <nome do diretório de destino>

cp -r java Python/
```

## Movendo arquivos e diretórios
```
mv <nome do arquivo> <nome do diretório de destino>

cp hello-world.py ../Java
```

Para mover diretórios não precisamos incluir o ``-r``
```
mv <nome do diretório>/ <nome do diretório de destino>/

mv java/ Python/
```

## Deletando arquivos e diretórios 
```
rm <nome do arquivo> 
rm hello-world.py
```

Para remover diretórios precisamos incluir o -r
```
rm -r <nome do diretório>
rm -r java
```

Para forçar a remoção precisamos incluir o -f
```
rm -rf <nome do diretório>
rm -rf java
```