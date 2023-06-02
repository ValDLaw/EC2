import csv

archivo_csv = 'worldcities.csv'

Cities = {}
with open(archivo_csv, "r", encoding="utf-8") as archivo :
    ar = csv.reader(archivo) 
    next(ar, None)
    for linea in ar :
        city = linea[0]
        lat = float(linea[2])
        lng = float(linea[3])
        country = linea[4]

        Cities[(city.lower(),country.lower())] = [lat, lng] 

def getCoordinatesCSV(city, country):
    return Cities.get((city.lower(), country.lower()), "No existe") 