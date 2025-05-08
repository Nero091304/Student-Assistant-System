import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def db_connect():
    try:
        con = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sasdb"
        )

        if con.is_connected():
            return con  

    except mysql.connector.Error:
        QMessageBox.critical(None, "Database Error", "Unable to connect. Please contact the system administrator!")
        return None




