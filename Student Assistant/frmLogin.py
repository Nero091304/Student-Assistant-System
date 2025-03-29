import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QVBoxLayout
from PyQt5.QtCore import QFile, QTextStream, Qt
from PyQt5.QtGui import QPainter, QPixmap, QPalette, QColor

from db_connection import db_connect  # Import the database connection function

class frmLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form") 
        self.setGeometry(700, 150, 885, 653)  # Size and coordinates
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove title bar
        self.cp = 0  # Counter for failed attempts

        layout = QVBoxLayout()
        
        # Username Label and Input
        self.txtUser = QLineEdit()
        self.txtUser.setPlaceholderText("Username")
        self.txtUser.setFixedSize(330, 51)
        layout.addWidget(self.txtUser)
        
        # Password Label and Input
        self.txtPass = QLineEdit()
        self.txtPass.setPlaceholderText("Password")
        self.txtPass.setFixedSize(330, 51)
        self.txtPass.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.txtPass)

        palette = self.txtUser.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 128))  # White with 50% opacity
        self.txtUser.setPalette(palette)
        self.txtPass.setPalette(palette)
        
        # Show Password Checkbox
        self.show_password = QCheckBox("Show Password")
        self.show_password.stateChanged.connect(self.toggle_password)
        layout.addWidget(self.show_password)
        
        # Login Button
        self.btnLogin = QPushButton("Login")
        self.btnLogin.setFixedSize(330, 43)
        self.btnLogin.clicked.connect(self.login)
        layout.addWidget(self.btnLogin)

        # Exit Button
        self.btnClose = QPushButton("Exit")
        self.btnClose.clicked.connect(self.exit_app)
        layout.addWidget(self.btnClose)
        
        self.setLayout(layout)

        # Load external QSS file
        self.load_stylesheet("Login.qss")
        self.setStyleSheet("background-color: #2C2638;")

    def load_stylesheet(self, file_name):
        """Loads and applies an external QSS file."""
        file = QFile(file_name)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            qss = stream.readAll()
            self.setStyleSheet(qss)
            file.close()

    def paintEvent(self, event):
        """Set a single, properly scaled background image with opacity."""
        painter = QPainter(self)
        pixmap = QPixmap("bgLogin.png")  # Ensure file exists
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.setOpacity(1)  # 3% opacity
            painter.drawPixmap(self.rect(), scaled_pixmap)

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

        # DATABASE CONNECTION ==================================================
        con = db_connect()  # Connect to the database
        if con is None:
            return  # Stop execution if connection fails

        cursor = con.cursor()
        cursor.execute("SELECT * FROM tbllogin WHERE Username = %s AND Password = %s", (username, password))
        result = cursor.fetchone()
        con.close()

        if result:
            QMessageBox.information(self, "Login Security", f"ACCESS GRANTED: Hi {username}! Welcome to Student Assistant System")
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
    app = QApplication(sys.argv)  # Initializing the App
    window = frmLogin()  # Create window object
    window.show()  # Display window
    sys.exit(app.exec_())  # Start event loop
