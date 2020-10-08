import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

####import my scripts
from app_backend import app
from homepage import Homepage
#from control_chart import Control_Chart, graph_cc
#from control_chart import app_cc, sixty_two
from charts_page import sixty_one

####print version of dash
print ("Dash core components version " , dcc.__version__)


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
    if pathname == '/360_1':
        return sixty_one()
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