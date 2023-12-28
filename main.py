from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
import json
import os

months = [0, "January","February","March","April","May","June","July","August","September","October","November","December"]

# Get the Average Temperature
def temp():
    apikey=(os.getenv('Weather_API'))
    location = "19301"
    headers = {"accept": "application/json"}
    url = "http://api.weatherapi.com/v1/forecast.json?key="+ apikey +"&q="+ location +"&days=1&aqi=no&alerts=no"
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    lowTemp = data["forecast"]["forecastday"][0]["day"]["mintemp_f"]
    highTemp = data["forecast"]["forecastday"][0]["day"]["maxtemp_f"]
    avgTemp = (lowTemp + highTemp) / 2
    return int(avgTemp)

#Figure out what color we need
def color(temperature):
    colors = ['White', 'Cyan', 'Varsity Blue', 'Slime', 'Forest Green', 'Varsity Gold', 'Orange', 'Magenta']
    if temperature < 20:
        return colors[0]
    elif temperature < 30:
        return colors[1]
    elif temperature < 40:
        return colors[2]
    elif temperature < 50:
        return colors[3]
    elif temperature < 60:
        return colors[4]
    elif temperature < 70:
        return colors[5]
    elif temperature < 80:
        return colors[6]
    else:
        return colors[7]

# Get Values from APIs
month = months[datetime.now().month]
day = datetime.now().day
temp = temp()
color = color(temp)

# GOOGLE STUFF
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('./google.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Temperature Blanket 2024').sheet1

# Append the data to the last row
data = [month, day, temp, color]
sheet.append_row(data)