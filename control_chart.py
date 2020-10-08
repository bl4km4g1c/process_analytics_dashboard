# no longer using this tool

import dash
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from navbar import Navbar
import dash_bootstrap_components as dbc
from data import _datagen_

nav = Navbar()


####define body of control chart

header = html.Div([
    html.P(),
    html.H1("SPC Process Charts"),
    html.P()
])

##sparklines for data - need to complete this.... how to get data in correct format??? maybe generate seperate DF?
def sparklines(df):
    fig = px.line(df, facet_row = "machine")
    
    #lock axes and hide
    fig.update_xaxes(visible=False, fixedrange=True)
    fig.update_yaxes(visible = False, fixedrange = True)
    
    #remove facet/subplot labels
    fig.update_layout(showlegend = False, annotations=[], overwrite = True)
    
    #disable modebar 
    fig.show(config = dict(displayModeBar=False))

    return fig

###figure for control chart

def control_chart(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x= df['x'],y = df['data'] , mode='lines+markers',
                            name='data', line = dict(color='royalblue', width=2)))
    fig.add_trace(go.Scatter(x=df['x'],y= df['x_bar'],mode='lines',name='x_bar', line = dict(color='royalblue', width=2, dash='dot')))
    fig.add_trace(go.Scatter(x=df['x'],y= df['UCL'],mode='lines', name='UCL', line = dict(color='firebrick', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=df['x'],y= df['LCL'],mode='lines',name='LCL', line = dict(color='firebrick', width=2, dash='dash')))
    fig.add_trace(go.Scatter(x=df['x'],y= df['Viol'],mode='markers',name='Violation', marker=dict(size = 10, color='tomato', opacity=0.5, symbol='circle-open')))
    #fig.add_trace(go.Scatter(x = df['x'],y = df['random_y2'], mode='markers',                    name='markers'))
    fig.update_layout(
        xaxis_title_text = 'Sample #',
        yaxis_title_text = 'Value',
        autosize= True
    )
    fig.show()
    
    return fig

def hist_chart(df):
     ###figure for histogram
    group_labels = ['Test']
    #fig2 = ff.create_distplot([df['data']], group_labels) #this is a distplot not a histogram - histogram is using GO
    fig = go.Figure()
    fig.add_trace(go.Histogram(y=df['data']))
    fig.update_layout(
        xaxis_title_text = 'Count',
        autosize= True
        )
    fig.show()
    
    return fig 

# ###create body for the page
# def display_body(fig, fig2, fig3):
#     body = html.Div(
#         [
#         dbc.Row([
#               dbc.Col(dcc.Graph(id='sparky_g', figure= fig3), width="auto", xs=12, md=12, lg=12)
#           ]), 
#           dbc.Row(
#                [
#                    dbc.Col([
#                        html.H4("Control Chart"),
#                        dcc.Graph(id = 'cc-graph', figure=fig)], 
#                        width= "auto", xs = 12, md=8, lg = 10),
#                    dbc.Col([
#                        html.H4("Histogram"),
#                        dcc.Graph(id = 'hist-plot', figure=fig2)],
#                        width = "auto", xs=12, md = 4, lg = 2),
#                ],
#                no_gutters = True
#            )
#         ])
#     return body

###generate figures

df = data(1000)
df2 = spark(1000)

fig1 = control_chart(df)
fig2 = hist_chart(df)

#sparklines current using different data source, need to rework data generations into classes to split more efficiently

fig3 = sparklines(df2)


def app_cc():
    layout = html.Div([
        nav,
        header,
        display_body(fig1, fig2, fig3)
    ])
    return layout

def sixty_one():
    layout = html.Div([
        nav,
        header,
        display_body(fig1, fig2, fig3)
    ])
    return layout

def sixty_two():
    layout = html.Div([
        nav,
        header,
        display_body(fig1, fig2, fig3)
    ])
    return layout