import pandas as pd
from matplotlib import pyplot as plt

dados_emprestimos = []

nomes_emprestimos = pd.read_csv("./dados_biblioteca/dados_emprestimos/emprestimos.csv",header=None)


for nome in nomes_emprestimos[0]:
    caminho = f"./dados_biblioteca/dados_emprestimos/{nome}"
    dados_emprestimos.append(pd.read_csv(caminho))

df_emprestimos = pd.concat(dados_emprestimos)

df_exemplares = pd.read_csv("./dados_biblioteca/dados-exemplares.csv")

df_emprestimos = df_emprestimos.merge(df_exemplares)
df_emprestimos = df_emprestimos.dropna()
df_emprestimos = df_emprestimos.drop_duplicates()

df_ano_emprestimos = df_emprestimos["data_emprestimo"].value_counts()
df_ano_emprestimos = df_ano_emprestimos.reset_index()
df_ano_emprestimos["data_emprestimo"] = pd.to_datetime(df_ano_emprestimos["data_emprestimo"])
df_ano_emprestimos["ano"] = df_ano_emprestimos["data_emprestimo"].dt.year

df_grupo_ano = df_ano_emprestimos.groupby("ano")["count"].sum()
df_grupo_ano = df_grupo_ano.reset_index()

plt.plot(df_grupo_ano["ano"],df_grupo_ano["count"])
plt.title("Evolução dos empréstimos ao longo dos anos")
plt.xlabel("Ano")
plt.ylabel("Quantidade")
plt.show()



