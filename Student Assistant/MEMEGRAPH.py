import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtChart import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis
from PyQt5.QtGui import QPainter
from PyQt5.QtCore import Qt

class BarChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Personality Score Chart")
        self.setGeometry(100, 100, 800, 600)

        # Sample data
        personalities = ["INTJ", "ENFP", "ISTP", "INFJ"]
        scores = [38, 40, 36, 34]

        # Create bar set and add scores
        bar_set = QBarSet("Score")
        bar_set.append(scores)

        # Create series and add bar set
        series = QBarSeries()
        series.append(bar_set)

        # Create chart and add series
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Scores by Personality Type")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Add X-axis categories
        axis_x = QBarCategoryAxis()
        axis_x.append(personalities)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        # Add Y-axis (optional: let it auto-scale)
        chart.createDefaultAxes()

        # Create chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChartWindow()
    window.show()
    sys.exit(app.exec_())

