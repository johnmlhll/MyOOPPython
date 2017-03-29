# Find % conversation rate of web searches2sales by counts totals
# Dataset distributed on Dataiku and Spark used as a dataframework
%pylab inline

# Import Libraries
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
ins_dataset_ds = dataiku.Dataset("insert_dataset")
# And read it as a Spark dataframe
ins_dataset_df = dkuspark.get_dataframe(sqlContext, ins_dataset_ds)

# Init notebook mode for offline activity
py.init_notebook_mode()

# Read Spark df into a Pandas df
ins_dataset_df_pandas = ins_dataset_df.toPandas()

# Plot Data
trace1=go.Scatter(
    x = ['Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec'],
    y = ins_dataset_df_pandas['conv_rate']*100,

    mode='lines+markers',
    name='Conversion % Searches to Sales',
    line=dict(
        color='rgb(46,139,87)',
        width=5
    )
)
data=[trace1]

# Plot Layout
layout=go.Layout(
    title="Years Conversion Rate - Searches 2 Sales by Month",
    xaxis=dict(
    title='Month',
    linewidth='4',
    ),
    yaxis=dict(
    title='Conversion % Searches to Sales',
    linewidth='4',
    ticksuffix = '%',
    ),
)

# Plot Figure and Chart
fig = go.Figure(data=data, layout=layout)
py.iplot(fig)
