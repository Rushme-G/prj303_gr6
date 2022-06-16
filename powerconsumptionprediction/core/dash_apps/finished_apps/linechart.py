import numpy as np
from dash import dcc
from dash import html
import pandas as pd
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('Linechart', external_stylesheets=external_stylesheets)
df = pd.read_csv('totalconsumption.csv')
# print(df.isnull().sum())
ndf = pd.read_csv('totalconsumption1.csv')

ydf = pd.read_csv('totalconsumption2.csv')

app.layout = html.Div([
    # html.H5('Yearly Change in Energy Consumption for the Past Three Years'),
    dcc.Graph(id='line-graph', animate=True, style={"backgroundColor": "#1a2d46", 'color': '#ffffff'}),
    html.Div(
        id='line-updatemode',
        
    ),
])


@app.callback(
               Output('line-graph', 'figure'),
              [Input('line-updatemode', 'value')])
def display_value(value):
    
    graph = go.Scatter(x=df['Month'],y=df['totalconsumption'],
                  name='consumption in 2021')


    graph1 = go.Scatter(x=ndf['Month'],y=ndf['totalconsumption'],
                  name='consumption in 2019')

    graph2 = go.Scatter(x=ydf['Month'],y=ydf['totalconsumption'],
                  name='consumption in 2020')
    layout = go.Layout(
        title='Yearly Change in Energy Consumption for the Past Three Years(2019 and 2021)',
        paper_bgcolor='#27293d',
        font=dict(color='white'),
        showlegend=True

    )

    return {'data': [graph,graph1,graph2], 'layout': layout}

