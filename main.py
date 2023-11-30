import Inventory
import User
import cart

#class declaration
I = Inventory.Inventory("Inventory.db","Inventory")
C = cart.Cart("Cart.db","Cart")
user = User.User("User.db", "Users")

closed = False
#Before Login
while True:
    print("""1. Log In to an Existing Account
         2. Create an Account
         3. Close the Site
         Which option would you like to select?\n""")

    user_input = input("")
            
    if user_input == "3" :
        #sets closed equal to true to ensure the user doesnt go to the after login menu
        closed = True
        break
        
    elif user_input == "1":
        if not user.login():
            print("Login failed.")
            continue
        else:
            print("Login successful.")
            break
            
    elif user_input == "2":
        user.createAccount()
        break
            
    else:
        print("Invalid menu option. Please try again.")

#After Login Menu

#if statement to make sure user is logged in or made an account
if not closed:
    while True:
        print("""1. Logout
            2. View Account Information
            3. Inventory Information
            4. Cart Information
            \n""")
        #gets user input for menuing
        menu_option = input("Please select a menu option:")

        #logs the user out of the site
        if menu_option == "1":
            user.logout()
            break
        
        #views the information of the user
        if menu_option == "2":
            user.viewAccountInformation()

        #menu option for inventory information
        if menu_option == "3":
            #After Login
            option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")
            while option != "2":

                #option = input("Please select a menu option:\n (0) View Inventory\n(1) Search Inventory:  ")
                if option == "0":
                    I.viewInventory()
                elif option == "1":
                    I.searchInventory()
                option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")

        if menu_option == "4":
            #AFTER LOGIN -- CART INFO

            cartoptions = input("Please select a menu option:\n(0) View Cart\n(1) Add Items to Cart\n(2) Remove an Item from Cart\n(3) Check Out\n(4) Go Back: ")
            while cartoptions != "4":
                if cartoptions == "0":
                    C.viewcart(user.getUserID,I.getdatabaseName)
                elif cartoptions == "1":
                    ad = input("Please type ISBN of book: ")
                    C.additem(user.getUserID, ad)
                elif cartoptions == "2":
                    re = input("Please type ISBN of book: ")
                    C.additem(user.getUserID, re)
                    C.removeitem
                elif cartoptions == "3":
                    C.checkout(user.getUserID)

