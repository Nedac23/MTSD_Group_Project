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
            connection = sqlite3.connect(self.databaseName)

            print("Successful connection.")

        except:
            print("Failed connection.")

            #exit if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        
        correct = ""
        
        #inputs (subject to change)
        
        print("Please enter the information for your new account.\n")
        
        while correct != "Y":
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            password = input("Password: ")
        
            address = input("Street Address: ")
            city = input("City: ")
            state = input("State: ")
            zipcode = input("Zip Code: ")
            payment = input("Payment Method: ")
            
            correct = input("Has all your information been entered correctly? (Y/N) ")
            
            while correct != "Y" and correct != "N":
                correct = input("Invalid response. Please try again: (Y/N) ")
            if correct == "N":
                print("\nPlease reenter the information for your new account.\n")
        
        
        #inserts into the table
        query = """INSERT INTO Users 
                (Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) 
                VALUES (?, ?, ?, ?, ?, ? ,? ,? ,?)""".replace('\n',' ')
        data = (email, password, first, last, address, city, state, zipcode, payment,)
        cursor.execute(query,data)
        
        #validates
        self.loggedIn = True
        
        query = "SELECT UserID FROM Users WHERE FirstName =? AND LastName =? AND Password =?"
        data = (first, last, password,)
        #stores the userID to the class
        self.userID = cursor.fetchall()
        
        #closes the cursor and connection
        cursor.close()
        connection.close()
        
    def viewAccountInformation(self):
        #test connection to database
        try:
            connection = sqlite3.connect(self.databaseName)

            print("Successful connection.")

        except:
            print("Failed connection.")

            #exit if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        
        cursor.execute(f"SELECT * FROM Users WHERE UserID LIKE \"{self.userID}\"")
        
        #Gets the results of the query
        result = cursor.fetchall()
        #prints the results
        for x in result:

            print(f"""Name: {x[2]} {x[3]}
                  Email: {x[0]}
                  Password: {x[1]}
                  Address: {x[4]}, {x[5]}, {x[6]}, {x[7]}
                  Payment: {x[8]} \n""")
            
        #close the cursor and connection
        cursor.close()
        connection.close()
