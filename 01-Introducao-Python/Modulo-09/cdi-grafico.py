import csv
from sys import argv

import seaborn as sns

# Extraindo as colunas hora e taxa

horas = []
taxas = []

with open(file='./taxa-cdi.csv', mode='r', encoding='utf8') as fp:
  linha = fp.readline()
  linha = fp.readline()
  while linha:
    linha_separada = linha.split(sep=',')
    hora = linha_separada[1]
    horas.append(hora)
    taxa = float(linha_separada[2])
    taxas.append(taxa)
    linha = fp.readline()

# Salvando no grafico

grafico = sns.lineplot(x=horas, y=taxas)
grafico.get_figure().savefig(f"{argv[1]}.png")