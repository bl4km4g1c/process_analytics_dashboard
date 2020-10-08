import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from navbar import Navbar
from app_backend import app 

def card_template(image_path, text1):
    
    card = dbc.Card(
                [
                    dbc.CardImg(src=image_path, top = True),
                    dbc.CardBody(
                    [
                        html.H4(text1, className="card-title"),
                        html.P(
                            "This page contains the CPPs for {}".format(text1),
                            className = "card-text",
                        ),
                        dbc.Button("Go to: Machine {}".format(text1), color = "primary"),
                    ]
                    )

                ]
            )
    
    return card