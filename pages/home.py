import dash
from dash import html, dcc, Dash, callback
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

dash.register_page(__name__, name="Home", path='/')


#Header start
Header=html.Div([html.H3("Phone Work Management System")],style={'height':'100px','width':'1000px','background-color':'#FFE4E1','margin-left':'50px','padding-top':'20px','text-align':'center'})
#Header end

#Cards start
cards=html.Div([
                    html.Div([
                            html.Div([html.I(className="fa fa-user me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'greenyellow'}),
                            html.Div([html.H4("13"),html.P("customers")],className='card1_detail')
                    ],className='card1_div'),
                   
                   
                    html.Div([
                            html.Div([html.I(className="fa fa-list me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#FF7F50'}),
                            html.Div([html.H4("8"),html.P("categories")],className='card1_detail')
                    ],className='card1_div'),
                   
                   
                    html.Div([
                            html.Div([html.I(className="fa  fa-shopping-cart me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#00FFFF'}),
                            html.Div([html.H4("7"),html.P("Products")],className='card1_detail')
                    ],className='card1_div'),
                   
                   
                    html.Div([
                            html.Div([html.I(className="fa fa-dollar me-20",style={'font-size':'50px','color':'white','margin-left':'30px','margin-top':'40px'}),],className="card",style={'background-color':'#FDD761'}),
                            html.Div([html.H4("0"),html.P("Sales")],className='card1_detail')
                    ],className='card1_div'),                   
        ], className='card_div',)
#Cards end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Stock is running low in quantity block start
card_content1 = [
    dbc.CardHeader(" Stock is running low in quantity", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
#Stock is running low in quantity block end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Unpaid bills for purchase
card_content2 = [
    dbc.CardHeader(" Unpaid Bills For Purchase", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
#Unpaid bills for purchase end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Unpaid bills for repair
card_content3 = [
    dbc.CardHeader(" Unpaid Bills For Repair", style={'font-size':'20px','color':'#A52A2A','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
#Unpaid bills for repair end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#Highest Selling Products
card_content4 = [
    dbc.CardHeader(" Highest Selling Products", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
#Highest Selling Products end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# LATEST SALES
card_content5 = [
    dbc.CardHeader("  LATEST SALES", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
# LATEST SALES end
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# RECENTLY ADDED PRODUCTS
card_content6 = [
    dbc.CardHeader("  RECENTLY ADDED PRODUCTS", style={'font-size':'20px','color':'Black','font-weight':'bold','background-color':'#F5F5DC','text-align':'center','width':'295px'},class_name='fa fa-th'),
    dbc.CardBody(
        [
            html.P(
                "This is some card content that we'll reuse",
                className="card-text",),
        ]
    ),
]
# RECENTLY ADDED PRODUCTS end

layout =html.Div([

    
    dbc.Col([
            Header,
            cards,
            dbc.Col(dbc.Card(card_content1, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'})),   #Column for stock
            dbc.Col(dbc.Card(card_content2, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(330px,-150px)',}),   #Column for Unpaid bills for purchase
            dbc.Col(dbc.Card(card_content3, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(660px,-300px)'}),   #Column for Unpaid bills for repair
            
            dbc.Col(dbc.Card(card_content4, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(0px,-200px)',}),   #Column for HIGHEST SALEING PRODUCTS
            dbc.Col(dbc.Card(card_content5, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(330px,-350px)',}),   #Column for LATEST SALES
            dbc.Col(dbc.Card(card_content6, style={'color':"light",'display':'flex','flex-direction':'column','width':'300px'}),style={'transform':'translate(660px,-500px)'}),   #RECENTLY ADDED PRODUCTS
            
            
            
            ],style={'width':'fit-content','color':'blue'}),
      

], style={'width':'fit-content','color':'blue'})