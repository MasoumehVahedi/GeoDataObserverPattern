import numpy as np
from pattern import Observable



# Create the geo_data types
class GeoData:
    class Point:
        def __init__(self, point: int):
            self.point = point

    class Line:
        def __init__(self, line: int):
            self.line = line

    class Area:
        def __init__(self, area: int):
            self.area = area


# Generate and get the geo_data types.
# This is our observable
class GeoTask(Observable):
    def __init__(self):
        super(GeoTask, self).__init__()
        self.geoData = GeoData()

    # This is interface
    def getGeoData(self):
        return self.geoData

    def generateGeoData(self):
        # Updating geoData
        self.geoData.Point = np.random.randint(low=1, high=100)
        self.geoData.Line = np.random.randint(low=1, high=100)
        self.geoData.Area = np.random.randint(low=1, high=100)


