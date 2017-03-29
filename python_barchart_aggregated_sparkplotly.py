#Produce a Bar Chart comparing by month internet site searches and actual sales
#from an aggregrated click stream dataset.
#Each space denotes a different cell in Jupyter Notebooks.

#figure style
%pylab inline

#import libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

#initalise plotly offline notebook
py.init_notebook_mode()

#initalise Pyspark and assign a single SQL Context(sc)
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

#read in dataset from Dataiku
intCS_ds = dataiku.Dataset("MyInternetClickStreamDataSet")

#assign to pyspark df
intCS_df = dkuspark.get_dataframe(sqlContext, intCS_ds)

#instantiate toPandas as a single call df
intCS_df_pandas = intCS_df.toPandas()

#declare coordinates and map the plot
trace1 = go.Bar(
    x = intCS_df_pandas['search__month'],
    y = intCS_df_pandas['search_count'],
    name = 'Search Totals',
    marker=dict(
        color='rgb(26,118,255)'
    )
),
trace2 = go.Bar(
    x = intCS_df_pandas['search_month'],
    y = intCS_df_pandas['booking_count'],
    name = 'Booking Totals',
    marker=dict(
        color='rgb(55,83,109)'
    )
)
data=[trace1, trace2]

#map the layout and styling features (if using Jupyter notebooks, code this in a new cell!)
layout=go.Layout(
title = 'WebSite Search to Sales - 2015',
    xaxis=dict(
    tickfont=dict(
        title = 'Month',
        size = 14,
        color = 'rgb(107,107,107)'
        )
    ),
    yaxis=dict(
        title = 'Count Sales Transactions',
        titlefont=dict(
            size = 16,
            color = 'rgb(107,107,107)'
    ),
    tickfont=dict(
        size=14,
        color = 'rgb(107,107,107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgb(255,255,255,0)'
    ),
    barmode = 'group',
    bargap = 0.15,
    bargroupgap=0.1
)
fig = go.Figure(data=data,layout=layout)

#execute the plot of the graph
plot_url = py.iplot(fig)
