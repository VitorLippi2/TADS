import pandas as pd
from matplotlib import pyplot as plt

employees = pd.read_csv("../employees.csv").dropna(how="all")
employees["Gender"] = employees["Gender"].fillna("NI")
group_gender = employees.groupby("Gender")["Salary"].mean()

plt.pie(group_gender, labels=group_gender.index, autopct='%1.1f%%')
plt.show()

plt.bar(group_gender.index, group_gender)
plt.show()
