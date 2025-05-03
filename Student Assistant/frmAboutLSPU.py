from PyQt5.QtWidgets import QApplication, QWidget, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import Qt

class frmAboutLSPU(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("LSPUHOME.png") 
        if not pixmap.isNull():
            
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)

        super().paintEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutLSPU()
    window.show()
    app.exec_()
