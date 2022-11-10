import dash
from dash import html, dcc, Dash, callback, dash_table
from dash.dependencies import Input, Output, State
from pandas import *
import pandas as pd
import dash_bootstrap_components as dbc
from PIL import Image
import io
import base64


# dash.register_page(__name__, name="Mangage Customers", path='/pages/manage_customers.py')

app = dash.Dash(__name__,title='Mxpertz', use_pages=False,
                        meta_tags=[{'name': 'viewport',
                                    'content': 'width=device-width, initial-scale=1.0'}]
                            ) 

forms=dbc.Form([
    dbc.Row(html.H3("Add New Customer"),style={'text-align':'center'}),
    dbc.Row(
    [
       dbc.Col([
         dbc.Label("Title"),
                dcc.Dropdown(id="title_dropdown",options=[{"label": "Mr.", "value": 'Mr.'},{"label": "Mrs.", "value": 'Mrs.'},{"label": "Ms.", "value": 'Ms.'}],)
                
                ],width=1),
        dbc.Col(
            [
                dbc.Label("First Name"),
                dbc.Input(
                    type="text",
                    id="first name",
                    # value='',
                    placeholder="Enter here",
                    persistence=False
                ),
            ],
            width=4,
        ),
        dbc.Col(
            [
                dbc.Label("Last Name"),
                dbc.Input(
                    type="text",
                    id="last name",
                    # value='',
                    placeholder="Enter here",
                    
                ),
            ],
            width=4,
        ),
    ],
    className="g-3",
),
html.Br(),
dbc.Row(
    [
       dbc.Col([
         dbc.Label("Address"),
               dbc.Input(
                    type="text",
                    id="address",
                    # value='',
                    placeholder="Enter here",
                    persistence=False)
                ],width=4),
        dbc.Col(
            [
                dbc.Label("Contact No."),
                dbc.Input(
                    type="tel",
                    id="contact",
                    # value='',
                    placeholder="Enter no. here",
                    persistence=False
                ),
            ],
            width=2,
        ),
        dbc.Col(
            [
                dbc.Label("Email"),
                dbc.Input(
                    type="email",
                    id="mail",
                    # value='',
                    placeholder="Enter Email here",
                    
                ),
            ],
            width=5,
        ),
    ],
    className="g-3",
),



     dbc.Row(
    [
        dbc.Col(
            [
                dbc.Label("User Role"),
                dcc.Dropdown(id="user_role",options=[{"label": "Retailer", "value": 'Retailer'},{"label": "Dealer", "value": 'Dealer'},],),
            ],
            width=2,
        ),
        
        dbc.Col(
            [
                dbc.Label("Status"),
                dcc.Dropdown(id="status",options=[{"label": "Active", "value": 'Active'},{"label": "Deactive", "value": 'Deactive'},],),
            ],
            width=2,
        ),

        dbc.Col([html.A(dcc.Upload('Upload Image',id='upload'))], width=2), 

        # dbc.Col([
        #     dbc.Label("Mode of Sale"),
        #     dcc.RadioItems(options=['Online', 'Offline', 'Cash Sale'],inputStyle={'margin-left':'15px'},style={'margin-top':'0px','border':'2px solid black','justify-content':'center'})
        # ], style={'margin-left':'500px','padding-top':'10px','align-items':'center','justify-content':'center'},width=4),

    dbc.Row(dbc.Col(dbc.Button("Add User", color="primary",id='adding-rows-button', n_clicks=0), width="auto",style={'margin-top':'0px','border':'2px solid red'},align='center'),style={'margin-top':'10px','border':'2px solid'},align='center',justify='center')

],
style={'title':'Add New User Group'}
)
])

