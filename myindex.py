from dash import html, dcc
from dash.dependencies import Input, Output

import globals
from app import *
from components import sidebar, dashboards, extratos

# =========  Layout  =========== #
content = html.Div(id="page-content")

app.layout = dbc.Container(children=[
    dcc.Store(id='store-receitas', data=globals.df_receitas.to_dict()),
    dcc.Store(id='store-despesas', data=globals.df_despesas.to_dict()),
    dcc.Store(id='store-cat-receitas', data=globals.df_cat_receita.to_dict()),
    dcc.Store(id='store-cat-despesas', data=globals.df_cat_despesa.to_dict()),

    dbc.Row([
        dbc.Col([
            dcc.Location(id='url'),
            sidebar.layout
        ], md = 2, style={'background-color': '', 'height': '1080px'}),
        dbc.Col([
            content
        ], md = 10, style={'background-color': '', 'height': '1080px'})
    ])
], fluid=True,)

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def render_page(pathname):
    if pathname == '/' or pathname == '/dashboards':
        return dashboards.layout
    
    if pathname == '/extratos':
        return extratos.layout

if __name__ == '__main__':
    app.run_server(port=8051, debug=True)