import requests
import json
import os

apikey=(os.getenv('Weather_API'))
location = "19301"
headers = {"accept": "application/json"}

# Make the request and capture the response
def temp():
    url = "http://api.weatherapi.com/v1/forecast.json?key="+ apikey +"&q="+ location +"&days=1&aqi=no&alerts=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    lowTemp = data["forecast"]["forecastday"][0]["day"]["mintemp_f"]
    highTemp = data["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
    avgTemp = (lowTemp + highTemp) / 2
    return int(avgTemp)