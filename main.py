from factory import Factory 
from calculate import Calculate
import random

ciudad1 = input("Ingrese el nombre de la primera ciudad: ")
pais1 = input("Ingrese el nombre del país al que pertenece: ")
ciudad2 = input("Ingrese el nombre de la segunda ciudad: ")
pais2 = input("Ingrese el nombre del país al que pertenece: ")

opcion = Factory.obtener_servicio(random.randint(0,2))

print(opcion)

lat_lon1 = Calculate.getlatlon(ciudad1,pais1,opcion)
lat_lon2 = Calculate.getlatlon(ciudad2,pais2,opcion)

lat_long_dist = Calculate.haversine(lat_lon1[0], lat_lon1[1], lat_lon2[0], lat_lon2[1])
print(lat_long_dist)