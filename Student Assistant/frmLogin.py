import sys  
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox
from PyQt5.QtCore import Qt, QFile, QTextStream, QSize
from PyQt5.QtGui import QPainter, QPixmap, QPalette, QColor, QIcon
from db_connection import db_connect  # Import the database connection function

class frmLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form") 
        self.setGeometry(500, 150, 885, 653)  # Size and coordinates
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove title bar
        self.cp = 0  # Counter for failed attempts

        # Username Input
        self.txtUser = QLineEdit(self)
        self.txtUser.setPlaceholderText("Username")
        self.txtUser.setFixedSize(330, 51)
        self.txtUser.move(500, 295)  

        # Password Input
        self.txtPass = QLineEdit(self)
        self.txtPass.setPlaceholderText("Password")
        self.txtPass.setFixedSize(330, 51)
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.txtPass.move(500, 372)  

        # Placeholder Text Color
        palette = self.txtUser.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 77))  # 30% opacity
        self.txtUser.setPalette(palette)
        self.txtPass.setPalette(palette)

        # Register Button
        self.btnRegister = QPushButton("REGISTER", self)
        self.btnRegister.setFixedSize(150, 37)
        self.btnRegister.move(510, 203)  
        self.btnRegister.setObjectName("btnRegister")  

        # Loging Button
        self.btnLoging = QPushButton("LOG IN", self)
        self.btnLoging.setFixedSize(150, 37)
        self.btnLoging.move(670, 203)  
        self.btnLoging.setObjectName("btnLoging")  

        # Ensure buttons are checkable
        self.btnLoging.setCheckable(True)
        self.btnRegister.setCheckable(True)

        self.btnLoging.clicked.connect(self.toggle_button_styles)
        self.btnRegister.clicked.connect(self.toggle_button_styles)

        # Login Button
        self.btnLogin = QPushButton("Login", self)
        self.btnLogin.setFixedSize(330, 43)
        self.btnLogin.move(500, 467)  
        self.btnLogin.setObjectName("btnLogin")  
        self.btnLogin.clicked.connect(self.login)

        # Gmail Button (Adjusted Position)
        self.btnGmail = QPushButton("Gmail", self)
        self.btnGmail.setFixedSize(160, 43)
        self.btnGmail.move(500, 575)  
        self.btnGmail.setObjectName("btnGmail") 
        self.btnGmail.clicked.connect(self.gmail)

        self.lblGmailIcon = QLabel(self)
        self.lblGmailIcon.setPixmap(QPixmap("gmail.png").scaled(21, 21))  
        self.lblGmailIcon.move(536, 585)  

        # Apple Button
        self.btnApple = QPushButton("Apple", self)
        self.btnApple.setFixedSize(160, 43)
        self.btnApple.move(674, 575)  
        self.btnApple.setObjectName("btnApple")  
        self.btnApple.clicked.connect(self.apple)

        self.lblAppleIcon = QLabel(self)
        self.lblAppleIcon.setPixmap(QPixmap("Apple.png").scaled(21, 21))  
        self.lblAppleIcon.move(713, 585)  

        # Exit Button
        self.btnClose = QPushButton("", self)
        self.btnClose.setFixedSize(43, 37)  
        self.btnClose.move(831, 13)  
        self.btnClose.setObjectName("btnClose")  
        self.btnClose.setIcon(QIcon("Close.png"))
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.clicked.connect(self.exit_app)

        # Load external QSS file
        self.load_stylesheet("Login.qss")  
        self.setStyleSheet("background-color: #2C2638;")

        # Set "LOG IN" as default selected button
        self.btnLoging.setChecked(True)
        self.toggle_button_styles()  # Apply styles on startup


    def toggle_button_styles(self):
        """ Ensure only one button remains in 'checked' state and updates styles properly. """
        sender = self.sender()
    
        if sender == self.btnLoging:
            self.btnLoging.setChecked(True)
            self.btnRegister.setChecked(False)
            self.txtUser.show()
            self.txtPass.show()
            self.btnLogin.show()
        elif sender == self.btnRegister:
            self.btnRegister.setChecked(True)
            self.btnLoging.setChecked(False)
            self.txtUser.hide()
            self.txtPass.hide()
            self.btnLogin.hide()

        # Explicitly update styles
        self.update_button_styles()

    def update_button_styles(self):
        """ Force UI to refresh styles so the checked button is properly displayed """
        self.btnLoging.style().unpolish(self.btnLoging)
        self.btnLoging.style().polish(self.btnLoging)
        self.btnRegister.style().unpolish(self.btnRegister)
        self.btnRegister.style().polish(self.btnRegister)

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
        pixmap = QPixmap("bgLogin.png")  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
            painter.setOpacity(1)
            painter.drawPixmap(self.rect(), scaled_pixmap)

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
            QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")
            return

        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM tbllogin WHERE Username = %s AND Password = %s", (username, password))
            result = cursor.fetchone()
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
            return
        finally:
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

    def gmail(self):
        """Handles Gmail login functionality"""
        QMessageBox.information(self, "Gmail Login", "Gmail login feature is under development, please check back later.")

    def apple(self):
        """Handles Apple login functionality"""
        QMessageBox.information(self, "Apple Login", "Apple login feature is under development, please check back later.")

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
