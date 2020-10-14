import dash
import numpy as np
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from navbar import Navbar
import dash_bootstrap_components as dbc
from data import _datagen_ as dg

def control_chart(df, df2):

    #find array shape of 1st df
    length, width = df.shape
    #find array shape of 2nd df
    length2, width2 = df2.shape
    size = int(width2/width)
    print(size)
    print(df2.shape)
    print(df.shape)
    #initialise figure
    #fig = go.Figure()
    #initialise subplots figure - is subplots better than new plot????? - if subplots look bad change to add new plot instead
    fig = make_subplots(rows = width, cols=1 )
    
    #initialise colour list for loop
    c = ['royalblue', 'firebrick', 'firebrick', 'darkviolet', 'darkviolet']
    #initialise list for type of markers
    l = ['dot', 'dash', 'dash', 'dash']
    
    #variable size data overlay generator
    for i in range(width):
        #change from chart to subplot ....
        fig.add_trace(go.Scatter(x= df.index,y = df.iloc[:,i] , mode='lines',
                                name='Measure {}'.format(i+1), line = dict(color="forestgreen", width=2)),
                                 row=i+1, col =1)
        for j in range(size):
            if j%4==0 and not j ==0:
                fig.add_trace(go.Scatter(x= df.index,y = df2.iloc[:, j+5*i] , mode='markers',
                                   name='{}'.format(df2.columns[j+5*i]), marker=dict(size = 5, color='tomato', opacity=1, symbol='circle')),
                                    row=i+1, col=1)
                print(j)
            elif j==1 and not j ==0:
                print ("No print on this line")
            else:
                fig.add_trace(go.Scatter(x= df.index,y = df2.iloc[:, j+5*i] , mode='lines',
                                   name='{}'.format(df2.columns[j+5*i]), line = dict(color=c[j], width=2, dash = l[j])),
                                 row = i+1, col=1)
                
    #change layouts to work with subplotting to make fully modular
    fig.update_layout(
        xaxis_title_text = 'Sample #',
        yaxis_title_text = 'Value',
        autosize= True,
        height = width*300, ####need to fetch screen size with html so this is a variable
        showlegend = False
    )
    fig.show()
    
    return fig

def histogram(df,df2):
    #shape
    length, width = df.shape
    length2,width2 = df2.shape
    
    size = int(length2/length)
    ###figure for histogram
    group_labels = ['Test']
    #fig2 = ff.create_distplot([df['data']], group_labels) #this is a distplot not a histogram - histogram is using GO
    fig = make_subplots(rows = width, cols = 1)
    for i in range(width):

        # for j in range(size):
                       
        #     if j%4==0 and not j==0:
                
        #         if df2.iloc[:, j+5*i] is not None:
        #             fig.add_trace(go.Histogram(y=df2.iloc[:,j+5*i], marker=dict(color = "tomato")), row = i+1, col =1)
                    
        #         else: 
                    fig.add_trace(go.Histogram(y=df.iloc[:,i], marker=dict(color = "forestgreen")),row = i+1, col =1)

#        for j in range(size):
#            if j%==0 and not j==0:
#                fig.add_trace(go.Histogram(y = df2.iloc[,j+5*i], row = i+1, col=1))
        
    fig.update_layout(
        xaxis_title_text = 'Count',
        autosize= True,
        height = width*300,
        showlegend = False
        )
    fig.show()
    
    return fig 


