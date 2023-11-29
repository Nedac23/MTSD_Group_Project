from inspect import _void
import sqlite3
import sys
class Inventory:
    #zero consturctor
    def __init__(self):
       self.databaseName = ""
       self.tableName = ""
    #consturctor
    def __init__(self, databaseName,tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    #setter for databaseName
    def setdatabaseName(self, databaseName):
        self.databaseName = databaseName
    #setter for tableName
    def settableName(self, tableName):
        self.tableName = tableName
    
    #getter for databaseName
    def getdatabaseName(self):
        return self.databaseName
    
     #getter for tableName
    def gettableName(self):
        return self.tableName
    #view inventory function
    def viewInventory(self):
            #testing connection to database
            try:
                connection = sqlite3.connect("Inventory.db")

                print("Successful connection.")

            except:
                print("Failed connection.")

            ## exits the program if unsuccessful
                sys.exit()
                
            print()
            ## cursor to send queries through
            cursor = connection.cursor()
            #executing SQL Query
            cursor.execute("SELECT * FROM books")

            #Gets the results of the query
            result = cursor.fetchall()
            #prints the results
            for x in result:
                print("Inventory: ")
                print("\n")
                print("ISBN:", x[0]," Title:", x[1], " Author:", x[2], "Genre:", x[3], "Pages:", x[4], "Release Date:", x[5], "Stock", x[6] ) 
                print("\n")


            ## close the cursor and connection once you're done
            cursor.close()
            connection.close()
            return 0
    
    #search Inventory function
    def searchInventory(self):
        try:
            connection = sqlite3.connect("Inventory.db")

            print("Successful connection.")

        except:
            print("Failed connection.")

        ## exits the program if unsuccessful
            sys.exit()
            
        print()
        ## cursor to send queries through
        cursor = connection.cursor()

        title = input("Please enter the title of the book you would like to search for: ")
        query = "SELECT * FROM books WHERE Title =? "
        data = (title,)
        cursor.execute(query, data)
        
        result = cursor.fetchall()
        if(len(result) == 0):
            print("Nothing Found") 
        else:
            for x in result:
                if(x[1] == title):
                    print("Title: ", x[1]) 
                    print("\n")
     
        cursor.close()
        connection.close()
    
        return 0

    #decrease stock function
    def decreaseStock(self, ISBN):
        #testing connection
        stock_count = 0
        try:
                connection = sqlite3.connect("Inventory.db")

                print("Successful connection.")

        except:
                print("Failed connection.")

            ## exits the program if unsuccessful
                sys.exit()
                
        print()
        ## cursor to send queries through
        cursor = connection.cursor()

        #selects the stock value using the ISBN since it is unique
        query = "SELECT * FROM books WHERE ISBN =? "
        data = (ISBN,)
        cursor.execute(query, data)

        #results from the select query
        result = cursor.fetchall()
       #sets the result to the varibale stock_count
        for x in result:
           stock_count = (x[6])
           #print(stock_count)
        
       #decreases the stock
        if(stock_count == 0):
            stock_count = 0
        else:
            stock_count = stock_count - 1
       # print(stock_count)

       #updates the database with the new stock value
        query = "UPDATE books SET Stock =? Where ISBN =? "
        data = (stock_count, ISBN,)
        cursor.execute(query,data)

        #commits changes
        connection.commit()
        #closes cursor and connection
        cursor.close()
        connection.close()
        return 0
        
       

        
