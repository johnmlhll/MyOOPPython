%pylab inline

#import libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
from plotly.graph_objs import *
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

# Load PySpark
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

#import api creditentals for the author: John Mulhall @johnmlhll
py.sign_in('johnmlhll','*api_key*')

# creating a sample 3 dimensional density flow chart with periphal datacharts
#setting variables using np.random
t = np.linspace(-1,1.2,2000)
x = (t**3)+(0.3*np.random.randn(2000))
y = (t**6)+(0.3*np.random.randn(2000))

#first plot for tracing scatterplot using plotly.graph_objs
trace1 = go.Scatter(
x=x, y=y, mode='markers', name='points',
marker=dict(color='rgb(102,0,0)', size=2, opacity=0.4)
)
#2nd trace (density chart) plotting aspects of the visualisation down the line to the last trace
trace2 = go.Histogram2dcontour(
x=x, y=y,name='density', ncontours=20,
colorscale='Hot', reversescale=True, showscale=False
)
trace3 = go.Histogram(
x=x, y=y, name='x density',
marker=dict(color='rgb(102,0,0)'),
yaxis = 'y2'
)
trace4 = go.Histogram(
x=x, y=y, name='y density', marker=dict(color='rgb(102,0,0)'),
xaxis = 'x2'
)
data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
showlegend = False,
autosize = False,
width = 600,
height = 550,
xaxis=dict(
    domain=[0,0.85],
    showgrid=False,
    zeroline=False,
),
yaxis=dict(
    domain=[0,0.85],
    showgrid=False,
    zeroline=False,
),
margin=dict(
    t=50
),
hovermode='closet',
bargap=0,
xaxis2=dict(
    domain=[0.85,1],
    showgrid=False,
    zeroline=False,
),
yaxis2=dict(
    domain=[0.85,1],
    showgrid=False,
    zeroline=False,
))

#plot graph figure and output
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='2D Density Plot/Histogram (Sample)')
