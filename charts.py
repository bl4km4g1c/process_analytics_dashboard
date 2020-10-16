# import dash
# import dash_daq as daq
# import numpy as np
# import pandas as pd
# import dash_core_components as dcc
# import dash_html_components as html
import plotly.graph_objects as go
# import plotly.express as px
from plotly.subplots import make_subplots
import datetime as dt
# from navbar import Navbar
# import dash_bootstrap_components as dbc
# from data import _datagen_ as dg
# import dash_daq as daq


def control_chart(df, df2, measure_names):
    time1 = dt.datetime.now()
    # find array shape of 1st df
    length, width = df.shape

    # find array shape of 2nd df
    length2, width2 = df2.shape

    # Calculate relative size of data set vs calculations
    size = int(width2/width)
    print(size)
    print(df2.shape)
    print(df.shape)

    # initialise figure
    # fig = go.Figure()
    # initialise subplots figure - is subplots better than new plot?????
    # ... if subplots look bad change to add new plot instead

    fig = make_subplots(rows=width,
                        cols=1,
                        subplot_titles=measure_names)

    # initialise colour list for loop
    # ###c = ['royalblue', 'firebrick', 'firebrick', 'darkviolet', 'darkviolet', 'darkviolet']

    # initialise list for type of markers
    # ###l = ['dot', 'dash', 'dash', 'dash', 'dash', 'dash']

    # variable size data overlay generator
    
    for i in range(width):
        # change from chart to subplot ....
        fig.add_trace(go.Scatter(x=df.index, y=df.iloc[:, i],
                                 mode='lines',
                                 name='Measure {}'.format(i+1),
                                 line=dict(color="forestgreen",
                                 width=2)), row=i+1, col=1)

        for j in range(size):
            if j % 4 == 0 and not j == 0:
                fig.add_trace(go.Scatter(x=df.index, y=df2.iloc[:, j+size*i],
                                         mode='markers',
                                         name='{}'.format(df2.columns[j+size*i]),
                                         marker=dict(size=5, color='tomato',
                                         opacity=1, symbol='circle')),
                              row=i+1,
                              col=1)
                print(j)

            elif j == 1 and not j == 0:

                print("No print on this line")

            else:

                fig.add_trace(go.Scatter(x=df.index,
                                         y=df2.iloc[:, j+size*i],
                                         mode='lines',
                                         name='{}'.format(df2.columns[j+size*i]),
                                         line=dict(color='royalblue',
                                                   width=2,
                                                   dash='dash')),
                              row=i+1,
                              col=1)

    # change layouts to work with subplotting to make fully modular
    time_to_update_1 = dt.datetime.now() - time1
    print ("Figures updated in {}".format(time_to_update_1))
    
    fig.update_layout(
        xaxis_title_text='Sample #',
        yaxis_title_text='Value',
        autosize=True,
        height=width*300,
        # ###need to fetch screen size with html so this is a variable
        showlegend=False
    )
    fig.show()
    time_to_update_2 = dt.datetime.now() - time1
    print ("Figures shown in {}".format(time_to_update_2))
    return fig


def histogram(df):
    # shape
    length, width = df.shape

    fig = make_subplots(rows=width, cols=1)
    for i in range(width):

        fig.add_trace(go.Histogram(y=df.iloc[:, i],
                                   marker=dict(color="forestgreen")),
                      row=i+1,
                      col=1)

    fig.update_layout(
        xaxis_title_text='Count',
        autosize=True,
        height=width*300,
        showlegend=False
        )

    fig.show()

    return fig
