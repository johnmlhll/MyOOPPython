#Sample (10k records) of a large dataset and visualise a Dataiku dataset through Apache Spark.
#Then run the visualisation through toPandas() and chart the results
#(internet search V actual sales) on a line graph by month overlaid by scatter points

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
intCS_ds = dataiku.Dataset("MyInternetClickStreamDataSet")

# And read it as a Spark dataframe
intCS_df = dkuspark.get_dataframe(sqlContext, intCS_ds)

# Discern a sample dataset from the source Spark dataset intCS_df
intCS_sdf = intCS_df.sample(False, 0.5, 10000)

# Initiate offline notebook mode
py.init_notebook_mode()

# Insantiate toPandas() and assign sampled Spark df to it
intCS_sdf_pandas = intCS_sdf.toPandas()

# Plot the Linechart
x = intCS_sdf_pandas['parsed_date_month'] #X axis dataset attribute
y0 = intCS_sdf_pandas['search_qty_sum'] #Y axis dataset attribute
y1 = intCS_sdf_pandas['sales_qty_sum'] # Y axis dataset attribute

Search_Quantity = go.Scatter(
x=x,
y=y0,
mode='line'
)
Sales_Quantity = go.Scatter(
x=x,
y=y1,
mode='markers'
)

data = [Search_Quantity,Sales_Quantity]

# Execute the plot via plotly
py.iplot(data)
