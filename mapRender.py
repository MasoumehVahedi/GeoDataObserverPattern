# map_render = visualization

import numpy as np
from pattern import Observer, Observable
from geoData import GeoTask

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import sys


class MapRender(QWidget, Observer):
    def __init__(self, geoDataObj: GeoTask):
        super(MapRender, self).__init__()
        self.geoDataObj = geoDataObj
        self.initUI()

    def initUI(self):
        # Create QLabel widgets to display the geoData values
        self.pointLabel = QLabel(self)  # self is our actual object that is QMainWindow
        self.lineLabel = QLabel(self)
        self.areaLabel = QLabel(self)

        # Create a QVBoxLayout to arrange the QLabel widgets
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Geo Data: "))
        layout.addWidget(self.pointLabel)
        layout.addWidget(self.lineLabel)
        layout.addWidget(self.areaLabel)
        # Set the layout
        self.setLayout(layout)

    def show(self):
        self.pointLabel.setText("Point: {}".format(self.geoDataObj.getGeoData().Point))
        self.lineLabel.setText("Line: {}".format(self.geoDataObj.getGeoData().Line))
        self.areaLabel.setText("Area: {}".format(self.geoDataObj.getGeoData().Area))

    def updateData(self, status):
        self.show()






