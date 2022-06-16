import numpy as np
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Boxplot', external_stylesheets=external_stylesheets)
df = pd.read_excel('Gyalpozhing_household_power_consumption.XLSX')
# print(df.head())
# print('hello')
df = pd.DataFrame(df,columns=['Category','portion','posting_Date','current','voltage','consumption','energy_Charges'])
df = df.loc[(df['posting_Date'] >= '01-01-2019') & (df['posting_Date'] < '01-01-2022')]

df['Year'] = pd.to_datetime(df['posting_Date']).dt.year
df['Month'] = pd.to_datetime(df['posting_Date']).dt.month
df = df.drop(['posting_Date'], axis = 1)

df = df.drop_duplicates(keep='first')


from sklearn.impute import SimpleImputer

imp = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
imp = imp.fit_transform(df)

df = pd.DataFrame(imp, columns=df.columns)

X = df.Month
Y = df.consumption


app.layout = html.Div([
    # html.H4('Energy Consumption for past two years'),
    dcc.Graph(id='bar-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff', 'margin-bottom':'8px'}),
    html.Div(
        id='bar-updatemode',
        
    ),
    html.Br(),
    
])


@app.callback(
               Output('bar-graph', 'figure'),
              [Input('bar-updatemode', 'value')])
def display_value(value):
    
    graph = go.Bar(x=X, y=Y)


    layout = go.Layout( 
        title= 'Monhthly Change in Energy Consumption for Past Three Years',
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white'),
        margin=dict(t=50, b=225), # Where l r t b correspond to left, right, top, bottom

    )
    
     
    return {'data': [graph], 'layout': layout}