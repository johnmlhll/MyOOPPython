# Unit test the program "customers.py"
# Confirm methods to invite customers <100km away work as expected

#import libraries
import unittest
from customers import Customers

#instantiate class for test purposes
tcust = Customers()


class Test_Class(unittest.TestCase):

    #test method 1 - test file import
    def test_get_file_path(self):
        self.setUp()
        self.assertTrue(type(tcust.isValid) == bool)
        self.assertFalse(tcust.isValid)
        self.assertTrue(type(tcust.file_path) == str)
        self.assertTrue(tcust.file_path == "")
        self.assertRaises(Exception, tcust.get_file_path())
        self.assertTrue(tcust.get_file_path())
        self.tearDown()

    #test method 2 - read customer file
    def test_read_customer_file(self):
        self.setUp()
        self.assertTrue(type(tcust.lines) == dict)
        self.assertTrue(tcust.lines == {})
        self.assertRaises(Exception, tcust.read_customer_file())
        self.assertTrue(tcust.read_customer_file())
        self.tearDown()

    #test method 3 - test processing
    def test_process_customer_coordinates(self):
        self.setUp()
        self.assertTrue(tcust.customer_lines == {})
        self.assertTrue(tcust.invite_dict == {})
        self.assertTrue(tcust.invite_file == "")
        self.assertTrue(type(tcust.customer_lines) == dict)
        self.assertTrue(type(tcust.invite_dict) == dict)
        self.assertTrue(type(tcust.invite_file) == str)
        self.assertRaises(Exception, tcust.process_customer_coordinates())
        self.tearDown()

    #Test method 4 - printing str object results (invite list)
    def test_print_invite_list(self):
        self.setUp()
        self.assertTrue(tcust.isValid)
        self.assertTrue(tcust.invite_file == "")
        self.assertTrue(type(tcust.invite_file) == str)
        self.assertRaises(Exception, tcust.print_invite_list())
        self.tearDown()

if __name__ == '__main__':
    unittest.main()
