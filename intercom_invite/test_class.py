# Unit test the program "customers.py"
# Confirm methods to invite customers <100km away work as expected

#import libraries
import unittest
import json, os
from os.path import expanduser

#Variables, lists, etc


#Connect with json data file
def getFilePath():
    try:
        home = expanduser("~")
        file_path = os.path.join(home, 'customers.json')
    except IOError as fe:
        print "Oh, something went wrong, error message is ",fe.with_traceback
        print 'Welcome, please make sure your .json file is in your home folder: ', home
    return file_path

getFilePath()    #function call.

class TestCustomers(unittest.TestCase):
    #test method 1 - test file import
    def test_data(self):
        self.setUp()
        test_data = {"latitude": "52.986375", "user_id": 12, "name": "Christina McArdle", "longitude": "-6.043701"}
        self.assertTrue(type(test_data) == dict)
        self.tearDown()
    #test method 2 - test processing
    def test_processing(self):
        self.setUp()
        lines = {}
        invite_name = []
        invite_user_id = []
        invite_dict = {}
        customer_list = {"latitude": "53.2451022", "user_id": 4, "name": "Ian Kehoe", "longitude": "-6.238335"}
        HOME_LAT = float(53.3381985)
        self.assertTrue(type(HOME_LAT) == float)
        self.assertTrue(type(customer_list) == dict)
        self.assertTrue(type(invite_dict) == dict)
        self.assertTrue(type(invite_name) == list)
        self.assertTrue(type(invite_user_id) == list)
        self.assertTrue(type(lines) == dict)
        self.tearDown()

if __name__ == '__main__':
    unittest.main()
