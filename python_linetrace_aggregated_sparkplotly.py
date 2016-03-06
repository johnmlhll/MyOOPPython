#Python script using plotly to plot the web searches to sales 
#Figure style for aggregrated dataset visualisation
%pylab inline

#Import libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

# Load PySpark
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

# Read the descriptor of a Dataiku dataset
intCS_ds = dataiku.Dataset("MyInternetClickStreamDataSet")
# And read it as a Spark dataframe
intCS_df = dkuspark.get_dataframe(sqlContext, intCS_ds)

# Initiate offline Notebook mode
py.init_notebook_mode()

# Instantiate toPandas and assign the Spark dataframe
intCS_df_pandas = intCS_df.toPandas()

#Plot coordinate variables
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
         'August', 'September', 'October', 'November', 'December']
avg_search = intCS_df_pandas['avg_search_count']
avg_sale = intCS_df_pandas['avg_sale_count']

# Plot the linetracker chart data and stylings using plotly library
trace4 = go.Scatter(
    x = month,
    y = avg_search,
    name = 'WebSite Searches - Average Count',
    line = dict(
    color= 'rgb(205,12,24)',
    width=4)
)
trace5 = go.Scatter(
    x = month,
    y = avg_sale,
    name = 'Website Sales - Average Count',
    line = dict(
    color='rgb(46,139,87)',
    width=4,
    dash='dot') #options are 'dot', 'dash' and 'dashdot'
)
data=[trace4, trace5]

# Plot the layout of the chart and label it
layout = dict(title = 'Search V Sales - 2015 Count Averages',
             xaxis=dict(title='Month'),
             yaxis=dict(title='Count Value'),
             )

# Plot & Chart the graph using plotly in notebooks
fig = dict(data=data, layout=layout)
py.iplot(fig)
