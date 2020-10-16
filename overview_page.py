# import dash
# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import base64
from navbar import Navbar
from app_backend import app
from dash.dependencies import Input, Output
from card_generator import card_template, card_template_overview
from data import _datagen_ as dg
import datetime as dt


nav = Navbar()

# create header for overview page
header = html.Div([
    html.P(),
    html.H1(id='page-name'),
    html.P()
])


body = html.Div(id='card-overview')

component_list = dg.data_request("/workspace/Python_Main/myApp/Resources/Index.csv")

component_list = component_list.values.tolist()

# function to kill duplicates


def remove_duplicates(line_list, comp_filter):

    unique_list = []
    output_list = []
    for entry in line_list:
        if entry[1] == comp_filter and entry[4] not in unique_list:
            unique_list.append(entry[4])
            output_list.append(entry)

        else:
            # print ('{} not equal to {}'.format(entry[1]), str(comp_filter))
            None

    return output_list

# callback for creating dynamic process_cards


@app.callback(Output('card-overview', 'children'), [
              Input('url', 'pathname')])
def make_card(pathname):
    time_math_1 = dt.datetime.now()
    process_cards = []
    pathname = pathname.strip('/')

    # Generate card data
    new_list = remove_duplicates(component_list, pathname)
    for entry in new_list:
        if pathname == entry[1]:
            process_cards.append(card_template_overview(entry[1],
                                                        entry[4],
                                                        entry[5]))
            # print(new_list)
        else:
            None
    
    body = dbc.Container([
        dbc.Row(
            process_cards
            )
        ])
    time_math_2 = dt.datetime.now() - time_math_1
    print ("Cards created in {}".format(time_math_2))
    return body

# callback to pull out href name


@app.callback(Output('page-name', 'children'), [
   Input('url', 'pathname')])
def display_page_name(pathname):
    if '/control_chart' in pathname:
        None
    else:
        return "Overview page for {} CPPs".format(pathname.strip('/'))


# define overview page function and generate when called from index script


def overview_page():
    layout = html.Div([
        nav,
        header,
        body
    ])
    return layout

