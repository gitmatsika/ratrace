import dash
from dash import dcc, html, callback, Output, Input
import plotly.express as px
import dash_bootstrap_components as dbc

import pandas as pd

# To create meta tag for each page, define the title, image, and description.
dash.register_page(__name__,
                   path='/',  # '/' is home page and it represents the url
                   name='Bid History',  # name of page, commonly used as name of link
                   title='Index',  # title that appears on browser's tab
                   #image='pg1.png',  # image in the assets folder
                   description='Histograms are the new bar charts.'
)

# page 1 data
def toCsv(bid):
    df = pd.DataFrame(bid)
    df.to_csv("data/auction.csv", index=False)

def months(data):
    all_months: list[str] = data['month'].tolist()
    unique_months = sorted(set(all_months))
    return unique_months



#unique_years = [2023]

def readtolist():
    df = pd.read_csv('/data/auction.csv')
    auction = df.to_dict('records')
    return auction
data =pd.read_csv('../data/auction.csv')
data['time']=pd.to_datetime(data['time'])
data =pd.read_csv('../data/auction.csv')
data['time']=pd.to_datetime(data['time'])
#print(data)
data = data[['amt', 'time', 'name']]
data['day'] = data['time'].dt.day
data['month'] = data['time'].dt.month
data['year'] = data['time'].dt.year
unique_months = months(data)
all_years = data['year'].tolist()
unique_years = sorted(set(all_years), key=int)

col1 = html.Div(
               children=[
                       html.Span(dbc.Badge("Year", pill=True, color="primary", className="me-1")),
                        #html.Div(children="Year", className="menu-title"),
                        dcc.Dropdown(
                            id="year-filter",
                            options=[
                                {"label": Year, "value": Year} for Year in unique_years],
                            #value="2023",
                            clearable=False,
                            className="w-25 p-3 bg-light border",
                        ),
                    ],
                )

col2 = html.Div(
                    children=[
                        html.Span(dbc.Badge("Month", pill=True, color="secondary", className="me-1")),
                        #html.Div(children="Month", className="menu-title"),
                        dcc.Dropdown(id="month-filter",
                                     options=[
                                         {"label": Username, "value": Username} for Username in unique_months
                                     ],
                                     #value="3",
                                    clearable=False,
                                    # searchable=False,
                                    className="w-25 p-3 bg-light border",
                                    ),
                        ],
                    )

col3=  html.Div(
                    children=dcc.Graph(
                        id="auction-chart",
                        config={"displayModeBar": False},),
                    className="card",
                )
col4= html.Div(children=dcc.Graph(
                        id="highest-chart",
                        config={"displayModeBar": False},
                        #figure="fig1",
                    ),
                    className="card",
                )

col5 = html.Div(html.H1(
            children="Highest Bidder for the bid : ", className="header-title"))
row = dbc.Row(
    [
        dbc.Col(col1, align="center", class_name="ms-1"),
        dbc.Col(col2, className="ms-1"),
    ]
    )
row1 = dbc.Row(
                [
                   dbc.Col(col3),
                   dbc.Col(col4),
                ],
             )
header = html.Div("Auction", className="h2 p-2 text-white bg-primary text-center")

layout = dbc.Container(
            [
                header,
                row,
                row1,
            ],
            )



@callback(

    Output("auction-chart", "figure"),
    Output("highest-chart", "figure"),
    Input("year-filter", "value"),
    Input("month-filter", "value"),

)
def update_charts(year, month):
    filtered_data = data.query(
        "year == @year and month == @month"
    )
    if filtered_data.shape[0] == 0:
        return html.Div("No Data Selected")
    auction_chart_figure = {
        "data": [
            {
                "x": filtered_data["name"],
                "y": filtered_data["amt"],

                "type": "bar",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Auction",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "colorway": ["#17B897"],
            "xaxis": {"title": "Bidder"},
            "yaxis": {"title": "Amount"},
        },
    }

    pt = filtered_data.pivot_table(
        values="amt",
        index=["day"],
        aggfunc="max",
        fill_value=0
    )
    pt = pt.reset_index().sort_values("amt", ascending=False)
    highest_chart_figure = {
        "data": [
            {
                "x": pt["day"],
                "y": pt["amt"],

                "type": "bar",
                "hovertemplate": "$%{y:.2f}<extra></extra>",
            },
        ],
        "layout": {
            "title": {
                "text": "Auction",
                "x": 0.05,
                "xanchor": "left",
            },
            "xaxis": {"fixedrange": True},
            "yaxis": {"tickprefix": "$", "fixedrange": True},
            "xaxis": {"title": "Day"},
            "yaxis": {"title": "Amount"},
            # "colorway": ["#17B897"],

        },
    }
    print(data)
    return auction_chart_figure, highest_chart_figure

































