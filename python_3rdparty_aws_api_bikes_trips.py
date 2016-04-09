# -*- coding: utf-8 -*-
# Python script on DSS DataScienceStudio - Dataiku to import bike data from an API (Amazon)
# Import 2012 Bike trip Data from CapitalBike share using AmazonAWS API
# DSS platform folder for the url data imports is bikes_trip_data
# Its a flexible script approach as no input data sources used on DSS

# Import libraries
import os
import urllib
import dataiku

# List settings for 2012 data imports
QUARTERS = ['2012-Q1','2012-Q2','2012-Q3','2012-Q4']

# Recipe outputs - Folder download and path details for actual data imports
bikes_trip_data = dataiku.Folder("2hJoIUww")
bikes_trip_data_path = bikes_trip_data.get_path()

# Download the actual data imports
retriever = urllib.URLopener()
base_url = 'https://s3.amazonaws.com/capitalbikeshare-data'
suffix = '-cabi-trip-history-data.zip'

#Run the actual downloads, create filenames and assign them to the folderpath
for quarter in QUARTERS:
    filename = '{}{}'.format(quarter, suffix)
    source_url='{}/{}'.format(base_url, filename)
    target_dir = os.path.join(bikes_trip_data_path, filename)
    retriever.retrieve(source_url, target_dir)
    print '[+] Downloaded {}...'.format(filename)
