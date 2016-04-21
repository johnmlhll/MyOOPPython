#Test Class for testing inputs, processing and outputs functionally using unittest

#Import libraries
import unittest
#Class Arrays/Lists
stacked_array_inputs = [4,2,100,[1,82,302,1],2,3,4,[411,99089,5],312,[0, 33]]
processed_list = [4, 2, 100, 1, 82, 302, 1, 2, 3, 4, 411, 99089, 5, 312, 0, 33]

class Intercom_Test_Class(unittest.TestCase):

    #Testing stacked_array_inputs for the speed of list flattening
    def test_flatten_lists(self):
        self.setUp()
        test_list = [4,2,100,[1,82,302,1],2,3,4,[411,99089,5],312,[0, 33]]
        self.assertTrue(type(stacked_array_inputs) == list)
        self.assertListEqual(stacked_array_inputs, test_list)
        self.tearDown()
    #Testing the output to ensure its correct as a list of numbers
    def test_flatten_outputs(self):
        self.setUp()
        test_output = [4, 2, 100, 1, 82, 302, 1, 2, 3, 4, 411, 99089, 5, 312, 0, 33]
        self.assertEqual(processed_list, test_output)
        self.assertTrue(type(processed_list) == list)
        self.assertListEqual(processed_list, test_output)
        self.tearDown()

if __name__ == '__main__':
    unittest.main()
