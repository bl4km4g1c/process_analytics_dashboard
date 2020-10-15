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
from data import _datagen_ as dg
from string_parser import _stringparser_ as sp


nav = Navbar()


####define header for body page

header = html.Div([
    html.P(),
    html.H1(id='charts-page-name'),
    html.H1(id='chart-page-filter'),
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

#code to import data for test runs

df = pd.read_csv("/workspace/Python_Main/myApp/dfmaster.csv")
df2 = pd.read_csv("/workspace/Python_Main/myApp/dfmaster2.csv")

df = df.set_index(['Datetime'])
df2 = df2.set_index(['Datetime'])


#Define figures for control chart

fig = control_chart(df, df2)
fig2 = histogram(df,df2)


def charts_page():
    layout = html.Div([
        nav,
        header,
        display_body(fig)
    ])
    return layout

measure_list = dg.data_request("https://raw.githubusercontent.com/bl4km4g1c/process_analytics_dashboard/master/Index.csv?_sm_au_=isVZpQZkR1qq4jSNpGsWvKttvN1NG")

measure_list = measure_list.values.tolist()

#function to kill duplicates
def remove_duplicates(measure_list, meas_filter, comp_filter):
    unique_list = []
    output_list = []
    for entry in measure_list:
        if entry[1] == comp_filter and entry[4] == meas_filter and entry[4] not in unique_list:
            unique_list.append(entry[6])
            output_list.append(entry[7])
        else:
            None
    return output_list

#callback to pull out href name
@app.callback(Output('charts-page-name', 'children'),[
   Input('url', 'pathname')])

def display_page_name(pathname):
    #display path name if control chart is in title  
    if '/control_chart' in pathname:
        return sp.chart_titles(pathname)
    else:
        return None

###callback to get pathname split correctly and to update data based on this
@app.callback(Output('chart-page-filter', 'children'),[
   Input('url', 'pathname')])
def chart_page_filter(pathname):
    
    if '/control_chart' in pathname:
        measure_name, comp_filter = sp.filter_control(pathname)
        print (pathname)
        print (measure_name)
        print (comp_filter)

        measures = remove_duplicates(measure_list, measure_name, comp_filter)
        
        #loop through measures and find / except all measures which arent included
        index = 0
        successful_tries = []
        for measure in measures:
            print (measure)
            try:
                print (df[measures[index]])
                successful_tries.append(measures[index])
            except Exception:
                print ('{} measure not found in this set'.format(measure))
            #step through the index until the last
            index = index + 1
        print (successful_tries)
        print (df[successful_tries])
        
        df = df[successful_tries]
        
        
        return None
    