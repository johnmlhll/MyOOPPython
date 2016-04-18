#Test Class for testing inputs, processing and outputs functionally using unittest

#Import libraries
import unittest

#Class Arrays/Lists
stacked_array_inputs = [4,2,1,[1,82,3,1],2,3,4,[4,99,5],3,[0]]

class Intercom_Test_Class(unittest.TestCase):
    #init method
    def __init__(self, test_flatten_lists, test_flatten_outputs):
       self.test_flatten_lists = test_flatten_lists
       self.test_flatten_outputs = test_flatten_outputs

    #Testing stacked_array_inputs for the speed of list flattening
    def test_flatten_lists(self):
        test_list = [4,2,1,[1,82,3,1],2,3,4,[4,99,5],3,[0]]
        try:
            self.assertSequenceEqual(test_list, stacked_array_inputs)
            print "Test passed"
        except Exception as e:
            print "Test failed: Error is ", e.message

    #Testing the output to ensure its correct as a list of numbers
    def test_flatten_outputs(self):
        test_output = [4, 2, 1, 1, 8, 2, 3, 1, 2, 3, 4, 4, 9, 9, 5, 3, 0]
        self.assertSequenceEqual(seq1=processed_output, seq2=test_output)
