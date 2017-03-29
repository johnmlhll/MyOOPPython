#Using pandas.tools.plotting to get the charted curves of 4 streams of data from one 'Name' tag.

#figure/charting style
%pylab inline

#Import Libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
import pandas as pd
from pandas.tools.plotting import andrews_curves
from pandas.tools.plotting import parallel_coordinates

# Load PySpark
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

# Read the descriptor of a Dataiku dataset
iris_ds = dataiku.Dataset("iris_final")
# And read it as a Spark dataframe
iris_df = dkuspark.get_dataframe(sqlContext, iris_ds)

# Declare toPandas() dataframe from spark df
iris_df_pandas = iris_df.toPandas()

#Plot andrews curves with parallel coordinate tags
parallel_coordinates(iris_df_pandas, 'Name')
