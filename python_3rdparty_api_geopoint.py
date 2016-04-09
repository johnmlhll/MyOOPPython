# -*- coding: utf-8 -*-
# This script using the DSS-Dataiku platform and calls the API of the FCC.

# Import Libraries for API call from FCC for address details to match long-lat coordinates
import dataiku
import requests
import pandas as pd


# Recipe inputs
ds = dataiku.Dataset("bike_station1_prepared")

# Function to pass lat and long to the fcc 3rd party API to get back geo-pointed blocks
def get_block(lat, lon):
    data = {
        'format': 'json',
        'showall': 'true',
        'latitude': lat,
        'longitude': lon
    }
    r = requests.get('http://data.fcc.gov/api/block/find', params=data)
    if r.status_code == 200:
        return r.json()
    else:
        return None

# Iterative processing of records against the 3rd party API
results=[]

for record in ds.iter_rows():
    o = {}
    o['station_id'] = record['id']
    block_data = get_block(record.get('lat'), record.get('long'))
    block_id = block_data['Block']['FIPS']
    o['block_id'] = block_id
    o['block_group'] = block_id[:12]
    o['county_id'] = block_data['County']['FIPS']
    o['county_name'] = block_data['County']['name']
    o['state_id'] = block_data['State']['FIPS']
    o['state_code'] = block_data['State']['code']
    o['state_name'] = block_data['State']['name']
    results.append(o)

# Pass into pandas df
odf = pd.DataFrame(results)

# Recipe outputs --test issue, need to see why its failing here.
bsb = dataiku.Dataset("bike_station1_blocks")
bsb.write_with_schema(odf)
