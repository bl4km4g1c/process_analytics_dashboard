import dash
import dash_core_components as dcc
import dash_html_components as html
import data as dg
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output

####import my scripts
from app_backend import app
from homepage import Homepage
#from control_chart import Control_Chart, graph_cc
#from control_chart import app_cc, sixty_two
from charts_page import sixty_one, sixty_two
####print version of dash
print ("Dash core components version " , dcc.__version__)


######pull / generate random data
#create one dataframe / csv file eventually --- mysql???? see charts page
#def create_data():
#    df = dg.generate_data(1000, 5)
#    df2 = dg.create_control_data(df)
#    print ("Data requested @ {}".format(dt.datetime('YYYY/MM/DD %hh:%mm:%ss')))
#    df.to_csv('Python_Main/assets/df.csv', index=False, header=False)
#    df2.to_csv('Python_Main/assets/df2.csv', index=False, header=False)
#    return
    
#create_data()

app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
             [Input('url', 'pathname')]
             )
def display_page(pathname):
    #if pathname == '/control_chart':
    #    return app_cc()
    if pathname == '/homepage':
        return Homepage()
    if pathname == '/360-1':
        return sixty_one()
    if pathname == '/360-2':
        return sixty_two()
    #if pathname == '/360_2':
    #    return sixty_two()
    else:
        return Homepage()
    
#card button callback
#@app.callback(Output('page-content', 'children'),
#             [Input('url', 'pathname')])
#def 
    
# #display images
# @app.callback(Outut('image-content', 'children'),
#              [Input('url', 'pathname')])

# def display_image(pathname):
#     if image == ''

#run server
if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port=3000, debug=True)