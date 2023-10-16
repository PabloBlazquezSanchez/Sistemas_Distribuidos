"""
Entrega 4: ejercicio 16
Programa realizado por Pablo Blázquez Sánchez
Este programa te muestra quién está en la Estación Espacial Internacional
(International Space Station, ISS) y luego te muestra un mapa del mundo con
la posición de la ISS.
"""
import urllib.request
import json
import turtle
url = "http://api.open-notify.org/astros.json"
answer = urllib.request.urlopen(url)
result = json.loads(answer.read())
print("Personas en el espacio", result["number"])
personas = result["people"]
for p in personas:
    print(p["name"],"en",p["craft"])
url = "http://api.open-notify.org/iss-now.json"
answer = urllib.request.urlopen(url)
result = json.loads(answer.read())
place = result["iss_position"]
latitude = float(place["latitude"])
longitude = float(place["longitude"])
print("ISS se encuentra en la latitud", latitude, "y longitud", longitude)

pantalla = turtle.Screen()
pantalla.setup(1080, 720)
pantalla.setworldcoordinates(-180, -90, 180, 90)
pantalla.bgpic("map.jpg")

pantalla.register_shape("iss.png")
iss = turtle.Turtle()
iss.shape("iss.png")
iss.setheading(90)

iss.penup()
iss.goto(longitude, latitude)