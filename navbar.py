import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import datetime as dt
from app_backend import app
from dash.dependencies import Input, Output
import pytz


@app.callback(Output('live-update-time', 'children'), [
    Input('interval-component', 'n_intervals')])

def update_date(n):
    d = dt.datetime.now(pytz.timezone('Australia/Sydney')).strftime('%Y-%m-%d %HH:%MM')
    #timezone = pytz.timezone('Australia/Sydney')
    #d_aware = timezone.localize(d)
    time = str(d)
    return html.H5('Last updated {}'.format(time),
                  style = {
                      'textAlign': 'right',
                      'color': 'white',
                      'vertical-align': 'bottom',
                      'margin-top': '15px'
                  }
                  )


def Navbar():
    
    layout = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Report", href = '/report_page')),
            dbc.NavItem(dbc.NavLink("Information", href = '/info')),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More Pages",header=True),
                    dbc.DropdownMenuItem("New Page", href = '/info')
                ],
                nav=True,
                in_navbar=True,
                label = "More"
            ),
            html.P(id = 'live-update-time'),
            dcc.Interval(id = 'interval-component',
                         interval = 1*5000, #milliseconds
                         n_intervals = 0)
        ],
        brand = "Homepage",
        brand_href = '/homepage',
        color = "primary",
        fluid = True,
        dark=True
    )
    
    return layout
