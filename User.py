import sqlite3
import sys

class User:
    
    #constructor
    def __init__(self):
        self.databaseName = ""
        self.tableName = ""
        self.userID = ""
        self.loggedIn = False
        
    #destructor
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.userID = ""
        self.loggedIn = False
      
    #setters    
    def setdatabaseName(self, databaseName):
        self.databaseName = databaseName
        
    def settableName(self, tableName):
        self.tableName = tableName
    
    #getters
    def getdatabaseName(self):
        return self.databaseName
    
    def gettableName(self):
        return self.tableName
    
    def getLoggedIn(self):
        return self.loggedIn
    
    def getUserID(self):
        return self.userID
    
    #account creation function
    def createAccount(self):
        #test connection to database
        try:
            connection = sqlite3.connect(self.database)

            print("Successful connection.")

        except:
            print("Failed connection.")

            #exit if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        
        #inputs (subject to change)
        first = input("First Name: ")
        last = input("Last Name: ")
        email = input("Email: ")
        password = input("Password: ")
        
        address = input("Shipping Address: ")
        city = input("City: ")
        state = input("State: ")
        zipcode = input("Zip Code: ")
        
        payment = input("Payment Method: ")
