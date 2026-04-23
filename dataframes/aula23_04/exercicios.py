import pandas as pd

# limpando valores vazios
df = pd.read_csv("../employees.csv").dropna(how="all")
print(df.info())

# definindo coluna como bool
df["Senior Management"] = df["Senior Management"].astype("bool")

# transformando colunas datetime
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["Last Login Time"] = pd.to_datetime(df["Last Login Time"])

print(df.info())

# valores diferentes em Gender
print(df["Gender"].nunique())