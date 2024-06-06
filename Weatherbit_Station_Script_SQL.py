#from json import response
import requests
import json
import sys
import pandas as pd
from json import loads

#WeatherBit API Key

WeatherBit_Key = '<Your WeatherBit_Key>'
OpenWeather_Key = '<Your OpenWeather_Key>'

#City and Country

city = 'Burlington'
country = 'CA'

# WeatherBit API URL with the API Key, City and Country from variables

WeatherBit_url = "https://api.weatherbit.io/v2.0/current?&city={city}&country{country}&key={api_key}".format(api_key = WeatherBit_Key, city = city, country = country)
OpenWeatherURL = "http://api.openweathermap.org/data/2.5/weather?q=Burlington,CA&appid={key}".format(key = OpenWeather_Key)

#Make a API request using the full WeatherBit URL

WeatherBitJson = requests.get(WeatherBit_url)
OpenWeatherJson = requests.get(OpenWeatherURL)

#Store the JSON data in the WeatherBitResponseAPI variable

WeatherBitResponseAPI = WeatherBitJson.json()
OpenWeatherResponseAPI = OpenWeatherJson.json()

#print(WeatherBitResponseAPI)

#Assign values to variables

temperature = WeatherBitResponseAPI['data'][0]['temp']
city = WeatherBitResponseAPI['data'][0]['city_name']
country_code = WeatherBitResponseAPI['data'][0]['country_code']
precipitation = WeatherBitResponseAPI['data'][0]['precip']
pressure = WeatherBitResponseAPI['data'][0]['pres']
snow = WeatherBitResponseAPI['data'][0]['snow']
solar_radiation = WeatherBitResponseAPI['data'][0]['solar_rad']
sunrise = WeatherBitResponseAPI['data'][0]['sunrise']
sunset = WeatherBitResponseAPI['data'][0]['sunset']
uv = WeatherBitResponseAPI['data'][0]['uv']
visulazation = WeatherBitResponseAPI['data'][0]['vis']
description = WeatherBitResponseAPI['data'][0]['weather']['description']
wind_direction = WeatherBitResponseAPI['data'][0]['wind_cdir_full']
wind_speed = WeatherBitResponseAPI['data'][0]['wind_spd']
feels_Like = OpenWeatherResponseAPI['main']['feels_like']

#Print Variable values to check if they are assigned correctly

# print(city)
# print(country_code)
# print(temperature)
# print(precipitation)
# print(pressure)
# print(snow)
# print(solar_radiation)
# print(sunrise)
# print(sunset)
# print(uv)
# print(visulazation)
# print(description)
# print(wind_direction)
# print(wind_speed)
# print(feels_Like)

#SQL Server Connection String - Data Source=DELLG5\SQLEXPRESS;Initial Catalog=WeatherStation;Integrated Security=True

import pyodbc as db

#Connect to MS SQL

SQLConnection = db.connect('Driver={ODBC Driver 17 for SQL Server};'
                               'Server=LENOVOLOQ\\SQLEXPRESS;'
                               'Database=WeatherStation;'
                               'Trusted_Connection=yes;')

SQLConnection.setdecoding(db.SQL_CHAR, encoding='latin1')
SQLConnection.setencoding('latin1')

insert_data = SQLConnection.cursor()

#Insert Variable sinto MS SQL

query = '''INSERT INTO [dbo].[Weather]([Temperature],[Snow],[SolarRadiation],[UVIndex],[Visulazation],[Description],[WindSpeed],[Sunrise],[Sunset],[Precipitation],[City],[Country],[Pressure],[Wind_Direction],[FeelsLike]) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''

weather_tuple = temperature,snow,solar_radiation,uv,visulazation,description,wind_speed,sunrise,sunset,precipitation,city,country,pressure,wind_direction,feels_Like

insert_data.execute(query, weather_tuple)

#Commit to SQL

SQLConnection.commit()