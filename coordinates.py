import requests
import csv

class getCoordinates:

    def __init__(self):
        archivo_csv = 'worldcities.csv'

        self.Cities = {}
        with open(archivo_csv, "r", encoding="utf-8") as archivo :
            ar = csv.reader(archivo) 
            next(ar, None)
            for linea in ar :
                city = linea[0]
                lat = float(linea[2])
                lng = float(linea[3])
                country = linea[4]

                self.Cities[(city.lower(),country.lower())] = [lat, lng] 

    def CSV(self,city, country):
        return self.Cities.get((city.lower(), country.lower()), "No existe") 

    def API(self,city,country):
        url = f"https://nominatim.openstreetmap.org/search?q={city},{country}&format=json"
        
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()[0]
            lat = float(data["lat"])
            lon = float(data["lon"])
            return [lat,lon]
        else:
            print('Error en la solicitud:', response.status_code)
            return

    def Mock(self):
        return [0,0]