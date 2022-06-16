from django.shortcuts import render
import plotly.graph_objects as go
# Create your views here.
from plotly.offline import plot


def dashboard(request):
    def scatter():
        x1 = [1,2,3,4]
        y1 = [30, 35, 25, 45]

        trace = go.Scatter(
            x = x1,
            y = y1
        )
        layout = dict(
            title='Simple Graph',
            xaxis=dict(range=[min(x1), max(x1)]),
            yaxis = dict(range=[min(y1), max(y1)])
        )

        fig = go.Figure(data=[trace], layout=layout)
        plot_div = plot(fig, output_type='div', include_plotlyjs=False)
        return plot_div

    context ={
        'plot1': scatter()
    }

    return render(request, 'home/welcome.html', context)


def bar(request):
    

    return render(request, 'home/barchart.html')

def pie(request):
    

    return render(request, 'home/piechart.html')


def line(request):    

    return render(request, 'home/linechart.html')


def box(request):    

    return render(request, 'home/boxplot.html')