#-------------------------------------------------------------------------------------------------------------------------------------
data_table=html.Div([
 
    dash_table.DataTable(
        id='adding-rows-table2',
      
        columns = ([
                    dict(id='title', name='Title',type='text'),
                    dict(id='firstname', name='First Name', type='text'),
                    dict(id='lastname', name='Last Name', type='text'),
                    dict(id='addr', name='Address', type='text'),
                    dict(id='phone', name='Contact', type='numeric'),
                    dict(id='mailid', name='Email', type='any'),
                    dict(id='userrole', name='User Role', type='text'),
                    dict(id='customer_status', name='Status', type='text'), 
                    dict(id='image', name='Image', type='any',presentation='markdown'),                       
                 ]),

        data = [dict(group_name="", group_level='', status='')             
                for j in range(0)],       
        
        markdown_options={"html": True},
        editable=True,
        export_columns='all',
        export_format='xlsx',
        export_headers='display',
        row_deletable=True,
        filter_action="native",
        filter_options={"case": "insensitive"},
    ),    
    
    dcc.Store(id='click-memory1',data=[],storage_type='memory'),
])

###################################################
# App layout
app.layout=dbc.Container([                                                                 #Put layout when added to the app pages
dbc.Row(forms),
html.Hr(),
dbc.Row(data_table)

],style={'width':'82%'})
###################################################

# -------------------------------------------------------------------------------------
# Storing data of row
@app.callback(Output('click-memory1', 'data'),
             Input('adding-rows-table2', 'data'),
            #  prevent_initial_call=True
            #  Input('bar-container', component_property='children')]
            )
def store_data(data):    
    return data
# -------------------------------------------------------------------------------------
#Adding row
@app.callback(
                Output('adding-rows-table2', 'data'),           
                Input('adding-rows-button', 'n_clicks'),
                [State('adding-rows-table2', 'data'),
                State('adding-rows-table2', 'columns'),
                State('adding-rows-table2', 'derived_virtual_data'),
                State('title_dropdown','value'),
                State('first name','value'),
                State('last name','value'),
                State('address','value'),
                State('contact','value'),
                State('mail','value'),
                State('user_role','value'),
                State('status','value'),           
                State('upload','contents') 
                ],
                prevent_initial_call=True           
            )
def update_row(n_clicks,rows, columns,visible_data,val1,val2,val3,val4,val5,val6,val7,val8,val9):     
    img=val9    
    print(img)
    img = f"<img src={img}>"        #Use it to convert base64 image in html image string, when data from dcc.upload option as "content" in callback
   
    if n_clicks > 0:        
        rows.append({c['id']: '' for c in columns})

    df = pd.DataFrame(visible_data,columns=['title','firstname','lastname','addr','phone','mailid','userrole','customer_status','image'],)
    df2={'title':val1,'firstname':val2,'lastname':val3,'addr':val4,'phone':val5,'mailid':val6,'userrole':val7,'customer_status':val8,'image':img}
    df=df.append(df2, ignore_index = True)
    data=df.to_dict('records')
        # print(data)        
    print(val9)
    return data
  
# -------------------------------------------------------------------------------------
# Clear the input values from form
@app.callback(
    [Output('title_dropdown','value'),
    Output('first name','value'),
    Output('last name','value'),
    Output('address','value'),
    Output('contact','value'),
    Output('mail','value'),
    Output('user_role','value'),
    Output('status','value'),
    Output('upload','contents')    
    ],
    Input('adding-rows-button', 'n_clicks'),
    [State('title_dropdown','value'),
    State('first name','value'),
    State('last name','value'),
    State('address','value'),
    State('contact','value'),
    State('mail','value'),
    State('user_role','value'),
    State('status','value'),
    State('upload','contents')    
    ],
     prevent_initial_call=True
)

def table(n_clicks,val9,val10,val11,val12,val13,val14,val15,val16,val17):
    if n_clicks > 0:
        val9=""
        val10=""
        val11=""
        val12=""
        val13=""
        val14=""
        val15=""
        val16=""
        val17=""
        return val9,val10,val11,val12,val13,val14,val15,val16,val17

# ************************************************************************
if __name__=='__main__':
    app.run_server(debug=True)




