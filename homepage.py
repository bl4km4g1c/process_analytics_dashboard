import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from navbar import Navbar
from app_backend import app 

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

#body for homepage
                
body = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src="Python_Main/assets/test_image.png", top = True),
                    dbc.CardBody(
                    [
                        html.H4("360/1", className="card-title"),
                        html.P(
                            "This page contains the CPPs for 360/1",
                            className = "card-text",
                        ),
                        dbc.Button("Go to: Machine 360/1", color = "primary", id="3601-button", href='/360_1'),
                    ]
                    )

                ]
            )
        ]),
        dbc.Col([
            dbc.Card(
                [
                    dbc.CardImg(src="Python_Main/assets/test_image.png", top = True),
                    dbc.CardBody(
                    [
                        html.H4("360/2", className="card-title"),
                        html.P(
                            "This page contains the CPPs for 360/2",
                            className = "card-text",
                        ),
                        dbc.Button("Go to: Machine 360/2", color = "primary", id="3602-button", href='/360_2'),
                    ]
                    )

                ]
            )
        ])
        ])
])

def Homepage():
    layout = html.Div([
        nav,
        header,
        body
    ])
    return layout

