import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox, QGraphicsOpacityEffect
from PyQt5.QtCore import Qt, QFile, QTextStream, QSize, QTimer, QPropertyAnimation, QPoint, QEasingCurve
from PyQt5.QtGui import QPainter, QPixmap, QPalette, QColor, QIcon
from db_connection import db_connect  # Import the database connection function
from frmMain import frmMain # openfrmMain 

class frmLogin(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500, 150, 885, 653)  # Size and coordinates
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove title bar
        self.cp = 0  # Counter for failed attempts

        # Image Slideshow (Placed on the Left Side)
        self.lblImage = QLabel(self)
        self.lblImage.setFixedSize(460, 653)  # Match left section size
        self.lblImage.move(0, 0)  # Align to the left
        self.lblImage.setObjectName("lblImage")
        self.lblImage.setScaledContents(True)

        # Second QLabel for smooth transition effect
        self.lblNextImage = QLabel(self)
        self.lblNextImage.setFixedSize(460, 653)
        self.lblNextImage.move(0, 0)  # Start off-screen
        self.lblNextImage.setScaledContents(True)
        self.lblNextImage.hide()

        # List of images for slideshow
        self.image_index = 0
        self.image_list = ["img1.png", "img2.png", "img3.png"]

        # Timer to change images
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_image)
        self.timer.start(4000)  # Change image every 4 seconds

        # Show the first image immediately
        self.update_image()

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

        # Create Username Input
        self.txtNewUser = QLineEdit(self)
        self.txtNewUser.setPlaceholderText("Create Username")
        self.txtNewUser.setFixedSize(330, 51)
        self.txtNewUser.move(501, 271)

        # Create Password Input
        self.txtNewPass = QLineEdit(self)
        self.txtNewPass.setPlaceholderText("Create Password")
        self.txtNewPass.setFixedSize(330, 51)
        self.txtNewPass.setEchoMode(QLineEdit.Password)
        self.txtNewPass.move(501, 334)

        # Create Confirm Password Input
        self.txtConfirmPass = QLineEdit(self)
        self.txtConfirmPass.setPlaceholderText("Confirm Password")
        self.txtConfirmPass.setFixedSize(330, 51)
        self.txtConfirmPass.setEchoMode(QLineEdit.Password)
        self.txtConfirmPass.move(501, 397)
        
        # Login Button
        self.btnLogin = QPushButton("Login", self)
        self.btnLogin.setFixedSize(330, 43)
        self.btnLogin.move(500, 467)  
        self.btnLogin.setObjectName("btnLogin")  
        self.btnLogin.clicked.connect(self.login)

        self.btnCreate = QPushButton("Create Account", self)
        self.btnCreate.setFixedSize(330, 43)
        self.btnCreate.move(500, 467) 
        self.btnCreate.setObjectName("btnCreate")

        #Hide Create User Inputs
        self.txtNewUser.hide()
        self.txtNewPass.hide()
        self.txtConfirmPass.hide()
        self.btnCreate.hide()

        # Placeholder Text Color
        palette = self.txtUser.palette()
        palette.setColor(QPalette.PlaceholderText, QColor(255, 255, 255, 77))  # 30% opacity
        self.txtUser.setPalette(palette)
        self.txtPass.setPalette(palette)
        self.txtNewUser.setPalette(palette)
        self.txtNewPass.setPalette(palette)
        self.txtConfirmPass.setPalette(palette)

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
           
        # Show Password Buttons
        self.btnShowPassword = QPushButton("", self)
        self.btnShowPassword.setFixedSize(35, 35)
        self.btnShowPassword.move(777, 381)  
        self.btnShowPassword.setObjectName("btnShow")  
        self.btnShowPassword.setIcon(QIcon("eye.png"))
        self.btnShowPassword.setIconSize(QSize(35, 35))
        self.btnShowPassword.clicked.connect(lambda: self.toggle_password_visibility(self.txtPass))

        self.btnShowNewPassword = QPushButton("", self)
        self.btnShowNewPassword.setFixedSize(35, 35)
        self.btnShowNewPassword.move(777, 342)  
        self.btnShowNewPassword.setObjectName("btnShow")  
        self.btnShowNewPassword.setIcon(QIcon("eye.png"))
        self.btnShowNewPassword.setIconSize(QSize(35, 35))
        self.btnShowNewPassword.clicked.connect(lambda: self.toggle_password_visibility(self.txtNewPass))

        self.btnShowConfirmPassword = QPushButton("", self)
        self.btnShowConfirmPassword.setFixedSize(35, 35)
        self.btnShowConfirmPassword.move(777, 405)  
        self.btnShowConfirmPassword.setObjectName("btnShow")  
        self.btnShowConfirmPassword.setIcon(QIcon("eye.png"))
        self.btnShowConfirmPassword.setIconSize(QSize(35, 35))
        self.btnShowConfirmPassword.clicked.connect(lambda: self.toggle_password_visibility(self.txtConfirmPass))

        # Hide Show Password Buttons
        self.btnShowNewPassword.hide()
        self.btnShowConfirmPassword.hide()

        # Load external QSS file
        self.load_stylesheet("Login.qss")  
        self.setStyleSheet("background-color: #2C2638;")

        # Set "LOG IN" as default selected button
        self.btnLoging.setChecked(True)
        self.toggle_button_styles()  # Apply styles on startup

        
        # Connect the create account button to the function
        self.btnCreate.clicked.connect(self.create_account)

    def keyPressEvent(self, event):
        """Handles key press events for Enter key navigation."""
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):  # Check if Enter is pressed
            if self.txtUser.hasFocus():
                self.txtPass.setFocus()  # Move to password field
            elif self.txtPass.hasFocus():
                self.login()  # Attempt login if Enter is pressed in password field
        else:
            super().keyPressEvent(event)  # Default event handling

    def keyPressEvent(self, event):
        """Handles key press events for Enter key navigation."""
        if event.key() in (Qt.Key_Return, Qt.Key_Enter):  # Check if Enter is pressed
            if self.txtNewUser.hasFocus():
                self.txtNewPass.setFocus()  
            elif self.txtNewPass.hasFocus():
                self.txtConfirmPass.setFocus()  
            elif self.txtConfirmPass.hasFocus():
                self.create_account()
        else:
            super().keyPressEvent(event)  # Default event handling


    def toggle_button_styles(self):
        """ Ensure only one button remains in 'checked' state and updates styles properly. """
        sender = self.sender()
    
        if sender == self.btnLoging:
            self.btnLoging.setChecked(True)
            self.btnRegister.setChecked(False)
            self.txtUser.show()
            self.txtPass.show()
            self.btnLogin.show()
            self.btnShowPassword.show()
            self.txtNewUser.hide()
            self.txtNewPass.hide()
            self.txtConfirmPass.hide()
            self.btnCreate.hide()
            self.btnShowNewPassword.hide()
            self.btnShowConfirmPassword.hide()
        elif sender == self.btnRegister:
            self.btnRegister.setChecked(True)
            self.btnLoging.setChecked(False)
            self.txtUser.hide()
            self.txtPass.hide()
            self.btnLogin.hide()
            self.btnShowPassword.hide()
            self.txtNewUser.show()
            self.txtNewPass.show()
            self.txtConfirmPass.show()
            self.btnCreate.show()
            self.btnShowNewPassword.show()
            self.btnShowConfirmPassword.show()

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

        # DATABASE CONNECTION LOGIN ==================================================
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
            self.main_window = frmMain()  # Create an instance of the main form
            self.main_window.show()  # Show the main form
            self.close()  # Close the login form
        else:
            QMessageBox.critical(self, "Login Security", "ACCESS DENIED: Incorrect Username or Password")
            self.txtPass.clear()
            self.txtUser.setFocus()
            self.cp += 1

            if self.cp >= 4:
                QMessageBox.critical(self, "Limit Reached", "Student Management System application will now close.")
                sys.exit()

    # DATABASE CONNECTION Create ==================================================
    def create_account(self):
        """Handles the creation of a new user account."""
        new_username = self.txtNewUser.text().strip()
        new_password = self.txtNewPass.text().strip()
        confirm_password = self.txtConfirmPass.text().strip()
    
        if not new_username or not new_password or not confirm_password:
            QMessageBox.warning(self, "Message Prompt", "Please fill in all fields.")
            self.txtNewUser.setFocus()
            return
    
        if new_password != confirm_password:
            QMessageBox.warning(self, "Message Prompt", "Passwords do not match.")
            return
    
        con = db_connect()
        if con is None:
            QMessageBox.critical(self, "Database Error", "Failed to connect to the database.")
            return
    
        try:
            cursor = con.cursor()
            cursor.execute("SELECT * FROM tbllogin WHERE Username = %s", (new_username,))
            existing_user = cursor.fetchone()
    
            if existing_user:
                QMessageBox.warning(self, "Message Prompt", "Username already exists. Please choose another.")
                return
    
            cursor.execute("INSERT INTO tbllogin (Username, Password) VALUES (%s, %s)", (new_username, new_password))
            con.commit()
    
            QMessageBox.information(self, "Account Created", "Your account has been successfully created!")
    
            self.txtNewUser.clear()
            self.txtNewPass.clear()
            self.txtConfirmPass.clear()
            self.btnLoging.click()  # Switch back to login form
    
        except Exception as e:
            QMessageBox.critical(self, "Database Error", f"An error occurred: {e}")
        finally:
            con.close()
   
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

    def toggle_password_visibility(self, field):
        """Toggles the visibility of a given password field."""
        if field.echoMode() == QLineEdit.Password:
            field.setEchoMode(QLineEdit.Normal)  # Show password
        else:
            field.setEchoMode(QLineEdit.Password)  # Hide password

    def update_image(self):
        """Smooth transition: Current image moves left, new image enters from right."""

        # Determine the next image index
        next_index = (self.image_index + 1) % len(self.image_list)

        # Load the next image into lblNextImage (Hidden initially)
        self.lblNextImage.setPixmap(QPixmap(self.image_list[next_index]))
        self.lblNextImage.move(0, 0)  # Position off-screen (right) using -460
        self.lblNextImage.show()

        # Animate the current image to move left (out of frame)
        self.animation_out = QPropertyAnimation(self.lblImage, b"pos")
        self.animation_out.setDuration(1000)  # 1-second transition
        self.animation_out.setStartValue(QPoint(0, 0))
        self.animation_out.setEndValue(QPoint(-self.lblImage.width(), 0))  # Move left
        self.animation_out.setEasingCurve(QEasingCurve.OutCubic)

        # Animate the next image to move into place from the right
        self.animation_in = QPropertyAnimation(self.lblNextImage, b"pos")
        self.animation_in.setDuration(1000)
        self.animation_in.setStartValue(QPoint(0, 0))  # Start off-screen (right) using -460
        self.animation_in.setEndValue(QPoint(0, 0))  # Move to position
        self.animation_in.setEasingCurve(QEasingCurve.OutCubic)

        # After the animation, swap images
        def swap_images():
            self.lblImage.setPixmap(QPixmap(self.image_list[next_index]))  # Set new image
            self.lblImage.move(0, 0)  # Reset position
            self.lblNextImage.hide()  # Hide extra QLabel
            self.image_index = next_index  # Update index

        # Connect animation finish to swapping images
        self.animation_in.finished.connect(swap_images)

        # Start animations
        self.animation_out.start()
        self.animation_in.start()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmLogin()
    window.show()
    sys.exit(app.exec_())
