#PySpark script to join 3 dataframes and produce a horizontal bar chart on the DSS platform
#DSS stands for Dataiku DataScience Studio.
%pylab inline

#Import libraries
import dataiku
import dataiku.spark as dkuspark
import pyspark
from pyspark.sql import SQLContext
import matplotlib
import pandas as pd

# Load PySpark
sc = pyspark.SparkContext()
sqlContext = SQLContext(sc)

# Point to movie lens datasets python_users, python_ratings and python_movie_lens
users_ds = dataiku.Dataset("python_users")
movies_ds = dataiku.Dataset("python_movie_data")
ratings_ds = dataiku.Dataset("python_ratings")

#1 Read datasets into DataFrames (PySpark)
python_users = dkuspark.get_dataframe(sqlContext, users_ds)
python_movie_data = dkuspark.get_dataframe(sqlContext, movies_ds)
python_ratings = dkuspark.get_dataframe(sqlContext, ratings_ds)

#Analysis Piece #2 - Joining all three datasets together

a = python_ratings.join(python_users, python_ratings['user_id']==python_users['user_id'],'inner')\
    .drop(python_users['user_id'])
movie_lens_joined = a.join(python_movie_data, a['movie_id']==python_movie_data['movie_id'], 'inner')\
    .drop(python_movie_data['movie_id'])

#First actual output (user count of new joined dataframe)
print "Record Count of New Movie Lens (Joined) table is: ", movie_lens_joined.count()
print '\n'

#Analysis Piece #3 - Aggregration of ratings to rescale them by occupation

#Extra imports
from pyspark.sql import functions as spfun

#avg rating computation
avgs = movie_lens_joined.groupby('user_id').agg(spfun.avg('rating')\
                                               .alias('avg_rating'))
#join again with intitial
final_avgs = movie_lens_joined.join(avgs, movie_lens_joined['user_id']==avgs['user_id'])\
                                   .drop(avgs['user_id'])

#final column for new rescaled ratings by occupation
df = final_avgs.withColumn('rescaled_rating', final_avgs['rating'] - final_avgs['avg_rating'])

#Analysis Piece #4 - Plot rescaled ratings by occupation
matplotlib.style.use('ggplot')

#Spark Dataframe
stats = df.groupby('occupation').avg('rescaled_rating').toPandas()

#Pandas Dataframe
stats.columns = ['occupation', 'rescaled_rating']
stats = stats.sort('rescaled_rating', ascending = True)

#2nd actual output (horizontal bar chart of ratings rescaled by occupation)
stats.plot(kind = 'barh', x='occupation', y='rescaled_rating', figsize = (14,8))

#Analysis Piece #5 - Print Summary (3rd Output of 3) Information on the job
print "Summary Information of Movie Lens Data Sets"
print "-------------------------------------------"
print "Users DataFrame Count is ", python_users.count()
print "Rating DataFrame Count is ", python_ratings.count()
print "Movies DataFrame Count is ", python_movie_data.count()
print "-------------------------------------------"
print "Users Table Snippet & Schema are: "
print '\n'
print python_users.show()
print '\n'
print python_users.printSchema()
print "-------------------------------------------"
print "Rating Table Snippet & Schema are: "
print '\n'
print python_ratings.show()
print '\n'
print python_ratings.printSchema()
print "-------------------------------------------"
print "Movies Table Snippet & Schema are: "
print '\n'
print python_movie_data.show()
print '\n'
print python_movie_data.printSchema()
print "-------------------------------------------"
