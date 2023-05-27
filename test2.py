import urllib.parse
import requests

def calculo_de_distancia (inicio, destino):
	url = f'https://www.mapquestapi.com/directions/v2/route?key=PDtdUnRijjx1JF5MC6lKyLdBrfqoB4qC&from={inicio}&to={destino}'
	response = requests.get(url)
	data = response.json()
	distancia = data['route']['distance']
	return distancia

def calculo_de_duracion (inicio, destino):
	url = f'https://www.mapquestapi.com/directions/v2/route?key=PDtdUnRijjx1JF5MC6lKyLdBrfqoB4qC&from={inicio}&to={destino}'
	response = requests.get(url)
	data = response.json()
	distancia = data['route']['distance']
	return distancia

def calculo_de_combustible (distancia):
	litros_por_km = 0.12
	combustible = distancia * litros_por_km
	return combustible

def narrativa (inicio, destino, distancia, duracion, combustible):
	print (f"Viaje de {inicio} a {destino}:")
	print (f"Distancia: {distancia:.2f} km")
	print (f"Duracion: {duracion}")
	print (f"Combustible requerido: {combustible:.2f} litros")

inicio = input("Ciudad de Origen: ")
destino = input("Ciudad de Destino: ")

distancia = calculo_de_distancia (inicio, destino)
duracion = calculo_de_duracion (inicio, destino)
combustible = calculo_de_combustible (distancia)

narrativa (inicio, destino, distancia, duracion, combustible)

print ("==================================================================================")
print ("Su viaje desde la Ciudad de " + str(inicio), "hasta la ciudad de " + str(destino))
print ("tiene una distancia de " + str(distancia), "kilómetros", "y su viaje tiene una duración de " + str(duracion), "Horas")
print ("y va a consumir " + str(combustible), "Litros de combustible")
print ("==================================================================================")

