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
        return 0
    #search Inventory function
    def searchInventory(self):
        return 0
    #decrease stock function
    def decreaseStock(self, ISBN):
        return 0


        
