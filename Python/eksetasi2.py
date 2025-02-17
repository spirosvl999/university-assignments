import requests
import datetime

response = requests.get('https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson')
#print(response.json())

date_1=input("Give me the first date")
date_1=datetime

date_2=input("Give me the second date")
date2=datetime

max1_name=response.json()['results'][0][coordinates]
max1_name=response.json()['results'][0][mag]

max2_name=response.json()['results'][0][coordinates]
max2_name=response.json()['results'][0][mag]