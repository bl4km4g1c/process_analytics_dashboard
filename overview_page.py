import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from navbar import Navbar
from app_backend import app 
from dash.dependencies import Input, Output
from card_generator import card_template, card_template_overview

nav = Navbar()

#create header for overview page
header = html.Div([
    html.P(),
    html.H1(id='page-name'),
    html.P()
])

#line components master list for all components in line  - create cards for overview - placeholder
component_list = [["360-2", "Process 1", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
                 ["360-2", "Process 2", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
                 ["360-1", "Process 1", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
                  ["360-1", "Process 2", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
                  ["360-2", "Process 3", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
                  ["360-2", "Process 4", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"]
                 ]

body = html.Div(id = 'card-overview')

#define overview page function and generate when called from index script
def overview_page():
    layout = html.Div([
        nav,
        header,
        body
    ])
    return layout

#callback for creating dynamic process_cards
@app.callback(Output('card-overview', 'children'),[
              Input('url', 'pathname')])

def make_card(pathname):
    
    process_cards = []
    for entry in component_list:
        if pathname.strip('/') == entry[0]:
            process_cards.append(card_template_overview(entry[0], entry[1], entry[2]))
        else:
            None
        
        body = dbc.Container([
        dbc.Row(#[
            process_cards
            )

        ])
    
    return body

#callback to pull out href name
@app.callback(Output('page-name', 'children'),[
   Input('url', 'pathname')])

def display_page_name(pathname):
    if '/control_chart' in pathname:
        None
    else:
        return  "Overview page for {} CPPs".format(pathname.strip('/'))