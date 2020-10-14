import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from navbar import Navbar
from app_backend import app 
from card_generator import card_template


nav = Navbar()


####define body of home Homepage

header = html.Div([
    html.P(),
    html.H1("Homepage"),
    html.P(),
    html.H4("Overview"),
    html.P(),
    html.P("This application is designed to show continuous CPP charting and raise alerts when any issue is found. Please select the 'control chart' page for further detail.")
])


#card docs https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/

#body = html.Div(html.Img(src = app.get_asset_url('download.png')))

#place holder list of lines for producing homepage cards

line_list = [["360-1","https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"], 
             ["360-2","https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
             ["4010-1","https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
             ["4010-2", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
             ["4010-3", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
             ["4010-4", "https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"],
             ["4010-5","https://upload.wikimedia.org/wikipedia/en/9/92/Pok%C3%A9mon_episode_1_screenshot.png"]]


#function to create list of cards for population in home page

line_cards = []
for entry in line_list:
    line_cards.append(card_template(entry[0], entry[1]))
    
#create body of home page
    
body = dbc.Container([
    dbc.Row(#[
        line_cards
    )
       
])

def Homepage():
    layout = html.Div([
        nav,
        header,
        body
    ])
    return layout

