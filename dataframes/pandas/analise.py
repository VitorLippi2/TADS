import pandas as pd

data = ["Huguinho", "Zezinho", "Luizinho"]

emps_names = pd.Series(data)

email_data = ["huguinho.silva", "zezinho.pereira", "luizinho.souza"]

emps_mails = pd.Series(email_data, name="emails")
emps_names.name = 'names'

emps_ids = pd.Series([9000, 9001, 9002], name="ids")

df = pd.concat([emps_ids, emps_names, emps_mails], axis=1)
df = df.set_index("ids")
print(df)