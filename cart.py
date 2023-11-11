import sqlite3
import sys

class Cart:
    def __init__(self, database="", table=""):
        self.database = database
        self.table = table

    def getdatabase(self):
        return self.database

    def gettable(self):
        return self.table

    def setdatabase(self, database):
        self.database = database

    def settable(self, table):
        self.table = table

    def viewcart(self):

