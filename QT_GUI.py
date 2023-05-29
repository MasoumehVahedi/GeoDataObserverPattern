import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow


class QT(QMainWindow):
    def __init__(self, geo_task, maprender):
        super().__init__()
        self.geo_task = geo_task
        self.maprender = maprender

    def window(self):
        self.setCentralWidget(self.maprender)
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Geo Data")

        # Set up a QTimer to periodically update the geoData and trigger the display
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.updateGeoData())
        self.timer.start(1000)  # Update every 1 second

        self.show()

    def updateGeoData(self):
        for i in range(100):
            # Set geo data and notify observers
            self.geo_task.generateGeoData()


