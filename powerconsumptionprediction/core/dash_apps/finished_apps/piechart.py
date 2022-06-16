
import numpy as np
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

from plotly.subplots import make_subplots

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Piechart', external_stylesheets=external_stylesheets)
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

df = df[df['consumption'] > 1.0]


companies = df['Year'].value_counts()
labels = companies.keys()


app.layout = html.Div([
    html.H4('Consumption over Past Three Years'),
    dcc.Graph(id='line-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    html.Div(
        id='line-updatemode',
        
    ),
])


@app.callback(
               Output('line-graph', 'figure'),
              [Input('line-updatemode', 'value')])
def display_value(value):
         
    
    
    graph = go.Pie(labels=labels, values=companies, scalegroup='one',
                        name="consumption")    
    
    layout = go.Layout(
        title='Showing the Regions',
        paper_bgcolor='#27293d',
        font=dict(color='white'),
        showlegend=True

    )
    
    

    return {'data': [graph], 'layout': [layout]}



