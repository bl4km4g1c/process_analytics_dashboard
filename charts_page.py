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

nav = Navbar()


####define header for body page

header = html.Div([
    html.P(),
    html.H1("SPC Process Charts"),
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


#write code for main page here to pull data and such

df = dg.generate_data(1000, 5)
df2 = dg.create_control_data(df)
fig = control_chart(df, df2)
fig2 = histogram(df)

def sixty_one():
    layout = html.Div([
        nav,
        header,
        display_body(fig)
    ])
    return layout