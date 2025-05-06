from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableView, QHeaderView,  QDateEdit
from PyQt5.QtGui import QPainter, QPixmap, QIcon,  QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSize

class frmAboutHistory(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1868, 9)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        self.btnExport = QPushButton("Export", self)
        self.btnExport.setFixedSize(377, 70)
        self.btnExport.move(136, 841)
        self.btnExport.setObjectName("btnExport")

        self.txtSearch = QLineEdit(self)
        self.txtSearch.setFixedSize(495, 60)
        self.txtSearch.move(770, 76)
        self.txtSearch.setObjectName("txtSearch")

        self.btnRefresh = QPushButton(self)
        self.btnRefresh.setFixedSize(70, 70)
        self.btnRefresh.move(1772, 72)
        self.btnRefresh.setIcon(QIcon("Refresh.png"))  
        self.btnRefresh.setIconSize(QSize(50, 50))
        self.btnRefresh.setObjectName("btnRefresh")

        self.datePicker = QDateEdit(self)
        self.datePicker.setCalendarPopup(True)  
        self.datePicker.setDisplayFormat("MMMM dd, yyyy")  
        self.datePicker.setFixedSize(257, 60)
        self.datePicker.move(1317, 76)  
        self.datePicker.setObjectName("datePicker")

        self.tableView = QTableView(self)
        self.tableView.setFixedSize(1210, 775)
        self.tableView.move(628, 166)
        self.tableView.setObjectName("tableView")

        # Create and set model
        self.model = QStandardItemModel(100, 4, self)  # 0 rows, 4 columns
        self.model.setHorizontalHeaderLabels(["Date Taken", "Personality Type", "Score", "Remarks"])
        self.tableView.setModel(self.model)

        # Optional: Stretch columns to fit width
        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.load_stylesheet("History.qss")

    def exit_app(self):
        self.close()

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap = QPixmap("AboutHistory.png")  
        if not pixmap.isNull():
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            x = (self.width() - scaled_pixmap.width()) // 2
            y = (self.height() - scaled_pixmap.height()) // 2
            painter.drawPixmap(x, y, scaled_pixmap)

        super().paintEvent(event)

    def load_stylesheet(self, file_path):
        try:
            with open(file_path, "r") as f:
                self.setStyleSheet(f.read())
        except FileNotFoundError:
            print(f"Stylesheet file '{file_path}' not found.")

if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutHistory()
    window.show()
    app.exec_()
