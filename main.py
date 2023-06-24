import requests
import json

import win32com.client as wincom


speak = wincom.Dispatch("SAPI.SpVoice")
city  = input("Enter the name od the City: ")

url = f"https://api.weatherapi.com/v1/current.json?key=da26abf4877d4b748d8101718232406&q={city}&aqi=no"
r= requests.get(url)
print(r.text)
weatherDic = json.loads(r. text)
# {city} name {tempetature} {condition} {wind speed} {humidity} {uv- index}
say = (f'city name {city} temperature is {weatherDic["current"]["temp_c"]} degree celcious conditions are {weatherDic["current"]["condition"]["text"]} wind speed is {weatherDic["current"]["wind_kph"]} kilometer per hour and humidity is {weatherDic["current"]["humidity"]} percent and UV index is {weatherDic["current"]["uv"]} .')
print(say)
speak.Speak(say)
