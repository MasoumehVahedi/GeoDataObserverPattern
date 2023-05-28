import numpy as np
import random
import sys

from geoData import GeoTask
from pattern import Observable, Observer
from gui import GUI



def main():
    geo_task = GeoTask()
    guiObj = GUI(geo_task)
    geo_task.attach(guiObj)

    for i in range(100):
        # Set geo data and notify observers
        geo_task.generateGeoData()


if __name__ == "__main__":
    main()


