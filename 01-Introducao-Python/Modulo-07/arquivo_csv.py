class ArquivoCSV(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()
    self.colunas = self._extrair_nome_colunas()

  def _extrair_conteudo(self):
    conteudo = None
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      conteudo = arquivo.readlines()
    return conteudo

  def _extrair_nome_colunas(self):
    return self.conteudo[0].strip().split(sep=',')

  def extrair_coluna(self, indice_coluna: str):
    coluna = list()
    for linha in self.conteudo:
      conteudo_linha = linha.strip().split(sep=',')
      coluna.append(conteudo_linha[indice_coluna])
    coluna.pop(0)
    return coluna