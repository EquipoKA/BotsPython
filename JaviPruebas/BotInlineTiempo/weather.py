#!/usr/bin/env python
# encoding: utf-8

import requests, json

ID_ZARAGOZA = '3104324'

def assembleCallID(ID=ID_ZARAGOZA):
	API_URL='http://api.openweathermap.org/data/2.5/weather?q='
	API_URL += ID
	API_URL += '&APPID=86ac64b568bb3251eb5a22e595b8f4cf'
	return API_URL

def assembleCallName(Name='Zaragoza'):
	API_URL='http://api.openweathermap.org/data/2.5/weather?q='
	API_URL += Name
	API_URL += '&APPID=86ac64b568bb3251eb5a22e595b8f4cf'
	return API_URL

def getJSONRDawData(url):
	r = requests.get(url)
	return r.json()

def parseJSON(rawdata):
	'''
	for i in rawdata['main']:
		print(rawdata['main'][i])
	'''
	temp = rawdata['main']['temp']
	return kelvinToCelsius(float(temp))


def getTempZaragoza():
	print(parseJSON(getJSONRDawData(url)))
	return parseJSON(getJSONRDawData(url))

def fahrenToCelsius(fahren):
	return ((fahren - 32) * 5 / 9)

def kelvinToCelsius(kelvin):
	return kelvin - 273.15

url = assembleCallName()
print(getTempZaragoza())

'''
{'coord': {'lon': -0.88, 'lat': 41.66}, 'weather': [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02n'}], 'base': 'stations', 'main': {'temp': 281.44, 'pressure': 1021, 'humidity': 57, 'temp_min': 280.15, 'temp_max': 283.15}, 'visibility': 10000, 'wind': {'speed': 11.8, 'deg': 290}, 'clouds': {'all': 20}, 'dt': 1509991200, 'sys': {'type': 1, 'id': 5510, 'message': 0.0019, 'country': 'ES', 'sunrise': 1509950555, 'sunset': 1509987073}, 'id': 3104324, 'name': 'Zaragoza', 'cod': 200}
'''

'''
coord
weather
base
main
visibility
wind
clouds
dt
sys
id
name
cod
'''