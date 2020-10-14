import dash
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from navbar import Navbar
import dash_bootstrap_components as dbc
from data import _datagen_ as dg
from charts import control_chart, histogram
from app_backend import app
from dash.dependencies import Input, Output

nav = Navbar()


####define header for body page

header = html.Div([
    html.P(),
    html.H1(id='charts-page-name'),
    html.P()
])

###create body for the page
#-------------------------------need to adjust the figure height next 

def display_body(fig):
    body = html.Div(
        [ 
          dbc.Row(
               [
                   dbc.Col([
                       html.H4("Control Chart"),
                       dcc.Graph(id = 'cc-graph', figure=fig)], 
                       width= "auto", xs = 12, md=8, lg = 10),
                   dbc.Col([
                       html.H4("Histogram"),
                       dcc.Graph(id = 'hist-plot', figure=fig2)],
                       width = "auto", xs=12, md = 4, lg = 2),
               ],
               no_gutters = True
           )
        ])
    return body

#code to generate_data for test runs
df = dg.generate_data(1000, 10)
df2 = dg.create_control_data(df)
fig = control_chart(df, df2)
fig2 = histogram(df)


def charts_page():
    layout = html.Div([
        nav,
        header,
        display_body(fig)
    ])
    return layout

#callback to pull out href name
@app.callback(Output('charts-page-name', 'children'),[
   Input('url', 'pathname')])

def display_page_name(pathname):
    if '/control_chart' in pathname:
        return  "{} Control Charts".format(pathname.strip('/control_chart'))
    else:
        return  None
    