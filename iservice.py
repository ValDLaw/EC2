from math import radians, cos, sin, asin, sqrt
from mock_service import getCoordinatesMock
from csv_service import getCoordinatesCSV
from api_service import getCoordinatesAPI

class InterfaceService:
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
        if (forma == "csv"):
            return getCoordinatesCSV(ciudad,pais)
        elif (forma == "api"):
            return getCoordinatesAPI(ciudad,pais)
        elif (forma == "mock"):
            return getCoordinatesMock()
        else:
            return