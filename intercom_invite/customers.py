#The Challenge: Q3 of the Intercom Screening Test = Screen a json customer
#list and return a party invite list that shows customer names with user_ids,
#which are <100km from the intercom office coordiantes provided.
#Approach on this one is more functional then OOP/Class driven
#The program has only one input from a json file with a straight
#forward processing path to completion (validated invite list)
#Applicant name is John Mulhall, Twitter @johnmlhll

#import libraries
import json
import os, math
from os.path import expanduser
from pprint import pprint

# Declare variables/dicts/
lines = {}
invite_name = []
invite_user_id = []
invite_dict = {}

# Function 01 - get file path for local machine.
def getFilePath():
    try:
        home = expanduser("~")
        file_path = os.path.join(home, 'customers.json')
    except IOError as fe:
        print "Oh, something went wrong, error message is ",fe.with_traceback
        print 'Welcome, please make sure your .json file is in your home folder: ', home
    return file_path

getFilePath() #function call

# Function 02 - read file and process details from the json read into a dict for processing
def processCustomerFile():
    try:
        # dict/variables
        customer_list = {}
        copy_dict = {}
        invite_count = 0

        #read in json file with dict
        file_name = open(getFilePath())
        lines = file_name.readlines()

        for line in lines:
            customer_list = json.loads(line)
            #process coordinates from dict to see if they are 100km from "home_coordinates"
            HOME_LAT = float(53.3381985)
            HOME_LON = float(-6.2592576)
            EARTH_RADIUS = 6371000 #meters

            lat1 = ''
            lon1 = ''

            #calculation performed in Meters, then aggregrated to Kilometers
            for cust, value in customer_list.iteritems():
                lat1 = float(customer_list["latitude"])
                lon1 = float(customer_list["longitude"])

                dist_lat = math.radians(lat1-HOME_LAT)
                dist_lon = math.radians(lon1-HOME_LON)

                coordinates_conv = math.sin(dist_lat/2) * math.sin(dist_lat/2) + math.cos(math.radians(HOME_LAT))\
                * math.cos(math.radians(dist_lat)) * math.sin(dist_lon/2) * math.sin(dist_lon/2)

                coordinates_calc = 2 * math.atan2(math.sqrt(coordinates_conv), math.sqrt(1 - coordinates_conv))

                coordinates_dist = float(EARTH_RADIUS * coordinates_calc)
                customer_distance = round(coordinates_dist, 2)/1000 #aggregate back to Kilometers

            #Assignent of customer distance to the invite list or not.
            if customer_distance <= 100:
                invite_dict.update(customer_list)
                invite_name.append(invite_dict['name'])
                invite_user_id.append(invite_dict['user_id'])
    except Exception as e:
        print "Oh no, something has gone wrong..."
        print "Error message is ", e.message

processCustomerFile() #function call

def getInviteList():
    print "-------------------------------------------------------"
    print "Validated Customer Invitation List for Intercom Party"
    print "-------------------------------------------------------"
    for i in xrange(len(invite_name)):
        print "Name: ", invite_name[i], "with User ID: ", invite_user_id[i]
    print '\n'
    print 'Note: Validated Customers are located < 100KM from Intercom HQ'
    print "--------------------------------------------------------------"
getInviteList() #function call
