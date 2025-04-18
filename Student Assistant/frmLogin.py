import sys #interact with the system with the command line
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QVBoxLayout, QWidget #Provides GUI components
from db_connection import db_connect  # Import the database connection function

class frmLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form") 
        self.setGeometry(700, 150, 477, 710) # size and coordinates
        self.cp = 0  # Counter for failed attempts
        
        layout = QVBoxLayout()
        
        # Username Label and Input
        self.lblUser = QLabel("Username:")
        layout.addWidget(self.lblUser)
        self.txtUser = QLineEdit()
        layout.addWidget(self.txtUser)
        
        # Password Label and Input
        self.lblPass = QLabel("Password:")
        layout.addWidget(self.lblPass)
        self.txtPass = QLineEdit()
        self.txtPass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.txtPass)
        
        # Show Password Checkbox
        self.show_password = QCheckBox("Show Password")
        self.show_password.stateChanged.connect(self.toggle_password)
        layout.addWidget(self.show_password)
        
        # Login Button
        self.btnLogin = QPushButton("Login")
        self.btnLogin.clicked.connect(self.login)
        layout.addWidget(self.btnLogin)
        
        # Exit Button
        self.btnClose = QPushButton("Exit")
        self.btnClose.clicked.connect(self.exit_app)
        layout.addWidget(self.btnClose)
        
        self.setLayout(layout)
        
    def toggle_password(self):
        """Toggle password visibility"""
        if self.show_password.isChecked():
            self.txtPass.setEchoMode(QLineEdit.Normal)
        else:
            self.txtPass.setEchoMode(QLineEdit.Password)
        
    def login(self):
        """Handles the login authentication process"""
        username = self.txtUser.text()
        password = self.txtPass.text()

        if not username or not password:
            QMessageBox.warning(self, "Message Prompt", "Please fill in both fields.")
            self.txtPass.clear()
            self.txtUser.clear()
            self.txtUser.setFocus()
            return

        con = db_connect()  # Connect to the database
        if con is None:
            return  # Stop execution if connection fails

        cursor = con.cursor()
        cursor.execute("SELECT * FROM tbllogin WHERE Username = %s AND Password = %s", (username, password))
        result = cursor.fetchone()
        con.close()

        if result:
            QMessageBox.information(self, "Login Security", f"ACCESS GRANTED: Hi {username}! Welcome to Student Management System Dashboard")
            self.close()  # Close the login form
            # Add code to open the main dashboard window
        else:
            QMessageBox.critical(self, "Login Security", "ACCESS DENIED: Incorrect Username or Password")
            self.txtPass.clear()
            self.txtUser.setFocus()
            self.cp += 1

            if self.cp >= 4:
                QMessageBox.critical(self, "Limit Reached", "Student Management System application will now close.")
                sys.exit()

    def exit_app(self):
        """Exit confirmation dialog"""
        reply = QMessageBox.question(self, "Logout", "Do you want to Exit?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            sys.exit()

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv) #Initializing the App
    window = frmLogin() # Create window object
    window.show() # Display window
    sys.exit(app.exec_()) # Start event loop
