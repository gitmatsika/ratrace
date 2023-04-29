import dash_bootstrap_components as dbc
from dash import callback, Output, Input
import dash
from dash import dcc, html
from classBid import *

mybid =Mybid()
bids = mybid.readtolist()

dash.register_page(__name__,
                   path='/Place',
                   name='Place',
                   title='New heatmaps',
                   #image='pg3.png',
                   description='Placing Your Bid.'
)

email_input = dbc.Row([
        dbc.Label("Email"
                , html_for="email-row"
                , width=2),
        dbc.Col(dbc.Input(
                type="email"
                , id="email-row"
                , placeholder="Enter email"
            ),width=10,
        )],className="mb-3"
)
user_input = dbc.Row([
        dbc.Label("Amount", html_for="bib-row", width=2),
        dbc.Col(
            dbc.Input(
                type="number"
                , id="amt-row"
                , placeholder="Enter Amount"
                , maxLength = 80
            ),width=10
        )], className="mb-3"
)
message = dbc.Row([
        dbc.Label("Name", html_for="message-row", width=2),
        dbc.Col(
            dbc.Input(
                type="Text",
                id = "person-row"
                , placeholder="Enter name"
            ), width=10,
        )], className="mb-3")

markdown = ''' # Please place your bid here!'''
form = html.Div([ dbc.Container([
            dcc.Markdown(markdown)
            , html.Br()
            , dbc.Card(
                dbc.CardBody([
                     dbc.Form([email_input
                        , user_input
                        , message])
                ,html.Div(id = 'div-button', children = [
                    dbc.Button('Submit'
                    , color = 'primary'
                    , id='button-submit'
                    , n_clicks=0)
                ]) #end div
                ])#end cardbody
            )#end card
            , html.Br()
            , html.Br()
        ])
        ])


header = html.Div("Auction", className="h2 p-2 text-white bg-primary text-center")

layout = dbc.Container(
            [
                header,
                form,
            ],
            )




#layout = form

@callback(Output('div-button', 'children'),
         Input("button-submit", 'n_clicks')
         , Input("email-row", 'value')
         , Input("amt-row", 'value')
         , Input("person-row", 'value')
         )
def process_bid(n, email, bid, person):
    print(email, person, bid)
    print("testing")
    if n > 0:
        #return "Nothing added"
        #n=10
        print(email, person, bid)
        try:
            bids = mybid.readtolist()
            auction = mybid.newbid(bids, email, person, bid)
            mybid.toCsv(auction)
        except NameError as err:
            auction = []
            auction = mybid.newbid(auction, email, person, bid)
            mybid.toCsv(auction)
            print("i am here")
            print(auction)
        return [html.P("Bid Accepted")]
    else:
        #return "Thank you"


        return [dbc.Button('Submit', color='primary', id='button-submit', n_clicks=0)]




