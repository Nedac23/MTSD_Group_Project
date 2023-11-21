import Inventory

#class declaration
I = Inventory.Inventory("Inventory.db","books")



#After Login
option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")
while(option != "2"):

    #option = input("Please select a menu option:\n (0) View Inventory\n(1) Search Inventory:  ")
    if(option == "0"):
        I.viewInventory()
    elif(option == "1"):
        I.searchInventory()
    option = input("Please select a menu option:\n(0) View Inventory\n(1) Search Inventory\n(2) Go Back:  ")



