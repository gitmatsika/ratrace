import dash_bootstrap_components as dbc
from dash import html, callback, Output, Input
import dash
from dash import dcc, html
import plotly.express as px

dash.register_page(__name__,
                   path='/information',
                   name='Information',
                   title='Information',
                   #image='pg3.png',
                   description='Details'
)




form = dbc.Form(
    dbc.Row(
        [
            dbc.Label("Email", width="auto"),
            dbc.Col(
                dbc.Input(id="email-input",type="email", value="", placeholder="Enter email"),
                className="me-3",
            ),
            dbc.Label("Bid Amount", width="auto"),
            dbc.Col(
                dbc.Input(id="bid-input", type="float", value="", placeholder="Enter Amount"),
                className="me-3",
            ),
            dbc.Col(dbc.Button( "Submit", color="primary", n_clicks=0)),
        ],
        className="g-2",
        id="bid-form",
    )
)

layout = form

@callback(
    Output('bid-form', 'children'),
    Input("email-input", 'value'),
    Input("bid-input", 'value'),
    Input("submit-btn", 'n_clicks'),
)
def add_bid( mail, bid, n):
    if n is None:
        return "Nothing added"
    else:
        return "Thank you"





