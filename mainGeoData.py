import numpy as np
import random

from geoData import GeoTask
from pattern import Observable, Observer
from gui import GUI


def main():
    geo_task = GeoTask()
    guiObj = GUI(geo_task)
    observable = Observable()
    observable.add(guiObj)

    for i in range(100):
        # Set geo data and notify observers
        geo_task.generateGeoData()
        # Call update to trigger GUI to show the geo data
        observable.get_status("Updated GeoData")


if __name__ == "__main__":
    main()


