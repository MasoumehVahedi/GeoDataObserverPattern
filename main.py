import sys

from geoData import GeoTask
from gui import GUI
from mapRender import MapRender
from QT_GUI import QT

from PyQt5.QtWidgets import QApplication


def main():
    app = QApplication(sys.argv)
    geo_task = GeoTask()

    # With GUI
    guiObj = GUI(geo_task)
    geo_task.attach(guiObj)

    # With QT
    maprender = MapRender(geo_task)
    geo_task.attach(maprender)

    qt_window = QT(geo_task, maprender)
    qt_window.window()
    sys.exit(app.exec_())



if __name__ == "__main__":
    main()


