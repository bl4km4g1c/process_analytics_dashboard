import dash
import dash_core_components as dcc
import dash_html_components as html
import data as dg
import datetime as dt
import pandas as pd
from dash.dependencies import Input, Output
from overview_page import overview_page

####import my scripts
from app_backend import app
from homepage import Homepage
from charts_page import charts_page


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
    if pathname == '/homepage':
        return Homepage()
    if '360' in pathname or '4010' in pathname:
        if '/control_chart' in pathname:
            return charts_page()
        else: 
            return overview_page()
    else:
        return Homepage()
    


#run server
if __name__ == '__main__':
    app.run_server(host = '0.0.0.0', port=3000, debug=True)