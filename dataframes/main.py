import pandas as pd

nba = pd.read_csv('nba.csv', sep=',')


nba.insert(3, "Sport", value="Basktball")
# print(nba.columns)

nba = nba.dropna()


# média salarial por colegiado dos jogadores
nba = nba[["College", "Salary"]]
nba = nba.groupby(["College"]).mean("Salary")

print(nba)

# só apaga se tiver tudo vazio
print(nba.dropna(how="all"))
