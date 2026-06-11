import pandas as pd
import numpy as np

df = pd.read_csv("./finance/tesla.csv")
df = df.set_index("Date")
#print(df)

df_2shift = pd.concat([df["Close"], df["Close"].shift(2)], axis=1, keys=["Close", "2DayShift"])
df_2shift["%"] = (df_2shift["Close"] - df_2shift["2DayShift"]) / df_2shift["2DayShift"]
# print(df_2shift) # ex: dia 12 olha pra 2 dias antes(shift(2)) [[REGISTRADOS NO DF. O DF SEGUE A SEQUÊNCIA 7,8,9,12,13]]; Ou seja, do fechamento do dia 8(318.380005) ao dia 12(318.380005] tivemos um cresimento de 11%. Repare que o valor 

df_2shift["2DayRise"] = np.log(df_2shift["Close"] / df_2shift["2DayShift"]) # usa log pq n pode somar porcentagem
print(df_2shift)