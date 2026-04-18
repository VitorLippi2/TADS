import pandas as pd

# Carregue os dados do arquivo vendas.csv
df = pd.read_csv("vendas.csv", sep=",")

# Apresente o somatório de cada categoria e o somatório total
df_categoria = df[["Categoria", "Quantidade"]]
df_categoria = df_categoria.groupby("Categoria").sum()

print("Somatório por categoria:")
print(df_categoria.head())

print("Somatório Total: ", df_categoria[["Quantidade"]].sum())