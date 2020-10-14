import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import base64
from navbar import Navbar
from app_backend import app 


#create cards for homepage
def card_template(id_name, image_path):
    
    card = dbc.Card(
                [
                    dbc.CardImg(src=image_path, top = True),
                    dbc.CardBody(
                    [
                        html.H4(id_name, className="card-title"),
                        html.P(
                            "This page contains the CPPs for {}".format(id_name),
                            className = "card-text",
                        ),
                       dbc.Button("Go to: Machine {}".format(id_name), color = "primary", id="{}-button".format(id_name), href='/{}'.format(id_name)),
                    ]
                    )

                ]
            )
    
    return card

#create cards for overview page
def card_template_overview(id_name, process_name, image_path):
    
    card = dbc.Card(
                [
                    dbc.CardImg(src=image_path, top = True),
                    dbc.CardBody(
                    [
                        html.H4(process_name, className="card-title"),
                        html.P(
                            "Click for detailed information on {}".format(process_name),
                            className = "card-text",
                        ),
                       dbc.Button("Go to: {}".format(process_name), color = "primary", id="{}-button".format(process_name), href='/{}/{}/control_chart'.format(id_name,process_name)),
                    ]
                    )

                ]
            )
    
    return card