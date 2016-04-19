#declare global list variables
processed_list = []
stacked_array_inputs = [4,2,100,[1,82,302,1],2,3,4,[411,99089,5],312,[0, 33]]


class Intercom_List_Flattener(object):

    #Init method acting as a constructor
    def __init__(self, stacked_array_inputs, flatten):
        self.stacked_array_inputs = stacked_array_inputs
        self.flatten = flatten

    #Generator Method to flatten list
    def flatten(stacked_array_inputs):
        try:
            for item in stacked_array_inputs:
                if type(item) == int:
                    processed_list.append(item)
                else:
                    for subitem in item:
                        processed_list.append(subitem)
            return processed_list
        except Exception as e:
                print "Something with wrong with the flattening of the list"
                print "Error message is ",e.message
        else:
            print "List processing completed... please check for errors..."

    print flatten(stacked_array_inputs) #TEST CODE
