import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd

df = pd.read_csv("../employees.csv")

fig, (ax, ax1) = plt.subplots(1,2)
fig.set_size_inches(5.6, 4.2)


# pegando valores minimos e máximos
print(df["Salary"].nlargest(1))
print(df["Salary"].nsmallest(1))

ax.hist(
    df["Salary"], bins=np.arange(30_000, 160_000, 10_000), edgecolor="black", linewidth=1.2
)

formatter = ticker.FormatStrFormatter("$%1.0f")
ax.xaxis.set_major_formatter(formatter)
plt.title("Salários mensais no departamento de vendas. (employees.csv)")
plt.xlabel("Salário (bin = 10_000)")
plt.ylabel("Frequência")

plt.show()