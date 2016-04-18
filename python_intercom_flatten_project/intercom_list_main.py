#The Challenge: Intercom Test (Q2) for inputting and flattening an array
#without using libraries that have a flatten method or function (none in Python).
#Solution Notes: Programming approach used is OOP,language choice allows for
#functional Programming flexibility. Applicant name is John Mulhall @johnmlhll

#Import Classes for calling class methods
from intercom_list_flattener import Intercom_List_Flattener
from intercom_test_class import Intercom_Test_Class

#Main Class
class Intercom_Main_Flatten_Arrays(object):
    def __init__(self, stacked_array_inputs, flatten):
        self.stacked_array_inputs = stacked_array_inputs
        self.flatten = flatten

        #call tests - dev only
        #instantiate test class
        test = Intercom_Test_Class()

        #call tests
        test.test_flatten_lists()
        test.test_flatten_outputs()

        #instantiate list flattener class
        flat = Intercom_List_Flattener()

        #method call
        flat.flatten


    if __name__=='__main__':
        print 'Your flattened list of lists sir...'
        print 'Thank you for using this flatten program... have a great day!'
