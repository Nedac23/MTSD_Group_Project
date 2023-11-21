import sqlite3
import sys
import Inventory



# most of the sql code is just the stuff from the python databases example code directly 
#


class Cart:
    #initalizers 
    def __init__(self):
        self.database = ""
        self.table = ""
    def __init__(self, database="", table=""):
        self.database = database
        self.table = table

    #real functions

    def viewcart(self, userID, invdatabase):
        #for the cart db
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        #for the inventory db
        try:
            invconnection = sqlite3.connect(invdatabase)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()
        invcursor = invconnection.cursor()




        #grabs the ISBNs from the cart db and puts them in a list alongside their quantities

        query = ("SELECT ISBN, Quantity FROM Cart WHERE userID =?")
        data = (userID)
        cursor.execute(query,data)
        result = cursor.fetchall()
        #uses the grabbed isbn values to get the correct rows from the inventory class
        invquery = ("SELECT * FROM Inventory WHERE ISBN =?")
        invdata = (result[0])
        invcursor.execute(invquery,invdata)
        invresult = invcursor.fetchall()


        ###SELECT * FROM Books JOIN Cart ON Books.ISBN =Cart.ISBN

        #with the isbn list, use code from inventory.py to see the actual data of what the isbns are books of and also relay their
        #quantity. x[0] should be isbn and x[1] should be quantity
        for x in result:
            print(f"Title: 
                  {x[0]},{x[1]}
                  ")    


        cursor.close()
        invcursor.close()
        connection.close()
        invconnection.close()

    def addtocart(self, userID="", ISBN=""):
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        fcursor = connection.cursor()

        fquery = ("SELECT Quantity WHERE userID and ISBN = ?")
        fdata = (userID, ISBN)
        fcursor.execute(fquery,fdata)
        result = fcursor.fetchall
        fcursor.close()
        cursor = connection.cursor()
        if (result(0) > 0):
            query = ("UPDATE cart SET Num =? Where ISBN =? and userId =?")
            data = (result(0)+1,ISBN,userID)
            cursor.execute(query,data)
        else:
            query = ("INSERT INTO Cart (userID, ISBN, Quantity) VALUES (?, ?, ?)")
            data = (userID, ISBN, 1)
            cursor.execute(query,data)

        connection.commit()

        ## shows changes
        print(cursor.rowcount, "record(s) inserted.")

        cursor.close()
        connection.close()

    def removefromcart(self, userID="", ISBN=""):
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()


        query = "DELETE FROM Cart WHERE userID = ? AND ISBN = ?"


        data = (userID, ISBN,)

        ## sends query and data
        cursor.execute(query, data)

        ## commits change
        connection.commit()

        ## shows changes
        print(cursor.rowcount, "record deleted.")
        print()


        cursor.close()
        connection.close()

    def checkout(self, userID=""):
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()

        cursor = connection.cursor()



        invquery = ("SELECT ISBN FROM Cart WHERE userID =?")
        invdata = (userID)
        cursor.execute(invquery,invdata)
        result = cursor.fetchall()
        inv = Inventory()
        for x in result:
            inv.decreaseStock(x[0])
        #idk how to do cross class stuff in python so for this moment im leaving it and doing it later

        

        query = "DELETE FROM Cart WHERE userID = ?"
        data = userID

        ## sends query and data
        cursor.execute(query, data)

        ## commits change
        connection.commit()

        ## shows changes
        print(cursor.rowcount, "record(s) deleted.")


        cursor.close()
        connection.close()