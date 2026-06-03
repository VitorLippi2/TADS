from dash import Dash, html, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv')



app = Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])

app.layout = dbc.Container([
    dbc.Row([
        html.Div(children='App with Data',className='text-primary text-center fs-3')
    ]),
    dbc.Row([
        dbc.RadioItems(options=[
            {'value':'pop','label':'População'},
            {'value':'lifeExp','label':'Expectativa de vida'},{'value':'gdpPercap','label':'Renda per Capita'}
        ], value='lifeExp', inline= True, id='controls-and-radio-item')
    ]),
    dbc.Row([
        dcc.Graph(figure={},id='controls-and-graph')
    ])
])


@callback(
    Output(component_id='controls-and-graph',component_property='figure'),
    Input(component_id='controls-and-radio-item',component_property='value')
)
def update_graph(col_chosen):
    fig = px.histogram(df,x='continent',y=col_chosen,histfunc='avg' if col_chosen != 'pop' else 'sum')
    return fig




if __name__ == '__main__':
    app.run(debug=True)