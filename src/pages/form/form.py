import dash_bootstrap_components as dbc
from dash import html
import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__,
                   path='/bidding',
                   name='Bidding',
                   title='Bidding',
                   #image='pg3.png',
                   description='Placing Your Bid.'
)

email_input = html.Div(
    [
        dbc.Label("Email", html_for="example-email"),
        dbc.Input(type="email", id="example-email", placeholder="Enter email"),
        dbc.FormText(
            "Please Input our registerd Email",
            color="secondary",
        ),
    ],
    className="mb-3",
)

bid_input = html.Div(
    [
        dbc.Label("Bid", html_for="example-bid"),
        dbc.Input(
            type="float",
            id="example-bid",
            placeholder="Enter Bid",
        ),
        dbc.FormText(
            "This is your bid amount ", color="secondary"
        ),
    ],
    className="mb-3",
)

layout = dbc.Form([email_input, bid_input])





