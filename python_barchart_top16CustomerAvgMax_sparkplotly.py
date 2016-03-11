#Produce a Bar Chart comparing top 16 sales (volume) customers avg sales count
#to max sale count from an aggregrated click stream dataset.
#Each space denotes a different cell in Jupyter Notebooks.
#Platform and Data Source is Dataiku | DSS

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

#Assign customer_ids to "ID" from 1-20 (sequental) for presentation purposes on the X-Axis
customer_id = intCS_df_pandas['customer_id']
cust_id=[]
for id in cust_id:
    cust_id='ID'.join(id)

#Plot Data and Data variables for bars on chart
#average sales total (avg of count of bookings) by cust_id
trace1 = go.Bar(
    x = cust_id,
    y = intCS_df_pandas['sales_avg'],
    name='Average Sales by Customer_id',
    marker=dict(
        color='rgb(0,191,255)'
    )
)
#max sales by customer_id
trace2 = go.Bar(
    x = cust_id,
    y = intCS_df_pandas['sales_max'],
    name='Max Sales by Customer_id',
    marker=dict(
        color='rgb(205,92,92)'
    )
)
data=[trace1, trace2]

#Define graph layout
layout = go.Layout(
    title = "Top 16 Visitor_Id Avg_Bookings to Booking_Max",
    xaxis=dict(
    title='Top 16 Visitor_id (Booking_Max/City_Count > 5) Numbers',
    tickfont=dict(
            size=14,
            color='rgb(107,107,107)'
        )
    ),
    yaxis=dict(
    title='Count Value - Bookings/Cities',
    titlefont=dict(
        size=16,
        color='rgb(107,107,107)'
    ),
    tickfont=dict(
            size=14,
            color='rgb(107,107,107)'
        )
    ),
    legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255,255,255,0)',
        bordercolor='rgba(255,255,255,0)'
    ),
    barmode='group',
    bargap=0.15,
    bargroupgap=0.1
)

#plot the figure and graph it as final output
fig=go.Figure(data=data, layout=layout)
py.iplot(fig)
