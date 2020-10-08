import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


def Navbar():
    
    layout = dbc.NavbarSimple(
        children=[
            dbc.NavItem(dbc.NavLink("Control Chart", href = '/control_chart')),
            dbc.NavItem(dbc.NavLink("Information", href = '/info')),
            dbc.DropdownMenu(
                children=[
                    dbc.DropdownMenuItem("More Pages",header=True),
                    dbc.DropdownMenuItem("New Page", href = '/info')
                ],
                nav=True,
                in_navbar=True,
                label = "More"
            )
        ],
        brand = "Homepage",
        brand_href = '/homepage',
        color = "primary",
        dark=True
    )
    
    return layout



# def Navbar():
    
#     layout = html.Div(children=[
#         html.Nav(className = "nav nav-pills", children=[
#         html.A('Homepage', className="nav-item nav-link  btn" , href='/Homepage'),
#         html.A('Control-Chart', className="nav-item nav-link active btn" , href='/Control-Chart'),
#         html.A('Information', className="nav-item nav-link active btn" , href='/Information')
        
#         ])
#     ])
#     return layout