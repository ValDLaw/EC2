from math import radians, cos, sin, asin, sqrt
from coordinates import getCoordinates

class Calculate:
    def haversine(lat1, lon1, lat2, lon2):
        lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

        # haversine 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * asin(sqrt(a)) 
        r = 6371 #radio de la tierra (km)
        return c * r

    def getlatlon(ciudad, pais, forma):
        coordinates = getCoordinates()
        if (forma == "csv"):
            return coordinates.CSV(ciudad,pais)
        elif (forma == "api"):
            return coordinates.API(ciudad,pais)
        elif (forma == "mock"):
            return coordinates.Mock()
        else:
            return