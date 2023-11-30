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
    def __init__(self, database, table):
        self.database = database
        self.table = table

    #real functions

    def viewcart(self, userID, invdatabase):
        #for the cart db
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection. Cart")

        except:
            print("Failed connection. Cart")

            sys.exit()

        #for the inventory db
        try:
            invconnection = sqlite3.connect(invdatabase)

            print("Successful connection. INV")

        except:
            print("Failed connection. INV")

            sys.exit()

        cursor = connection.cursor()
        invcursor = invconnection.cursor()




        #grabs the ISBNs from the cart db and puts them in a list alongside their quantities

        query = ("SELECT * FROM Cart WHERE userID =?")
        data = (userID)
        cursor.execute(query,(str(userID),))
        result = cursor.fetchall()
        print(result)
       #uses the grab bed isbn values to get the correct rows from the inventory class
        #invquery = ("SELECT * FROM Inventory WHERE ISBN =?")
        invres = []
        for x in result:
            print(x)
            invquery = ("SELECT * FROM Inventory WHERE ISBN =?")
            invdata = (x[1])
            invcursor.execute(invquery,(str(invdata),))
            invres += invcursor.fetchall()
            
        print(invres)
       # invcursor.execute(invquery,invdata)
        


        ###SELECT * FROM Books JOIN Cart ON Books.ISBN =Cart.ISBN

        #with the isbn list, use code from inventory.py to see the actual data of what the isbns are books of and also relay their
        #quantity. x[0] should be isbn and x[1] should be quantity
        for x, y in zip(invres,result):
            print(f"Title: {x[1]}, ISBN: {x[0]}, Quantity: {y[2]}")    


        cursor.close()
        invcursor.close()
        connection.close()
        invconnection.close()

    def addtocart(self, userID, ISBN):
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            sys.exit()
        qvar = "1"
        #fcursor = connection.cursor()

        #fquery = ("SELECT Quantity WHERE userID =? AND ISBN =?")
        #fdata = (userID,ISBN)
        #fcursor.execute(fquery,fdata)
        #result = fcursor.fetchall
        #fcursor.close()
        cursor = connection.cursor()
        #if (result(0) > 0):
        #    query = ("UPDATE cart SET Quantity =? Where ISBN =? and userId =?")
        #    data = (result(0)+1,ISBN,userID)
        #    cursor.execute(query,data)
        #else:
        query = ("INSERT INTO Cart (userID, ISBN, Quantity) VALUES (?, ?, ?)")
        data = (userID, ISBN, str(qvar))
        cursor.execute("INSERT INTO Cart (userID, ISBN, Quantity) VALUES (?, ?, ?)",(str(userID),str(ISBN),str(qvar),))

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


        data = (str(userID), str(ISBN),)

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
        cursor.execute(invquery,(str(userID),))
        result = cursor.fetchall()
        print(result)
        I = Inventory.Inventory("Inventory.db","Inventory")
        for x in result:
            I.decreaseStock(str(x[0]),)

        

        query = "DELETE FROM Cart WHERE userID = ?"

        ## sends query and data
        cursor.execute(query, (str(userID),))

        ## commits change
        connection.commit()

        ## shows changes
        print(cursor.rowcount, "record(s) deleted.")


        cursor.close()
        connection.close()