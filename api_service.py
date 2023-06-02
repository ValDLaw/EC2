import requests

def getCoordinatesAPI(city,country):
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