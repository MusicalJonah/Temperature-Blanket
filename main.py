from temperature import temp
from color import color
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

months = [0, "January","February","March","April","May","June","July","August","September","October","November","December"]

# Get Values from APIs
month = months[datetime.now().month]
day = datetime.now().day
temp = temp()
color = color(temp)


print("Today is " + month + " " + str(day) + " and the average temperature is " + str(temp) + " degrees Fahrenheit.")

# GOOGLE STUFF
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('./google.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Temperature Blanket 2024').sheet1

# Append the data to the last row
data = [month, day, temp, color]
sheet.append_row(data)