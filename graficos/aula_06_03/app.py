import dash
import dash_bootstrap_components as dbc
from dash import html

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])

sidebar = html.Div([
    html.H2("Sidebar", className="display-4"),
    html.Hr(),
    html.P("Sidebar", className="lead"),
    dbc.Nav(
            [
                dbc.NavLink(page["name"], href=page["relative_path"], active="exact")
                for page in dash.page_registry.values()
                if page["path"] != "/404"
            ],
            vertical = True,
            pills = True
        )
    ], className  = "app-side-bar"  # app-side-bar é um id que está em style.css
)

content = html.Div(dash.page_container, className="app-content") # app-content é um id que está em style.css

app.layout = html.Div([sidebar, content])

if __name__ == "__main__":
    app.run(port=8888, debug=True)