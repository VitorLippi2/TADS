import dash
from dash import html

dash.register_page(__name__, path="/page-1", name="Page 1", order=1)

layout = html.P("Page 1")