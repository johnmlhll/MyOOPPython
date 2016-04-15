# -*- coding: utf-8 -*-
# Creating a python script to import a weeks worth of partitioned by day files
# The files are daily bike data for a  week in 2012 (7 files imported in total)

# Import Libraries
import os
import dataiku
import pandas as pd

# After partitioning the files by day in Dataiku UI, I called the dataiku variable for
# assigning the data by day of the partitioned files
DATE = dataiku.dku_flow_variables["DKU_DST_DATE"].replace('-', '')

# Recipe inputs
in_folder = dataiku.Folder("v8azAA1T")
in_path = in_folder.get_path()

# Read in data
file_name = 'capitalbikeshare_trip_data_'+DATE+'.csv'
file_path = os.path.join(in_path, file_name)
print '[+] Processing File: {}'.format(file_name)
df = pd.read_csv(file_path, sep='|', quotechar='"')

# Recipe outputs
bike_dataset = dataiku.Dataset("bike_dataset")
bike_dataset.write_with_schema(df)
