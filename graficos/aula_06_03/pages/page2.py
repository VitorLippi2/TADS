import dash
from dash import html

dash.register_page(__name__, path="/page-2", name="Page 2", order=2)

layout = html.P("Page 2")