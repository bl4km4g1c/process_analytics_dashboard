# import dash
# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import base64
from navbar import Navbar
# from app_backend import app
from card_generator import card_template
from data import _datagen_ as dg


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


line_list = dg.data_request("/workspace/Python_Main/myApp/Resources/Index.csv")

line_list = line_list.values.tolist()


# function to kill duplicates


def remove_duplicates(line_list):
    unique_list = []
    output_list = []
    for entry in line_list:
        if entry[1] not in unique_list:
            unique_list.append(entry[1])
            output_list.append(entry)
        else:
            None
    return output_list


homepage_list = remove_duplicates(line_list)


# function to create list of cards for population in home page

line_cards = []
for entry in homepage_list:
    image_path = entry[2]
    # print(image_path)
    line_cards.append(card_template(entry[1], image_path))

# create body of home page

body = dbc.Container([
    dbc.Row(
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

