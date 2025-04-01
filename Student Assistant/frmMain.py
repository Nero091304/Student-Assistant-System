import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import Qt

class frmMain(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Dashboard") 
        self.setGeometry(500, 150, 885, 653)  # Set size and position
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # Remove title bar
        
        # Add a welcome label
        self.label = QLabel("Welcome to the Student Assistant System!", self)
        self.label.move(250, 250)
        self.label.setFixedSize(400, 30)
        
        # Add a close button
        self.btnClose = QPushButton("Close", self)
        self.btnClose.setFixedSize(100, 40)
        self.btnClose.move(390, 400)
        self.btnClose.clicked.connect(self.close)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = frmMain()
    window.show()
    sys.exit(app.exec_())