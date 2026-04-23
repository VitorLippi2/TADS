import pandas as pd

nba = pd.read_csv("../nba.csv").dropna(how="all")

# preenchendo valores nulos com 0
nba["Salary"].fillna(0, inplace=True)
nba["Colege"] = nba["College"].fillna("None")

nba["Salary"] = nba["Salary"].astype("float")
nba["Number"] = nba["Number"].astype("int")
nba["Age"] = nba["Age"].astype("int")
nba["Position"].nunique()
nba["Position"] = nba["Position"].astype("category")
nba["Team"].nunique()
nba["Team"] = nba["Team"].astype("category")


print(nba.info())