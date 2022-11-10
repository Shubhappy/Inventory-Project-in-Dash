import dash
from dash import html, dcc, Dash, callback, dash_table
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
import pandas as pd

dash.register_page(__name__, name="Customer Role", path='/pages/customer_roles.py')

forms=dbc.Form([
    dbc.Row(html.H3("Add New User Group"),style={'text-align':'center'}),
    dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Group Name"),
                dbc.Input(
                    type="text",
                    id="name",
                    # value='',
                    placeholder="Enter here",
                    persistence=False
                ),
            ],
            width=6,
        ),
        dbc.Col(
            [
                dbc.Label("Group Level"),
                dbc.Input(
                    type="number",
                    id="level",
                    # value='',
                    placeholder="Enter here",
                    
                ),
            ],
            width=6,
        ),
    ],
    className="g-3",
),

     dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("Status"),
                dcc.Dropdown(id="dropdown",options=[{"label": "Active", "value": 'Active'},{"label": "Deactive", "value": 'Deactive'},],),
            ],
            width=6,
        ),]),



    dbc.Row(dbc.Col(dbc.Button("Add New Role", color="primary",id='adding-rows-button', n_clicks=0), width="auto",style={'margin-top':'0px','border':'2px solid red'},align='center'),style={'margin-top':'10px','border':'2px solid'},align='center',justify='center')

],
style={'title':'Add New User Group'}
)

#-------------------------------------------------------------------------------------------------------------------------------------
data_table=html.Div([
# html.Div([
#         # dcc.Input(
#         #     id='adding-columns-name',
#         #     placeholder='Enter a column name...',
#         #     value='',
#         #     style={'padding': 10}
#         # ),
#         # html.Button('Add Column', id='adding-columns-button', n_clicks=0)
#     ], style={'height': 50}),

   
    dash_table.DataTable(
        id='adding-rows-table',
      
        columns = [
    dict(id='group_name', name='Group Name',type='text'),
    dict(id='group_level', name='Group Level', type='numeric'),
    dict(id='status', name='Status')
],

        data = [
        dict(group_name="", group_level='', status='')
             
        for j in range(0)],       

        editable=True,
        export_columns='all',
        export_format='xlsx',
        export_headers='display',
        row_deletable=True,
        # fixed_rows={'header':True},
        filter_action="native",
        filter_options={"case": "insensitive"},
    ),

    # html.Div([html.Button('Add Row for data entry', id='adding-rows-button', n_clicks=0),],style={'height': 50}),
    
    dcc.Store(id='click-memory',data=[],storage_type='memory'),
])


###################################################
# App layout
layout=dbc.Container([                                                                 #Put layout when added to the app pages
dbc.Row(forms),
html.Hr(),
dbc.Row(data_table)

],style={'width':'82%'})
###################################################

# -------------------------------------------------------------------------------------
# Storing row data
@callback(Output('click-memory', 'data'),
             Input('adding-rows-table', 'data'),
            #  prevent_initial_call=True
            #  Input('bar-container', component_property='children')]
            )
def store_data(data):
    
    return data

# -------------------------------------------------------------------------------------
#Adding row
@callback(
            Output('adding-rows-table', 'data'),
           
            Input('adding-rows-button', 'n_clicks'), 
            # Input('name','value'),
            # Input('level','value'),
            # Input('dropdown','value'),
           [State('adding-rows-table', 'data'),
            State('adding-rows-table', 'columns'),
            State('adding-rows-table', 'derived_virtual_data'),
            State('name','value'),
            State('level','value'),
            State('dropdown','value')
            ],
           prevent_initial_call=True
           
)
def update_row(n_clicks,rows, columns,virtual_data,val4,val5,val6):     #val1,val2,val3,
    
    if n_clicks > 0:        
        rows.append({c['id']: '' for c in columns})

    df = pd.DataFrame(virtual_data,columns=['group_name','group_level','status'],)
    df2={'group_name':val4,'group_level':val5,'status':val6}
    df=df.append(df2, ignore_index = True)
    data=df.to_dict('records')


    print(data)


        
    return data

# -------------------------------------------------------------------------------------
# Clear the input values
@callback(
    [Output('name','value'),
    Output('level','value'),
    Output('dropdown','value'),],
    Input('adding-rows-button', 'n_clicks'),
    State('name','value'),
    State('level','value'),
    State('dropdown','value'),
  
     prevent_initial_call=True
)

def table(n_clicks,val7,val8,val9):
    if n_clicks > 0:
        val7=""
        val8=""
        val9=""
        
#         # x=len(rows)
#         # y=x+1
        
#         # data=[
#         #     {'column-{}'.format(i): (j + (i-1)*5) for i in range(1, 5)}
#         #     for j in range(x,y)
#         # ],

#         df = pd.DataFrame(all_rows_data,columns=['group_name','group_level','status'])
#         print(df)
        return val7,val8,val9



















# #Header start
# Header=html.Div([html.H3("Customer Roles will display here")],style={'height':'100px','width':'1000px','background-color':'#FFE4E1','margin-left':'50px','padding-top':'20px','text-align':'center'})
# #Header end

# layout =html.Div([

    
#     dbc.Col([
#             Header,           
            
#             ],style={'width':'fit-content','color':'blue'}),
      

# ], style={'width':'fit-content','color':'blue'})

# data1 = pd.DataFrame({'x1':range(50, 56),           # Create pandas DataFrame
#                       'x2':range(10, 16),
#                       'x3':range(36, 30, - 1)})
# # print(data1)         

# for i in range(1,2):                               # Append rows within for loop
#     data1.loc[len(data1)] = i * 5
# print(data1)