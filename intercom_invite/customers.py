#The Challenge: Screen a json customer
#list and return a party invite list that shows customer names with user_ids,
#which are <100km from the company office coordiantes provided.
#John Mulhall, Twitter @johnmlhll

#import libraries
import json
import os, math
from os.path import expanduser
from pprint import pprint

# Declare variables/dicts/
invite_dict = {}
file_path = ""
invite_file = ""
lines = {}
isValid = False


class Customers(object):
   #instance dict declaration
   customer_lines = {}

   def __init__(self):
      self.file_path = file_path
      self.customer_lines = self.customer_lines
      self.invite_dict = invite_dict
      self.lines = lines
      self.invite_file = invite_file
      self.isValid = isValid

    # Method 01 - get file path for local machine.
   def get_file_path(self):
      try:
         print '\n'
         file_name = raw_input("Please enter your file name in home folder now: ")
         self.file_path = os.path.join(expanduser('~')+'/',file_name)
         if os.path.exists(self.file_path):
            self.isValid = True
         return self.file_path
      except Exception, e:
         print "\n"
         print "Oh, something went wrong in getting your file and validating it..."
         print "Error message is ", str(e)
         print 'Please make sure your .json file is in your home folder... '

    # Method 02 - read file and process records
   def read_customer_file(self):
      try:
         #read in json file with dict
         file_name = open(self.file_path)
         self.lines = file_name.readlines()
         print '\n'
         return self.lines
      except Exception, e:
         print "\n"
         print "Oh no, something has gone wrong in method read_customer_file()..."
         print "Error message is ", str(e)

    #Method 03 - process customer list coordinates from readCustomerFile() againts home coordinates
   def process_customer_coordinates(self):
      #process coordinates from dictLine to see if they are 100km from "home_coordinates"
      HOME_LAT = float(53.3381985)
      HOME_LON = float(-6.2592576)

      EARTH_RADIUS = 6371000 #meters
      lat1 = ''
      lon1 = ''
      customer_distance = 0
      desired_distance  = 100

      for line in self.lines: #Iterate over lines and then load the line for processing
         self.customer_lines = json.loads(line)
         try:
            #calculation performed in Meters, then aggregrated to Kilometers
            for (key), (value)  in self.customer_lines.iteritems():
               lat1 = float(self.customer_lines["latitude"])
               lon1 = float(self.customer_lines["longitude"])
               dist_lat = math.radians(lat1-HOME_LAT)
               dist_lon = math.radians(lon1-HOME_LON)

               coordinates_conv = math.sin(dist_lat/2) * math.sin(dist_lat/2) + math.cos(math.radians(HOME_LAT))\
               * math.cos(math.radians(dist_lat)) * math.sin(dist_lon/2) * math.sin(dist_lon/2)

               coordinates_calc = 2 * math.atan2(math.sqrt(coordinates_conv), math.sqrt(1 - coordinates_conv))
               coordinates_dist = float(EARTH_RADIUS * coordinates_calc)

               customer_distance = round(coordinates_dist/1000, 2)

               #Assignent of customer distance to the invite list or not.
               #Assignement also to file object for printing to screen & file
               if customer_distance <= desired_distance:
                  self.invite_dict['distance'] = customer_distance
                  if value not in invite_dict.values():
                     self.invite_dict.update(self.customer_lines)
                     self.invite_file = self.invite_file + "\t%s     \t%s  \t%s\n" % (invite_dict["name"], invite_dict["user_id"], invite_dict["distance"])
            print '\n'
         except Exception, e:
               print "\n"
               print "Oh no, something has gone wrong in method process_customer_coordinates()..."
               print "Error message is ", str(e)

   #Method 04 - return list of customers and Ids within target radius of home office
   def print_invite_list(self):
      try:
         if self.isValid == True and self.invite_file != "":
            print "\t-------------------------------------------------------"
            print "\tValidated Customer Invitation List for Company Party"
            print "\t-------------------------------------------------------"
            print "\tName          \tCustomer ID \tDistance (km) \n"
            print "\t-------------------------------------------------------"
            print self.invite_file
            print '\n'
            print '\tNote: Validated Customers are located < 100KM from Company HQ'
            print "\t--------------------------------------------------------------"
         else:
            print '\n'
            print 'Sorry, your file never validated - please revise and retry...'
      except Exception, e:
            print "\n"
            print "Oh no, something has gone wrong in method process_customer_coordinates()..."
            print "Error message is ", str(e)
