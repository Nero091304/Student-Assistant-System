import mysql.connector
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QTableView, QHeaderView,  QDateEdit, QMessageBox, QAbstractItemView, QGraphicsOpacityEffect
from PyQt5.QtGui import QPainter, QPixmap, QIcon,  QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QSize, QDate
from frmExport import frmRealisticPaper

class frmAboutHistory(QWidget):
    def __init__(self, username):
        super().__init__()
        self.setFixedSize(1920, 1020)  
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.username = username

        self.btnClose = QPushButton(self)
        self.btnClose.setFixedSize(43, 37)
        self.btnClose.move(1868, 9)
        self.btnClose.setIcon(QIcon("Close.png"))  
        self.btnClose.setIconSize(QSize(28, 28))
        self.btnClose.setObjectName("btnClose")
        self.btnClose.clicked.connect(self.exit_app)

        self.btnExport = QPushButton("Export", self)
        self.btnExport.setFixedSize(377, 60)
        self.btnExport.move(136, 881)
        self.btnExport.setObjectName("btnExport")
        self.set_button_enabled(self.btnExport, False)

        self.btnView = QPushButton("View Result", self)
        self.btnView.setFixedSize(377, 60)
        self.btnView.move(136, 801)
        self.btnView.setObjectName("btnView")
        self.btnView.clicked.connect(self.View_Result)
        self.set_button_enabled(self.btnView, False)

        self.txtSearch = QLineEdit(self)
        self.txtSearch.setFixedSize(495, 60)
        self.txtSearch.move(770, 76)
        self.txtSearch.setObjectName("txtSearch")
        self.txtSearch.setPlaceholderText("Search by Personality Type...")
        self.txtSearch.setStyleSheet("QLineEdit { font-size: 18px; }")
        self.txtSearch.textChanged.connect(self.filter_by_personality)

        self.btnRefresh = QPushButton(self)
        self.btnRefresh.setFixedSize(70, 70)
        self.btnRefresh.move(1772, 70)
        self.btnRefresh.setIcon(QIcon("Refresh.png"))  
        self.btnRefresh.setIconSize(QSize(50, 50))
        self.btnRefresh.setObjectName("btnRefresh")
        self.btnRefresh.clicked.connect(self.reset_filters)

        self.datePicker = QDateEdit(self)
        self.datePicker.setCalendarPopup(True)  
        self.datePicker.setDisplayFormat("MMMM dd, yyyy")  
        self.datePicker.setFixedSize(257, 60)
        self.datePicker.move(1317, 76)  
        self.datePicker.setObjectName("datePicker")
        self.datePicker.setDate(QDate.currentDate())  
        self.datePicker.dateChanged.connect(self.filter_by_date)

        self.tableView = QTableView(self)
        self.tableView.setFixedSize(1220, 775)
        self.tableView.move(628, 166)
        self.tableView.setObjectName("tableView")

        self.model = QStandardItemModel(100, 6, self)  
        self.model.setHorizontalHeaderLabels(["Date Taken",
                                              "Personality Type",
                                              "Realistic Score", 
                                              "Investigative Score",
                                              "Artistic Score",
                                              "Social Score",
                                              "Enterprising Score",
                                              "Conventional Score",])
        self.tableView.setModel(self.model)
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableView.selectionModel().selectionChanged.connect(self.on_row_selected)

        self.btnView.setEnabled(False)

        header = self.tableView.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.load_stylesheet("History.qss")

        self.fetch_data_from_db()

    def exit_app(self):
        self.close()

    def filter_by_date(self, selected_date):
        formatted_date = selected_date.toString("MMMM d, yyyy")  

        for row in range(self.model.rowCount()):
            item = self.model.item(row, 0) 
            is_visible = item.text() == formatted_date
            self.tableView.setRowHidden(row, not is_visible)

    def filter_by_personality(self, text):
        search_text = text.strip().lower()

        for row in range(self.model.rowCount()):
            item = self.model.item(row, 1)
            personality = item.text().lower() if item else ""

            is_visible = search_text in personality
            self.tableView.setRowHidden(row, not is_visible)

    def reset_filters(self):
        self.txtSearch.clear()  
        self.datePicker.setDate(QDate.currentDate()) 

        for row in range(self.model.rowCount()):
            self.tableView.setRowHidden(row, False)

    def View_Result(self):
        selected_indexes = self.tableView.selectionModel().selectedRows()
        if selected_indexes:
            selected_row = selected_indexes[0].row()
            date_value = self.model.item(selected_row, 0).text()
            personality_value = self.model.item(selected_row, 1).text()

            row_has_data = False
            for col in range(self.model.columnCount()):
                item = self.model.item(selected_row, col)
                if item and item.text().strip() != "":  
                    row_has_data = True
                    break  

            if not row_has_data:
                QMessageBox.information(self, "No Data", "There is no output here.")
                return  

            date_value = self.model.item(selected_row, 0).text()
            personality_value = self.model.item(selected_row, 1).text()

            self.set_button_enabled(self.btnExport, True)

        personality_column_map = {
            "REALISTIC": 2,   
            "INVESTIGATIVE": 3,  
            "ARTISTIC": 4,   
            "SOCIAL": 5,    
            "ENTERPRISING": 6,  
            "CONVENTIONAL": 7  
        }

        score_column = personality_column_map.get(personality_value, None)
        raw_score = int(self.model.item(selected_row, score_column).text()) if score_column is not None else 0
        score_value = f"{(raw_score / 7) * 100:.2f}%" if score_column is not None else "N/A"

        # Gather all scores
        all_scores = {
            "R": int(self.model.item(selected_row, 2).text()),
            "I": int(self.model.item(selected_row, 3).text()),
            "A": int(self.model.item(selected_row, 4).text()),
            "S": int(self.model.item(selected_row, 5).text()),
            "E": int(self.model.item(selected_row, 6).text()),
            "C": int(self.model.item(selected_row, 7).text())
        }

        self.Courses_form = frmRealisticPaper(self.username, date_value, personality_value, score_value, all_scores)
        self.Courses_form.show()

        self.btnExport.clicked.connect(self.Courses_form.export_to_png)

    def on_row_selected(self, selected, deselected):
        has_selection = self.tableView.selectionModel().hasSelection()
        self.set_button_enabled(self.btnView, has_selection)
        self.set_button_enabled(self.btnExport, False)
  
    def set_button_enabled(self, button, enabled):
        button.setEnabled(enabled)
        opacity = 1.0 if enabled else 0.5
        effect = QGraphicsOpacityEffect()
        effect.setOpacity(opacity)
        button.setGraphicsEffect(effect)

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

    def mouseDoubleClickEvent(self, event):
        event.ignore()

    def fetch_data_from_db(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",    
                user="root",         
                password="",        
                database="sasdb"  
            )
            cursor = conn.cursor()

            cursor.execute("SELECT Date, Personality, RScore, IScore, AScore, SScore, EScore, CScore FROM tblhistory")
            rows = cursor.fetchall()

            self.model.removeRows(0, self.model.rowCount())

        
            total_rows = 100  # Set the number of rows you want
            total_columns = self.model.columnCount()  # Get the number of columns from the model

# Create blank rows for the table
            for i in range(total_rows):
                row_items = []
                for j in range(total_columns):
                    item = QStandardItem("")  # Blank cell
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Disable editing
                    item.setTextAlignment(Qt.AlignCenter)  # Center the text
                    row_items.append(item)
                self.model.appendRow(row_items)

# Now, populate the table with real data if available
            for i, row in enumerate(rows):
                if i >= total_rows:
                    break  # Avoid exceeding the row limit
                row = list(row)
                row[1] = row[1].upper()  # Uppercase Personality

    # Create the row items for real data
                row_items = [QStandardItem(str(value)) for value in row]
                for item in row_items:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Disable editing
                    item.setTextAlignment(Qt.AlignCenter)  # Center the text
                self.model.removeRow(i)  # Remove the empty row
                self.model.insertRow(i, row_items)  # Insert the row with data

                cursor.close()
                conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Error: {err}")



if __name__ == "__main__":
    app = QApplication([])
    window = frmAboutHistory()
    window.show()
    app.exec_()
