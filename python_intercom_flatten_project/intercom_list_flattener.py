#declare global list variables
processed_list = []
str_processed_list = []
final_processed_list = []
stacked_array_inputs = [4,2,1,[1,82,3,1],2,3,4,[4,99,5],3,[0]]
remove_items = []


class Intercom_List_Flattener(object):

    #Init method acting as a constructor
    def __init__(self, stacked_array_inputs, flatten):
        self.stacked_array_inputs = stacked_array_inputs
        self.flatten = flatten

    #Generator Method to flatten list
    def flatten(stacked_array_inputs):
        try:
            #[map(int, item.split(",")) for item in str(stacked_array_inputs)]
            for item in stacked_array_inputs:
                for subitem in str(item):
                    if subitem.isdigit():
                        processed_list.append(subitem)
            #remove non numeric characters from the list, then back to int list
            for p in processed_list:
                if p.isdigit():
                    str_processed_list.append(p)
            final_processed_list = map(int, str_processed_list)
            return final_processed_list
        except Exception as e:
                print "Something with wrong with the flattening of the list"
                print "Error message is ",e.message
        else:
            print "Oh, no list was processed this time. try again..."
    print flatten(stacked_array_inputs)
