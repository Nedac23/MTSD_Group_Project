import sqlite3
import sys

class User:
    
    #constructors
    def __init__(self):
        self.databaseName = ""
        self.tableName = ""
        self.userID = ""
        self.loggedIn = False
        
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
        
        correct = ""
        
        print("Please enter the information for your new account.\n")
        
        passwordCheck = True

        #inputs
        while correct != "Y":
            first = input("First Name: ")
            last = input("Last Name: ")
            email = input("Email: ")
            password = input("Password: ")
            #Checks if password is already in use
            while passwordCheck == True:
                cursor = connection.cursor()
                cursor.execute(f"SELECT Password FROM Users")
                result = cursor.fetchall()
                passwordCheck = password in result
                if not passwordCheck:
                    password = input("Password taken. Please create a different password: ")
        
            address = input("Street Address: ")
            city = input("City: ")
            state = input("State: ")
            zipcode = input("Zip Code: ")
            payment = input("Payment Method: ")
            
            #Gives user option to change account info before confirmation
            correct = input("Has all your information been entered correctly? (Y/N) ")
            
            while correct != "Y" and correct != "N":
                correct = input("Invalid response. Please try again: (Y/N) ")
            if correct == "N":
                print("\nPlease reenter the information for your new account.\n")
        
        #inserts into the table
        cursor = connection.cursor()
        query = """INSERT INTO Users 
                (Email, Password, FirstName, LastName, Address, City, State, Zip, Payment) 
                VALUES (?, ?, ?, ?, ?, ? ,? ,? ,?)""".replace('\n',' ')
        data = (email, password, first, last, address, city, state, zipcode, payment,)
        cursor.execute(query,data)

        #commits changes
        connection.commit()
        
        #validates
        self.loggedIn = True
        
        cursor.close()
        cursor = connection.cursor()
        
        query = "SELECT UserID FROM Users WHERE Password =?"
        data = (password,)
        cursor.execute(query,data)
        result = cursor.fetchall()
        #stores the userID to the class
        self.userID = result[0]
        
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

        ID = str(self.userID)
        
        query = "SELECT * FROM Users WHERE UserID= ?"
        data = (ID,)
        cursor.execute(query, data)
        
        #Gets the results of the query
        result = cursor.fetchall()
        #prints the results
        for x in result:
            print(f"""Name: {x[3]} {x[4]}
                  Email: {x[1]}
                  Password: {x[2]}
                  Address: {x[5]}, {x[6]}, {x[7]}, {x[8]}
                  Payment: {x[9]} \n""")
            
        #closes the cursor and connection
        cursor.close()
        connection.close()
        
    def login(self):
        #test connection to database
        try:
            connection = sqlite3.connect(self.databaseName)
            print("Successful connection.")
            
        except:
            print("Failed connection.")

            #exit if unsuccessful
            sys.exit()

        cursor = connection.cursor()
        
        print("Please enter your email address and password to login.\n")

        #login verification
        email = input("Email Address: ")
        password = input("Password: ")
        
        try:
            query = "SELECT UserID FROM Users WHERE Email =? AND Password =?"
            data = (email,password,)
            cursor.execute(query,data)
            result = cursor.fetchall()
            
            #stores the userID to the class
            self.userID = result[0]
            
        except:
            print("Email or Password is incorrect.")
            
            cursor.close()
            connection.close()
            return False

        #closes the connection
        cursor.close()
        connection.close()

        #validates 
        self.loggedIn = True
        return True
    
    def logout(self):
        #test connection to database
        try:
            connection = sqlite3.connect(self.databaseName)
            print("Successful connection.")
            
        except:
            print("Failed connection.")

            #exit if unsuccessful
            sys.exit()

        #resets login info
        self.userID = ""
        self.loggedIn = False
        
        return False
