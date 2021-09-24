from flask import Flask
from markupsafe import escape
import requests
import apikeys

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>UndercastServer</h1>"

@app.route("/getLocationDetails/<lat>/<lon>")
def getLocationDetails(lat, lon):
    lat = escape(lat)
    lon = escape(lon)
    return requests.get(f"https://revgeocode.search.hereapi.com/v1/revgeocode?at=${lat}%2C${lon}&lang=en-US&apiKey=${apikeys.HERE_API_KEY}")

@app.route("/searchCity/<searchString>")
def searchCity(searchString):
    searchString = escape(searchString)
    return requests.get(f"https://geocode.search.hereapi.com/v1/geocode?q=${searchSext}&apiKey=${apikeys.HERE_API_KEY}")


@app.route("/weather/<lat>/<lon>")
def weather(lat, lon):
    lat = escape(lat)
    lon = escape(lon)
    return requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&appid=${apikeys.OWM_API_KEY}")
    