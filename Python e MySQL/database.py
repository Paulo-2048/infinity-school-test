import mysql.connector
from mysql.connector import Error

class Connection:
    def __init__(self):
        pass
    
    def connect(self):
        try:
            self.con = mysql.connector.connect(host='127.0.0.1', database='ig_store', user='root', password='19032004pvss')
            if self.con.is_connected():
                return True 
        except Error as e:
            print(e)
            return False