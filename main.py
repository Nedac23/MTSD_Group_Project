import Inventory
import User
import Cart

#class declaration
I = Inventory.Inventory("Inventory.db","books")

#Before Login
user = User("User.db", "Users")

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



