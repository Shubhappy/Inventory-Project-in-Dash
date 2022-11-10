import dash
from dash import html, dcc, Dash
from dash import dash_table as dt
from dash.dependencies import Input, Output, State
from pandas import *
# import plotly.graph_objs as go
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import datetime
from time import strftime,localtime
import dash_auth
# from pages import Home


# Keep this out of source code repository - save in a file or a database
# VALID_USERNAME_PASSWORD_PAIRS = {
#     'admin': 'admin@123'
# }


external_stylesheets = [dbc.themes.BOOTSTRAP,
'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css','https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',"https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js","https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"]

app = dash.Dash(__name__,title='Mxpertz', use_pages=True, external_stylesheets=external_stylesheets, suppress_callback_exceptions=True,
                        meta_tags=[{'name': 'viewport',
                                    'content': 'width=device-width, initial-scale=1.0'}]
                            ) 


# auth = dash_auth.BasicAuth(
#     app,
#     VALID_USERNAME_PASSWORD_PAIRS)

#------------------------------------------------------------------------
# #Header start
# Header=html.Div([html.H3("Phone Work Management System")],style={'height':'100px','width':'1000px','background-color':'#FFE4E1','margin-left':'50px','padding-top':'20px','text-align':'center'})
# #Header end

# Dropdown styling start here
dropdown = dbc.DropdownMenu(
    label="Admin",
    children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-user"), " Profile"]),
        dbc.DropdownMenuItem([html.I(className="fa fa-cog ")," Setting"]),
        dbc.DropdownMenuItem([html.I(className="fa fa-power-off"),"  Logout"])
        ],
    className='logo_dropdown')
# Dropdown styling ends here
#-------------------------------------------------------------------------

# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# Side Navigation bar styling starts here
nav = [dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-home me-2"),"Dashboard"]),style={'color':'#C0C0C0'},href=('http://127.0.0.1:8050/')))]),
    
       dbc.Nav([    
                    dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-user me-2"),"Customer Management"]),style={'color':'#C0C0C0'},id='collapse-button2'),),
                    dbc.Collapse(dbc.ButtonGroup([dbc.Button("Customer Roles",href=('http://127.0.0.1:8050/pages/customer_roles.py')),dbc.Button("Manage Customers",href=('http://127.0.0.1:8050/pages/manage_customers.py'))],vertical=True),id="customer_collapse",is_open=False,),       
                    ],vertical=True),

       dbc.Nav([    
                    dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Products"]),style={'color':'#C0C0C0'},id='collapse-button1'),),
                    dbc.Collapse(dbc.ButtonGroup([dbc.Button("Manage Products",href=('https://google.com')),dbc.Button("Add Products",href=('https://gmail.com')),dbc.Button("Categories",href=('https://gmail.com')),dbc.Button("Subcategories",href=('https://gmail.com'))],vertical=True),id="product_collapse",is_open=False,),       
                    ],vertical=True),

        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-picture-o me-2"),"Images"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-file-text-o me-2"),"Invoice"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        
        
        
        
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-envelope-o me-2"),"Email"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Offer"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Company-Overview"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Office Expenses"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Purchase-Overview"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Repair-Overview"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Cash-Sale"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Sales"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),
        dbc.Nav([dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Sales Report"]),style={'color':'#C0C0C0'},href=('https://gmail.com')))]),

]    
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-user me-2"),"Customer Management"]),style={'color':'#C0C0C0'})),        
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Products"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-picture-o me-2"),"Images"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-file-text-o me-2"),"Invoice"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-envelope-o me-2"),"Email"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Offer"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Company-Overview"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Office Expenses"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Purchase-Overview"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Repair-Overview"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Cash-Sale"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Sales"]),style={'color':'#C0C0C0'})),
    #     dbc.NavItem(dbc.NavLink(html.Span([html.I(className="fa fa-th-large me-2"),"Sales Report"]),style={'color':'#C0C0C0'})),   
    # ],
    # vertical="md",)
