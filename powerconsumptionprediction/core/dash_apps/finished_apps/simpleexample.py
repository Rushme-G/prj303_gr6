from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from django_plotly_dash import DjangoDash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = DjangoDash('SimpleExample', external_stylesheets=external_stylesheets)


app.layout = html.Div([
    html.H4('Welcome '),
    html.Div([
        
        html.Div([
            html.P("This dashboard displays trends and patterns of Gyalpozhing's energy consumption through visualization. "),
            dcc.Markdown('''
##### Guidelines: 
1. Use the **side navigation bar** to view different graphs.
2. Use the **Home** button on the top right corner to navigate back to home page.
Markdown is a simple way to write and format text.

''')
        ])
    ])
    
    


    
])


@app.callback(
               Output('slider-graph', 'figure'),
              [Input('slider-updatemode', 'value')])
def display_value(value):


    layout = go.Layout(
        paper_bgcolor='#27293d',
        plot_bgcolor='rgba(0,0,0,0)',
        # xaxis=dict(range=[min(x), max(x)]),
        # yaxis=dict(range=[min(y), max(y)]),
        font=dict(color='white'),

    )
    
    # return {'layout': layout}