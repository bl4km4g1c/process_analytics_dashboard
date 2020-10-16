# import dash
# import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
# import base64
# from navbar import Navbar
# from app_backend import app
import dash_daq as dq
from data import _datagen_ as dg
from charts_page import remove_duplicates as rd2
import pandas as pd

def RAG_Indicator(process_name, id_name):
        component_list = dg.data_request("/workspace/Python_Main/myApp/Resources/Index.csv").values.tolist()
        df = pd.read_csv("/workspace/Python_Main/myApp/dfmaster.csv").tail(1)
        component_list = component_list
        Measure_list, Measure_names = rd2(component_list, process_name, id_name)
        index = 0
        successful_tries = []
        for measure in Measure_list:
            try:
                print(df[Measure_list[index]].shape)
                successful_tries.append(Measure_list[index])
            except Exception:
                print('{} measure not found in this set'.format(measure))

                index = index + 1

        df2 = pd.read_csv("/workspace/Python_Main/myApp/dfmaster2.csv").tail(1)
        df = df[successful_tries]
        new_df2 = dg.modify_df2(df2, successful_tries)
        length1, width1 = df.shape
        length2, width2 = new_df2.shape

        if width1 != 0:
            size = int(width2/width1)
            # print (width1)
            # print (width2)
            # Create list for checking RAG status
            check = []

            # Run through RAG columns for measures and check status
            for i in range(width1):
                list_at_i = new_df2.iloc[:, (size-1)+i*size]
                tester = all(x == True for x in list_at_i)
                check.append(tester)

            Process_RAG = all(x == True for x in check)
        else:
            Process_RAG = False
        if Process_RAG is True:
            colour = "forestgreen"
        elif Process_RAG is False:
            colour = "tomato"
        else:
            colour = "royalblue"

        return Process_RAG, colour


def card_template(id_name, image_path):

    card = dbc.Card(
                [
                    dbc.CardImg(src=image_path, top=True),
                    dbc.CardBody(
                        [
                            html.H4(id_name, className="card-title"),
                            html.P(
                                "This page contains the CPPs for {}".format(id_name),
                                className="card-text",
                            ),
                            dbc.Button("Go to: Machine {}".format(id_name),
                                       color="Secondary",
                                       id="{}-button".format(id_name),
                                       href='/{}'.format(id_name)),
                        ]
                    )
                    
                ],
        className="w-25 mb-3",
            )

    return card

# Create cards for overview page


def card_template_overview(id_name, process_name, image_path):

    Process_RAG, colour = RAG_Indicator(process_name, id_name)

    card = dbc.Card(
        [
            dbc.CardImg(src=image_path, top=True),
            dbc.CardBody(
                [
                    html.H4(process_name, className="card-title"),
                    html.P(
                        "Click for detailed information on {}".format(process_name),
                        className="card-text",
                    ),
                    dbc.Button("Go to: {}".format(process_name),
                               color="primary",
                               id="{}-button".format(process_name),
                               href='/{}/{}/control_chart'.format(id_name, process_name)),
                    dq.Indicator(
                                color=colour,
                                value=True,
                                size=30
                            )
                ]
            )
        ],
        className="w-25 mb-3",
    )

    return card