import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, QFile, QTextStream
from PyQt5.QtGui import QPainter, QPixmap, QPalette, QColor
from db_connection import db_connect  # Import the database connection function

class frmLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form") 
        self.setGeometry(700, 150, 885, 653)  # Size and coordinates
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # Remove title bar
        self.cp = 0  # Counter for failed attempts

        # UsernameInput
        self.txtUser = QLineEdit(self)
        self.txtUser.setPlaceholderText("Username")
        self.txtUser.setFixedSize(330, 51)
        self.txtUser.move(500, 295)  # Adjust X and Y position
        
        # Password Input
        self.txtPass = QLineEdit(self)
        self.txtPass.setPlaceholderText("Password")
        self.txtPass.setFixedSize(330, 51)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.txtPass.move(500, 372)  # Adjust X and Y position

        palette = self.txtUser.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 77))  # 30% opacity
        self.txtUser.setPalette(palette)
        self.txtPass.setPalette(palette)
            
        # Login Button
        self.btnLogin = QPushButton("Login", self)
        self.btnLogin.setFixedSize(330, 43)
        self.btnLogin.move(500, 467)  # Adjust position
        self.btnLogin.setObjectName("btnLogin")  # Assign a unique ID
        self.btnLogin.clicked.connect(self.login)
        
        # Exit Button
        self.btnClose = QPushButton("X", self)
        self.btnClose.setFixedSize(43, 37)  # Ensure consistency in size
        self.btnClose.move(831, 13)  # Adjust position
        self.btnClose.setObjectName("btnClose")  # Assign a unique ID
        self.btnClose.clicked.connect(self.exit_app)

        
        # Load external QSS file
        self.load_stylesheet("Login.qss")  # Ensure the stylesheet applies
        self.setStyleSheet("background-color: #2C2638;")

    def load_stylesheet(self, file_name):
        """Loads and applies an external QSS file."""
        file = QFile(file_name)
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            qss = stream.readAll()
            self.setStyleSheet(qss)
            file.close()
        else:
            print("Failed to load QSS file")

    def paintEvent(self, event):
        """Set a single, properly scaled background image."""
        painter = QPainter(self)
        pixmap = QPixmap("bgLogin.png")  # Ensure file exists
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            painter.setOpacity(1)
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
        con = db_connect()
        if con is None:
            return

        cursor = con.cursor()
        cursor.execute("SELECT * FROM tbllogin WHERE Username = %s AND Password = %s", (username, password))
        result = cursor.fetchone()
        con.close()

        if result:
            QMessageBox.information(self, "Login Security", f"ACCESS GRANTED: Hi {username}! Welcome to Student Assistant System")
            self.close()
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmLogin()
    window.show()
    sys.exit(app.exec_())
