import pandas as pd

data =[
    {
        "Emp": "Jeff Russel",
        "POs": [
            {"Pono": 2608, "Total": 35},
            {"Pono": 2617, "Total": 35},
            {"Pono": 2620, "Total": 139}
        ]
    },
    {
        "Emp": "Jane Boorman",
        "POs": [
            {"Pono": 2621, "Total": 95},
            {"Pono": 2626, "Total": 218}
        ]
    },
]

df = pd.json_normalize(data, "POs", "Emp").set_index(["Emp", "Pono"])
print(df)

print("-"*100)

print("Total de vendas", df.groupby(["Emp"])["Total"].sum())

print("-"*100)

df = df.reset_index()
print(df)

# transforma em json para ser lido no front
json_doc = (
    df.groupby(["Emp"], as_index=True)
    .apply(lambda x : x[["Pono", "Total"]].to_dict("records"))
    .reset_index()
    .rename(columns={0: "POs"})
    .to_json(orient="records")
)

print(json_doc)

