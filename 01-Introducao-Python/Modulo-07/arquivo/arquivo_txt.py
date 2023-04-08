class ArquivoTXT(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self._extrair_conteudo()

  def _extrair_conteudo(self):
    conteudo = None
    with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
      conteudo = arquivo.readlines()
    return conteudo

  def extrair_linha(self, numero_linha: int):
    return self.conteudo[numero_linha-1]