import random
from geoData import GeoTask
from pattern import Observer


# Observer
class GUI(Observer):
    def __init__(self, geoDataObj: GeoTask):
        super().__init__()
        self.geoDataObj = geoDataObj

    def show(self):
        print("Point: {}".format(self.geoDataObj.getGeoData().Point))
        print("Line: {}".format(self.geoDataObj.getGeoData().Line))
        print("Area: {}".format(self.geoDataObj.getGeoData().Area))

    # When we call update, the observer notice that something has changed to POLL data from observable
    def updateData(self, status):
        self.show()



