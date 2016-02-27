#Based on the public dataset movieLens, see ratings by occupation over the 1 - 5 scale
#Note this is an offline plot using plotly.offline and NOT plotly.plotly for an online plot.ly result
#This script was intitially written as a training exercise on Jupyter Notebooks (Svr Edition).


#Bring the result inline with the notebook (viewable at end of notebook)
%pylab inline

#import libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
from plotly.offline import plot
from plotly.graph_objs import Scatter
import plotly.offline as py
import plotly.graph_objs as go
import pandas as pd

#initalise plotly offline notebook
init_notebook_mode()

#initalise pyspark
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

#Point to movie lens datasets python_users, python_ratings and python_movie_lens
users_ds = dataiku.Dataset("python_users")
movies_ds = dataiku.Dataset("python_movie_data_4cols")
ratings_ds = dataiku.Dataset("python_ratings")

#Read datasets into DataFrames (PySpark)
py_users = dkuspark.get_dataframe(sqlContext, users_ds)
py_movies = dkuspark.get_dataframe(sqlContext, movies_ds)
py_ratings = dkuspark.get_dataframe(sqlContext, ratings_ds)

#Analysis Piece #1 - Joining all three datasets together
a_join = py_ratings.join(py_users, py_ratings['user_id']==py_users['user_id'],'inner')\
.drop(py_users['user_id'])
#now joing the new a_join object to moviedata dataframe object
movie_lens_join = a_join.join(py_movies, a_join['movie_id']==py_movies['movie_id'], 'inner')\
.drop(a_join['movie_id'])

#instantiate the pyspark movie_lens_join table as a Pandas object
movie_lens_join_pandas = movie_lens_join.toPandas()

#plot scatter chart by occupation (x) and rating (y as a color scale variable)

trace1 = go.Scatter (
    y = movie_lens_join_pandas['occupation'],
    mode = 'markers',
    marker=dict(
    size = 16,
    color = movie_lens_join_pandas['rating'],
    colorscale = 'Viridis',
    showscale = True
    )
)
data = [trace1]
py.iplot(data)
