import pandas as pd

df = pd.read_csv('../employees.csv')
df["Start Date"] = pd.to_datetime(df["Start Date"])
df["Senior Management"] = df["Senior Management"].astype("bool")

# limpando linhas nulas
df = df.dropna(how='all')
df['Team'] = df['Team'].fillna('Nulo')

# novo df -> salário superior a 100_000
mask = df["Salary"] > 100_000
employees_over_100_000 = df[mask]
print(employees_over_100_000)

df_salary = df.groupby("Team").mean("Salary")
df_salary = df[["Salary"]]
print(df_salary)
print(df_salary.nlargest(n=1, columns="Salary"))

# salário por equipe dividido por gênero
df_generos = df.groupby(["Team", "Gender"])["First Name"].count()
print(df_generos)

# nova coluna com Bônus 
df['Total Compensation'] = (df["Salary"] + df["Bonus %"]) / 100
print(df)

# ordenando de forma decrescente por salary
df = df.sort_values("Salary", ascending=False)