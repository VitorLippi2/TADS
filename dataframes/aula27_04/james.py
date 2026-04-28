import pandas as pd

df = pd.read_csv("../jamesbond.csv")

df = df.dropna()

# definindo "Film" e "Year" como índices
df = df.set_index(["Film", "Year"])

# Loc procura pelo index nao numerico. Iloc pelo indice numerico
# procurando pelo ator e diretor nome e pelo ano do filme
print(df.loc[("Casino Royale", 2006)][["Actor", "Director"]])

# salário de cada ator
print(df.groupby("Actor")["Bond Actor Salary"].sum())

# 4 maiores bilheterias
print(df.nlargest(n=4, columns="Box Office")["Box Office"])

# Apenas Sean como ator
df = df.reset_index()
mask = df["Actor"] == "Sean Connery" # cria máscara com True or False
#print(df[mask]) # aplica a máscara

# total de bilheteria com Daniel Craig
mask_craig = df["Actor"] == "Daniel Craig"
print("Soma de Bilheteria: ", df[mask_craig]["Box Office"].sum())


# acionando funções e atribuindo colunas
def convert_to_millions_text(number):
    return str(number) + " millions!"

df["Box Office M"] = df["Box Office"].apply(convert_to_millions_text)
print(df[["Film", "Box Office M"]])

# filmes mais velhos
print(df.nsmallest(n=3, columns="Year")["Year"])

# filmes mais novos
print(df.nlargest(n=3, columns="Year")["Year"])

# bilheteria por década