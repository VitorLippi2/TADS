from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import dash_ag_grid as dag
import dash_bootstrap_components as dbc
import pandas as pd

import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import base64
from io import BytesIO

df = pd.read_csv("./data/solar.csv")
# print(df.head())

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Dashboard", className="mb-2", style={"textAlign" : "center"}),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id = "category",
                value = "Number of Solar Plants",
                clearable = False,
                options = df.columns[1:]
            )
        ], width = 4)
    ])
])

