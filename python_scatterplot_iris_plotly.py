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
iris_ds = dataiku.Dataset("iris_final")
# And read it as a Spark dataframe
iris_df = dkuspark.get_dataframe(sqlContext, iris_ds)

#Initialise plotly offline mode
py.init_notebook_mode()

#Declare iris_df as a pandas Series
iris_df_pandas = iris_df.toPandas()

#Declare Variables
x_SepalL = iris_df_pandas['SepalLength']
y_SepalW = iris_df_pandas['SepalWidth']
x_PetalL = iris_df_pandas['PetalLength']
y_PetalW = iris_df_pandas['PetalWidth']

# A standard plotly scatter graph showing the correlation betwen sepal
# and petal length and width
trace = go.Scatter(
    x = x_SepalL,
    y = y_SepalW,
    mode = 'markers',
    marker=dict(size=12, line=dict(width=1)
    ),
name = 'Iris Sepal',
text = ["iris_df_pandas['Name']"]
)

trace1 = go.Scatter(
    x = x_PetalL,
    y = y_PetalW,
    mode = 'markers',
    marker=dict(size=12, line=dict(width=1)
    ),
name = 'Iris Petal',
text = ["iris_df_pandas['Name']"]
)

data = [trace, trace1]

layout = go.Layout(
    title = 'Iris - Petal2Sepal Study',
    hovermode = 'closest',
    xaxis=dict(
        title='Length Iris Attributes (mm)',
        ticklen = 5,
        zeroline=False,
        gridwidth=2,
    ),
    yaxis=dict(
        title = 'Width Iris Attributes (mm)',
        ticklen = 5,
        gridwidth = 2,
    )
)
fig = go.Figure(data=data, layout=layout)
py.iplot(data)
