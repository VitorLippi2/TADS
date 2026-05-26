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

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = dbc.Container([
    html.H1("Dashboard", className='mb-2', style={'textAlign':'center'}),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(
                id='category',
                value='Number of Solar Plants',
                clearable=False,
                options=df.columns[1:])
        ], width=4)
    ]),

    dbc.Row([
        dbc.Col([
            html.Img(id='bar-graph-matplotlib')
        ], width=12)
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='bar-graph-plotly', figure={})
        ], width=12, md=6),
        dbc.Col([
            dag.AgGrid(
                id='grid',
                rowData=df.to_dict("records"),
                columnDefs=[{"field": i} for i in df.columns],
                columnSize="sizeToFit",
            )
        ], width=12, md=6),
    ], className='mt-4'),
])

@app.callback(
    Output('bar-graph-matplotlib', 'src'),
    Output('bar-graph-plotly', 'figure'),
    Output('grid', 'defaultColDef'),
    Input('category', 'value')
)

def plot_data(selected_yaxis):
    # 1. Matplotlib (Corrigido: plt.subplots() e nomes de variáveis)
    fig, ax = plt.subplots(figsize=(14, 5))
    ax.bar(df["State"], df[selected_yaxis])
    ax.set_ylabel(selected_yaxis)
    plt.xticks(rotation=30)

    buf = BytesIO()
    fig.savefig(buf, format="png", bbox_inches='tight')
    plt.close(fig) # Importante para liberar memória
    
    fig_data = base64.b64encode(buf.getbuffer()).decode("ascii")
    bar_graph_matplotlib = f"data:image/png;base64,{fig_data}"

    # 2. Plotly (Corrigido nome da variável)
    fig_bar_plotly = px.bar(df, x="State", y=selected_yaxis)
    fig_bar_plotly.update_xaxes(tickangle=330)

    # 3. AG Grid cellStyle (Corrigido 'backgroundColod' para 'backgroundColor')
    my_cellStyle = {
        "styleConditions": [
            {
                "condition": f"params.colDef.field == '{selected_yaxis}'",
                "style": {"backgroundColor": "#d3d3d3"}
            },
            {
                "condition": f"params.colDef.field != '{selected_yaxis}'",
                "style": {"backgroundColor": "black"}
            }
        ]
    }

    return bar_graph_matplotlib, fig_bar_plotly, {"cellStyle": my_cellStyle}

if __name__ == "__main__":
    app.run(debug=False, port=8002)