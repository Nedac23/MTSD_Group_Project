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
            cursor.execute("SELECT * FROM books")


            result = cursor.fetchall()
            for x in result:
   
                print("ISBN:", x[0],"Title:", x[1], "\tAuthor:", x[2] ) ## only the ISBN
                print("\n")


            ## close the cursor and connection once you're done
            cursor.close()
            connection.close()
            return 0
    
    #search Inventory function
    def searchInventory(self):
        return 0
    #decrease stock function
    def decreaseStock(self, ISBN):
        return 0


        
