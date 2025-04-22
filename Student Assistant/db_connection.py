import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def db_connect():
  
    #Establishes a connection to the MySQL database.
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="smsdb"
        )

        if con.is_connected():
            return con  # Return the connection object

    except mysql.connector.Error:
        QMessageBox.critical(None, "Database Error", "Unable to connect. Please contact the system administrator!")
        return None




