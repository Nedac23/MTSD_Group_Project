import Inventory
import User
import Cart  #also looking at her python example file she imported it as ->>    from {classname} import *

#class declaration
I = Inventory.Inventory("Inventory.db","Inventory")    #looking at her python example file i don't think we need to do Class.Class
C = Cart("Cart.db","Cart")
user = User("User.db", "Users")
#Before Login


while(True):
    print("""1. Log In to an Existing Account
         2. Create an Account
         3. Close the Site
         Which option would you like to select?\n""")

    user_input = input("")
            
    if(user_input == "3"):
        break
        
    elif(user_input == "1"):
        user.login()
            
    elif(user_input == "2"):
        user.createAccount()
            
    else:
        print("Invalid menu option. Please try again.")
            

#After Login
option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")
while(option != "2"):

    #option = input("Please select a menu option:\n (0) View Inventory\n(1) Search Inventory:  ")
    if(option == "0"):
        I.viewInventory()
    elif(option == "1"):
        I.searchInventory()
    option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")

#AFTER LOGIN -- CART INFO
cartoptions = input("Please select a menu option:\n(0) View Cart\n(1) Add Items to Cart\n(2) Remove an Item from Cart\n(3) Check Out\n(4) Go Back: ")
while(cartoptions != 4):
    if(option == 0):
        C.viewcart(user.getUserID,I.getdatabaseName)
    elif(option == 1):
        ad = input("Please type ISBN of book: ")
        C.additem(user.getUserID, ad)
    elif(option ==2):
        re = input("Please type ISBN of book: ")
        C.additem(user.getUserID, re)
        C.removeitem
    elif(option == 3):
        C.checkout(user.getUserID)

