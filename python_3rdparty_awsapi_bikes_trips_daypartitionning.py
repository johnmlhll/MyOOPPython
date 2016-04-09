# -*- coding: utf-8 -*-
# Create a DataScienceStudio-DSS Folder path for partitionning bikes_trip_data
# downloaded data files for 2012

#Import Libraries
import os
import zipfile
import dataiku
import datetime
import pandas as pd

# Recipe inputs (folder)
in_folder = dataiku.Folder("2hJoIUww")
in_path = in_folder.get_path()

# Recipe outputs (folder)
out_folder = dataiku.Folder("v8azAA1T")
out_path = out_folder.get_path()

# File reads of decompressed zips (csv) and assignment to a dataframe
file_names = os.listdir(in_path)
results = pd.DataFrame()

for file_name in file_names:
    nv = file_name.replace('.zip', '.csv')
    path = os.path.join(in_path, file_name)
    with zipfile.ZipFile(path, 'r') as z:
       o = pd.read_csv( z.open(nv) )
       results = pd.concat((results, o))
print results.shape

# Parse the bike date day timestamp
def get_day(date):
    return datetime.datetime.strptime(date,'%m/%d/%Y %H:%M').strftime('%Y%m%d')

results['day'] = results['Start date'].map(get_day)

#Return results in a dataframe per day
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
for day in days:
    print "Doing %s..." %day
    df = results[results['day']==day]
    filename = 'capitalbikeshare_trip_data_{}.csv'.format(day)
    out = os.path.join(out_path, filename)
    df.to_csv(out, sep='|', index=None, quotchar='""')
