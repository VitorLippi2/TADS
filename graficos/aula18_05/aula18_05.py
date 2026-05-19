import pandas as pd
import numpy as np
import os

pasta = "../mergeando_tabelas/dados_biblioteca/dados_emprestimos"

caminho = os.listdir(path=pasta)

for a in caminho:
    print(a)

dadosEx = pd.read_csv("../mergeando_tabelas/dados_biblioteca/dados-exemplares.csv")

tabelas = []
for arquivo in caminho:
    print(arquivo)
    df = pd.read_csv(os.path.join(pasta, arquivo))
    tabelas.append(df)

tbEmprestimos = pd.concat(tabelas,ignore_index=True)
tbEmprestimos = pd.merge(tbEmprestimos, dadosEx, on="codigo_barras", how="left")

tbEmprestimos = tbEmprestimos.dropna(how="any")
tbEmprestimos = tbEmprestimos.drop_duplicates(ignore_index=True)

print(tbEmprestimos.columns)
print(tbEmprestimos)