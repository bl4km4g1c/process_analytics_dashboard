import dash
import numpy as np
import pandas as pd
import dash_daq as daq
import pytz
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import datetime as dt
#from datetime import date, timedelta

from navbar import Navbar
import dash_bootstrap_components as dbc
from data import _datagen_ as dg
from charts import control_chart, histogram
from app_backend import app
from dash.dependencies import Input, Output
from data import _datagen_ as dg
from string_parser import _stringparser_ as sp


# ### Define navigation bar ###

nav = Navbar()

# ### Define header for body page ###

header = html.Div([
    html.P(),
    html.H1(id='charts-page-name'),
    html.P(),
])

# function to kill duplicates


def remove_duplicates(measure_list, meas_filter, comp_filter):

    unique_list = []
    output_list = []
    for entry in measure_list:
        if entry[1] == comp_filter and entry[4] == meas_filter and entry[4] not in unique_list:
            unique_list.append(entry[6])
            output_list.append(entry[7])
        else:
            None
    return output_list, unique_list

#create selection dropdown
dropdown = html.Div([
    dcc.Dropdown(
        id = 'time-dropdown',
        options = [
            {'label': "Last Hour", "value": 1},
            {'label': "Last Shift", "value": 12},
            {'label': "Last Day", "value": 24}
        ],
        value = 1
    )
])


# #################### CALLBACK FUNCTIONS #######################
# ###############################################################

# Callback to pull out href name


@app.callback(Output('charts-page-name', 'children'), [
   Input('url', 'pathname')])
def display_page_name(pathname):

    # Display path name if control chart is in title
    if '/control_chart' in pathname:
        return sp.chart_titles(pathname)
    else:
        return None

# ### Callback to get pathname split correctly and to update data based on this


@app.callback([
    Output('chart-page-filter', 'figure'),
    Output('histo-page-filter', 'figure')],
    [Input('url', 'pathname'),
    Input('time-dropdown', 'value'),
    Input('interval-component', 'n_intervals')
    ])
def chart_page_filter(pathname, hours, n):
    
    # ### Code to import data and measure list ###

    df = pd.read_csv("/workspace/Python_Main/myApp/dfmaster.csv")
    df2 = pd.read_csv("/workspace/Python_Main/myApp/dfmaster2.csv")
    measure_list = dg.data_request("/workspace/Python_Main/myApp/Resources/Index.csv")


    # Set Index for imported data
    df = df.set_index(['Datetime'])
    df2 = df2.set_index(['Datetime'])


    # Send measures to list
    measure_list = measure_list.values.tolist()    

    if '/control_chart' in pathname:
        time_math_1 =  dt.datetime.now()
        measure_name, comp_filter = sp.filter_control(pathname)
        print(pathname)
        print(measure_name)
        print(comp_filter)

        measures, measure_names = remove_duplicates(measure_list,
                                                    measure_name,
                                                    comp_filter)
        
                
        # Loop through measures and find / except all measures which arent included
        index = 0
        successful_tries = []
        for measure in measures:
            # print (measure)
            try:
                print (df[measures[index]])
                successful_tries.append(measures[index])
            except Exception:
                print('{} measure not found in this set'.format(measure))
            # Step through the index until the last
            index = index + 1
        #print (successful_tries)
        # print (df[successful_tries])

        # filter df and set new df
        new_df = df[successful_tries]
        
        new_df2 = dg.modify_df2(df2, successful_tries)
        #print(new_df2)
        # check through data for df2 to ensure only correct columns are included
        
        
        #choose start date for the time filter - #### this is not fully working cannot look back past midnight currently
        start_date = (dt.datetime.now(pytz.timezone('Australia/Sydney')) - dt.timedelta(hours = hours )).strftime('%Y-%m-%d %H:%M:%S')
        new_df, new_df2 = dg.dropdown_times(new_df, new_df2, start_date)
        # Define figures for control chart
        time_math_2 = dt.datetime.now() - time_math_1
        print ("Math updated in {}".format(time_math_2))
        fig = control_chart(new_df, new_df2, measure_names)
        fig2 = histogram(new_df)

        # create body for callback output #

        return fig, fig2

# ################# create body for the page ########################
# ###################################################################

# ------------------------------need to adjust the figure height next


body = html.Div(
    [
      dbc.Row(
           [
               dbc.Col([
                   html.H4("Control Chart"),
                   dcc.Graph(id='chart-page-filter')],
                   width="auto", xs=11, md=7, lg=7),

               dbc.Col([
                   html.H4("Histogram"),
                   dcc.Graph(id='histo-page-filter')],
                   width="auto", xs=12, md=4, lg=2),
           ],
           no_gutters=True
       )
    ])


def charts_page():
    layout = html.Div([
        nav,
        dropdown,
        #date_picker,
        #time_picker,
        header,
        body
    ])
    return layout


