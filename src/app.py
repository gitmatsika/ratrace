import pandas as pd
import dash
from dash import Dash , dcc, Input, Output, html
import dash_bootstrap_components as dbc


external_stylesheets = [
    {
        "href": (
            "https://fonts.googleapis.com/css2?"
            "family=Lato:wght@400;700&display=swap"
        ),
        "rel": "stylesheet",
    },
]
app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.SPACELAB])
#[dbc.themes.SPACELAB]
app.title = "Augtion for 2023!"
sidebar = dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.Div(page["name"], className="ms-2"),
                    ],
                    href=page["path"],
                    active="exact",
                )
                for page in dash.page_registry.values()
            ],
            vertical=True,
            pills=True,
            className="bg-light",
)

app.layout = dbc.Container([
    #dbc.Row([
    #    dbc.Col(html.Div("Auction for 2023", className="bg-primary p-1 mt-2 text-center h2"))
    #]),

    #html.Hr(),

    dbc.Row(
        [
            dbc.Col(
                [
                    sidebar
                ], xs=4, sm=4, md=2, lg=2, xl=2, xxl=2),

            dbc.Col(
                [
                    dash.page_container
                ], xs=8, sm=8, md=10, lg=10, xl=10, xxl=10)
        ]
    )
], fluid=True)


if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8080)
    server = app.server


 #dbc.Col(html.Div("Auction for 2023",
 #                        style={'fontSize':50, 'textAlign':'center'}))
