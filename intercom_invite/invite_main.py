#The Challenge: Screen a json customer. Main class!
#List and return a party invite list that shows customer names with user_ids,
#which are <100km from the company office coordiantes provided.
#John Mulhall, Twitter @johnmlhll


#import libraries
from customers import Customers

class  Invite_Main(object):

    #call customer class methods
   cust = Customers()

   #Call class methods
   cust.get_file_path()
   cust.read_customer_file()
   cust.process_customer_coordinates()
   cust.print_invite_list()

   if __name__ == '__main__':
      print "\n"
      print "Thank You for using this program.. Have a great day!"
      print "----------------------------------------------------"
