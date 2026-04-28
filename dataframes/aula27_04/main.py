import pandas as pd

df = pd.read_csv('../employees.csv', sep=',')

# valores vazios em Gender
print(df["Gender"].isna().value_counts())

df = df.groupby("Gender").mean("Salary")

# média salarial por gênero
print(df.groupby(["Gender"])["Salary"].mean())

print(df)