# Side Navigation bar styling ends here
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#Cards start
# cards=html.Div([
#                     html.Div([
#                             html.Div([html.I(className="fa fa-user me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'greenyellow'}),
#                             html.Div([html.H4("13"),html.P("customers")],className='card1_detail')
#                     ],className='card1_div'),
                   
                   
#                     html.Div([
#                             html.Div([html.I(className="fa fa-list me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#FF7F50'}),
#                             html.Div([html.H4("8"),html.P("categories")],className='card1_detail')
#                     ],className='card1_div'),
                   
                   
#                     html.Div([
#                             html.Div([html.I(className="fa  fa-shopping-cart me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#00FFFF'}),
#                             html.Div([html.H4("7"),html.P("Products")],className='card1_detail')
#                     ],className='card1_div'),
                   
                   
#                     html.Div([
#                             html.Div([html.I(className="fa fa-dollar me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#FDD761'}),
#                             html.Div([html.H4("0"),html.P("Sales")],className='card1_detail')
#                     ],className='card1_div'),                   
#         ], className='card_div')
# #Cards end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #Stock is running low in quantity block start
# card_content1 = [
#     dbc.CardHeader(" Stock is running low in quantity", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# #Stock is running low in quantity block end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #Unpaid bills for purchase
# card_content2 = [
#     dbc.CardHeader(" Unpaid Bills For Purchase", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# #Unpaid bills for purchase end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #Unpaid bills for repair
# card_content3 = [
#     dbc.CardHeader(" Unpaid Bills For Repair", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# #Unpaid bills for repair end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# #Highest Selling Products
# card_content4 = [
#     dbc.CardHeader(" Highest Selling Products", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# #Highest Selling Products end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # LATEST SALES
# card_content5 = [
#     dbc.CardHeader("  LATEST SALES", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# # LATEST SALES end
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# # RECENTLY ADDED PRODUCTS
# card_content6 = [
#     dbc.CardHeader("  RECENTLY ADDED PRODUCTS", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
#     dbc.CardBody(
#         [
#             html.P(
#                 "This is some card content that we'll reuse",
#                 className="card-text",),
#         ]
#     ),
# ]
# # RECENTLY ADDED PRODUCTS end




# Layout section start her
# ************************************************************************
# ************************************************************************
# ************************************************************************

app.layout=dbc.Container([

#-------------------------------------------------------------------------------------------------------
# Header row start here  
    dbc.Row([
                #Logo image start here
                dbc.Col(html.Img(src='/assets/phonewerk.png',className='logo_image',height='50px',width='180px'),
                        width=2,
                        className="bg-primary text-white",style={'height':'65px','width':'245px'}),
                #Logo image ends here
                
                #Timer and login dropdown start here
                dbc.Col([            
                            html.Div(id='live-date-clock', className='clock'),
                                dcc.Interval(     
                                    id='interval-component',
                                    interval=1*1000, # 1 sec=1*1000 millisecond
                                    n_intervals=0
                                ),

                            html.Img(src='/assets/profile.png',className='profile_logo',height='30px',width='30px'), #Login image

                            dropdown, #dropdown mentioned globally
                        ],width=9),
                #Timer and login dropdown ends here    
                
            ], className="border border-danger",style={'height':'65px'}
           ),
# Header row ends here  
#-------------------------------------------------------------------------------------------------------

# Body row starts here 
    dbc.Row([
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++    
    dbc.Col(nav,width=2,className="side_nav"),  # Sidebar Navigation column
   
#Dashboard columns
    # First column for header and cards starts here
    # dbc.Col([
    #         Header,
    #         cards,
    #         dbc.Col(dbc.Card(card_content1, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'})),   #Column for stock
    #         dbc.Col(dbc.Card(card_content2, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(330px,-150px)',}),   #Column for Unpaid bills for purchase
    #         dbc.Col(dbc.Card(card_content3, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(660px,-300px)'}),   #Column for Unpaid bills for repair
            
    #         dbc.Col(dbc.Card(card_content4, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(0px,-200px)',}),   #Column for HIGHEST SALEING PRODUCTS
    #         dbc.Col(dbc.Card(card_content5, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(330px,-350px)',}),   #Column for LATEST SALES
    #         dbc.Col(dbc.Card(card_content6, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(660px,-500px)'}),   #RECENTLY ADDED PRODUCTS
            
            
            
    #         ],width=10,className="dashboard_page"),
          
    
    # dash.page_container
    dbc.Col([dash.page_container],width=9,className="dashboard_page")
    ])
# Body row ends here 



# Layout section end here
# ************************************************************************
], class_name="border border-info",fluid=True)

# ************************************************************************
#call back function for Date and clock according to localtime
@app.callback(Output('live-date-clock', 'children'),
              Input('interval-component', 'n_intervals'))
def date_clock(n):
        # time= strftime("%A, %d-%B-%Y, %H:%M:%S", localtime()
        time= strftime("%A, %B %d, %Y, %I:%M:%S %p", localtime()
        )
        return time


@app.callback(
    Output("product_collapse", "is_open"),
    [Input("collapse-button1", "n_clicks")],
    [State("product_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("customer_collapse", "is_open"),
    [Input("collapse-button2", "n_clicks")],
    [State("customer_collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



# ************************************************************************
if __name__=='__main__':
    app.run_server(debug=True)
