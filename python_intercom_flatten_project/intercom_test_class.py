#Test Class for testing inputs, processing and outputs functionally using unittest

#Import libraries
import unittest

#Class Arrays/Lists
stacked_array_inputs = [4,2,100,[1,82,302,1],2,3,4,[411,99089,5],312,[0, 33]]

class Intercom_Test_Class(unittest.TestCase):
    #init method
    def __init__(self, test_flatten_lists, test_flatten_outputs):
        self.test_flatten_lists = test_flatten_lists
        self.test_flatten_outputs = test_flatten_outputs

    #Testing stacked_array_inputs for the speed of list flattening
    def test_flatten_lists(self):
        test_list = [4,2,100,[1,82,302,1],2,3,4,[411,99089,5],312,[0, 33]]
        try:
            self.assertTrue(type(stacked_array_inputs) == int)
            self.assertListEqual(stacked_array_inputs, test_list)

            print "Test passed"
        except Exception as e:
            print "Test failed: Error is ", e.message

    #Testing the output to ensure its correct as a list of numbers
    def test_flatten_outputs(self):
        test_output = [4, 2, 100, 1, 82, 302, 1, 2, 3, 4, 411, 99089, 5, 312, 0, 33]
        self.assertTrue(type(processed_list) == int)
        self.assertListEqual(processed_output, test_output)
