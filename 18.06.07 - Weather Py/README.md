
# Reuben Quinto - WeatherPy


```python
# dependencies
import random
import requests
import json
import pandas as pd
import matplotlib.pyplot as plt
from citipy import citipy
from config import api_key

# init stuffs
rand_cities = []
url = "http://api.openweathermap.org/data/2.5/weather?" + "appid=" + api_key 
units = "imperial"

# created random lat & long func
def lat_random():
    # rand between 90
    return round(90*random.random()*random.uniform(-1,1),4)

def long_random():
    # random between 180
    return round(180*random.random()*random.uniform(-1,1),4)

i = 1
while i <= 500 :
    try:
        flag = True
        lat = lat_random()
        long = long_random()
        city = citipy.nearest_city(lat,long)
        max_temp = requests.get(url + "&q=" + city.city_name + "&units=" + units).json()["main"]["temp_max"]
        humidity = requests.get(url + "&q=" + city.city_name + "&units=" + units).json()["main"]["humidity"]
        cloudiness = requests.get(url + "&q=" + city.city_name + "&units=" + units).json()["clouds"]["all"]
        wind_speed = requests.get(url + "&q=" + city.city_name + "&units=" + units).json()["wind"]["speed"]
        url2 = requests.get(url + "&q=" + city.city_name + "&units=" + units).url
        rand_cities.append((lat,long,city.city_name,city.country_code, max_temp, humidity, cloudiness, wind_speed, url2))

    except KeyError:
        pass
        flag = False
    if flag == True:
        i = i + 1

# rand dataframe
weather_df = pd.DataFrame(rand_cities,columns=["latitude","longitude","city","country","max_temp","humidity","cloudiness","wind_speed","url"])
weather_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>latitude</th>
      <th>longitude</th>
      <th>city</th>
      <th>country</th>
      <th>max_temp</th>
      <th>humidity</th>
      <th>cloudiness</th>
      <th>wind_speed</th>
      <th>url</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-9.9670</td>
      <td>-9.4125</td>
      <td>georgetown</td>
      <td>sh</td>
      <td>77.00</td>
      <td>94</td>
      <td>40</td>
      <td>4.70</td>
      <td>http://api.openweathermap.org/data/2.5/weather...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-15.7139</td>
      <td>2.3494</td>
      <td>jamestown</td>
      <td>sh</td>
      <td>55.50</td>
      <td>64</td>
      <td>0</td>
      <td>14.12</td>
      <td>http://api.openweathermap.org/data/2.5/weather...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-78.7229</td>
      <td>54.1989</td>
      <td>east london</td>
      <td>za</td>
      <td>63.24</td>
      <td>100</td>
      <td>0</td>
      <td>13.00</td>
      <td>http://api.openweathermap.org/data/2.5/weather...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>46.3227</td>
      <td>-18.5857</td>
      <td>dingle</td>
      <td>ie</td>
      <td>81.60</td>
      <td>86</td>
      <td>88</td>
      <td>9.08</td>
      <td>http://api.openweathermap.org/data/2.5/weather...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-45.1117</td>
      <td>-6.9195</td>
      <td>saldanha</td>
      <td>za</td>
      <td>57.97</td>
      <td>91</td>
      <td>0</td>
      <td>3.60</td>
      <td>http://api.openweathermap.org/data/2.5/weather...</td>
    </tr>
  </tbody>
</table>
</div>




```python
# to csv
weather_df.to_csv("reubens_weather_pull.csv", index=False,header=True)
```


```python
# print log
print("------------------------------------------------------------------------------------------------")
print("Beginning Data Retrieval")
print("------------------------------------------------------------------------------------------------")

i = 1
for i in range(len(weather_df)):
    print("City Number: " + str(i+1) + " of 500 | City Name: " + weather_df["city"].iloc[i] + "| \n URL:" + weather_df["url"].iloc[i])
    
print("------------------------------------------------------------------------------------------------")
print("End of Data Retrieval")
print("------------------------------------------------------------------------------------------------")
```

    ------------------------------------------------------------------------------------------------
    Beginning Data Retrieval
    ------------------------------------------------------------------------------------------------
    City Number: 1 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 2 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 3 of 500 | City Name: east london| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=east%20london&units=imperial
    City Number: 4 of 500 | City Name: dingle| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dingle&units=imperial
    City Number: 5 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 6 of 500 | City Name: kisanga| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kisanga&units=imperial
    City Number: 7 of 500 | City Name: ayia marina| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ayia%20marina&units=imperial
    City Number: 8 of 500 | City Name: sao miguel do araguaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20miguel%20do%20araguaia&units=imperial
    City Number: 9 of 500 | City Name: dakoro| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dakoro&units=imperial
    City Number: 10 of 500 | City Name: ihosy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ihosy&units=imperial
    City Number: 11 of 500 | City Name: altamira| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=altamira&units=imperial
    City Number: 12 of 500 | City Name: cayenne| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cayenne&units=imperial
    City Number: 13 of 500 | City Name: comodoro rivadavia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=comodoro%20rivadavia&units=imperial
    City Number: 14 of 500 | City Name: belmonte| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=belmonte&units=imperial
    City Number: 15 of 500 | City Name: port-gentil| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port-gentil&units=imperial
    City Number: 16 of 500 | City Name: piranhas| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=piranhas&units=imperial
    City Number: 17 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 18 of 500 | City Name: montbrison| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=montbrison&units=imperial
    City Number: 19 of 500 | City Name: soyo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=soyo&units=imperial
    City Number: 20 of 500 | City Name: upernavik| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=upernavik&units=imperial
    City Number: 21 of 500 | City Name: oriximina| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=oriximina&units=imperial
    City Number: 22 of 500 | City Name: conde| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=conde&units=imperial
    City Number: 23 of 500 | City Name: hermanus| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus&units=imperial
    City Number: 24 of 500 | City Name: tabou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tabou&units=imperial
    City Number: 25 of 500 | City Name: oranzherei| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=oranzherei&units=imperial
    City Number: 26 of 500 | City Name: taoudenni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=taoudenni&units=imperial
    City Number: 27 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 28 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 29 of 500 | City Name: jalu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jalu&units=imperial
    City Number: 30 of 500 | City Name: lamu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lamu&units=imperial
    City Number: 31 of 500 | City Name: antalaha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=antalaha&units=imperial
    City Number: 32 of 500 | City Name: cabanas| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cabanas&units=imperial
    City Number: 33 of 500 | City Name: gourcy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=gourcy&units=imperial
    City Number: 34 of 500 | City Name: gra liyia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=gra%20liyia&units=imperial
    City Number: 35 of 500 | City Name: bathsheba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bathsheba&units=imperial
    City Number: 36 of 500 | City Name: caucaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=caucaia&units=imperial
    City Number: 37 of 500 | City Name: moba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=moba&units=imperial
    City Number: 38 of 500 | City Name: albany| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany&units=imperial
    City Number: 39 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 40 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 41 of 500 | City Name: roald| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=roald&units=imperial
    City Number: 42 of 500 | City Name: touros| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=touros&units=imperial
    City Number: 43 of 500 | City Name: sao paulo de olivenca| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20paulo%20de%20olivenca&units=imperial
    City Number: 44 of 500 | City Name: husavik| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=husavik&units=imperial
    City Number: 45 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 46 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 47 of 500 | City Name: quatre cocos| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=quatre%20cocos&units=imperial
    City Number: 48 of 500 | City Name: los llanos de aridane| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=los%20llanos%20de%20aridane&units=imperial
    City Number: 49 of 500 | City Name: faya| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=faya&units=imperial
    City Number: 50 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 51 of 500 | City Name: varkkallai| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=varkkallai&units=imperial
    City Number: 52 of 500 | City Name: kestel| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kestel&units=imperial
    City Number: 53 of 500 | City Name: casino| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=casino&units=imperial
    City Number: 54 of 500 | City Name: kalabo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kalabo&units=imperial
    City Number: 55 of 500 | City Name: busayra| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=busayra&units=imperial
    City Number: 56 of 500 | City Name: danbury| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=danbury&units=imperial
    City Number: 57 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 58 of 500 | City Name: altay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=altay&units=imperial
    City Number: 59 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 60 of 500 | City Name: bredasdorp| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bredasdorp&units=imperial
    City Number: 61 of 500 | City Name: yuli| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=yuli&units=imperial
    City Number: 62 of 500 | City Name: peyima| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=peyima&units=imperial
    City Number: 63 of 500 | City Name: tasiilaq| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tasiilaq&units=imperial
    City Number: 64 of 500 | City Name: bandarbeyla| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bandarbeyla&units=imperial
    City Number: 65 of 500 | City Name: cayenne| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cayenne&units=imperial
    City Number: 66 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 67 of 500 | City Name: tombouctou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tombouctou&units=imperial
    City Number: 68 of 500 | City Name: puerto ayora| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=puerto%20ayora&units=imperial
    City Number: 69 of 500 | City Name: sao filipe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20filipe&units=imperial
    City Number: 70 of 500 | City Name: gat| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=gat&units=imperial
    City Number: 71 of 500 | City Name: luderitz| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=luderitz&units=imperial
    City Number: 72 of 500 | City Name: salalah| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=salalah&units=imperial
    City Number: 73 of 500 | City Name: amapa| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=amapa&units=imperial
    City Number: 74 of 500 | City Name: kavaratti| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kavaratti&units=imperial
    City Number: 75 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 76 of 500 | City Name: grand-lahou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=grand-lahou&units=imperial
    City Number: 77 of 500 | City Name: touros| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=touros&units=imperial
    City Number: 78 of 500 | City Name: samarinda| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=samarinda&units=imperial
    City Number: 79 of 500 | City Name: buluang| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=buluang&units=imperial
    City Number: 80 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 81 of 500 | City Name: sao joao da barra| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20joao%20da%20barra&units=imperial
    City Number: 82 of 500 | City Name: ouahigouya| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ouahigouya&units=imperial
    City Number: 83 of 500 | City Name: voi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=voi&units=imperial
    City Number: 84 of 500 | City Name: gwanda| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=gwanda&units=imperial
    City Number: 85 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 86 of 500 | City Name: ejura| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ejura&units=imperial
    City Number: 87 of 500 | City Name: bredasdorp| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bredasdorp&units=imperial
    City Number: 88 of 500 | City Name: sungaipenuh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sungaipenuh&units=imperial
    City Number: 89 of 500 | City Name: thinadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=thinadhoo&units=imperial
    City Number: 90 of 500 | City Name: sao jose da coroa grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20jose%20da%20coroa%20grande&units=imperial
    City Number: 91 of 500 | City Name: goderich| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=goderich&units=imperial
    City Number: 92 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 93 of 500 | City Name: saint-philippe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint-philippe&units=imperial
    City Number: 94 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 95 of 500 | City Name: palembang| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=palembang&units=imperial
    City Number: 96 of 500 | City Name: matara| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=matara&units=imperial
    City Number: 97 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 98 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 99 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 100 of 500 | City Name: sao filipe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20filipe&units=imperial
    City Number: 101 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 102 of 500 | City Name: sao filipe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20filipe&units=imperial
    City Number: 103 of 500 | City Name: farafangana| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=farafangana&units=imperial
    City Number: 104 of 500 | City Name: kumba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kumba&units=imperial
    City Number: 105 of 500 | City Name: hermanus| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus&units=imperial
    City Number: 106 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 107 of 500 | City Name: tautira| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tautira&units=imperial
    City Number: 108 of 500 | City Name: goderich| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=goderich&units=imperial
    City Number: 109 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 110 of 500 | City Name: moundou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=moundou&units=imperial
    City Number: 111 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 112 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 113 of 500 | City Name: chitipa| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=chitipa&units=imperial
    City Number: 114 of 500 | City Name: ladnun| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ladnun&units=imperial
    City Number: 115 of 500 | City Name: ancud| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ancud&units=imperial
    City Number: 116 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 117 of 500 | City Name: arraial do cabo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=arraial%20do%20cabo&units=imperial
    City Number: 118 of 500 | City Name: lesogorskiy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lesogorskiy&units=imperial
    City Number: 119 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 120 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 121 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 122 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 123 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 124 of 500 | City Name: sao gabriel da cachoeira| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20gabriel%20da%20cachoeira&units=imperial
    City Number: 125 of 500 | City Name: tabou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tabou&units=imperial
    City Number: 126 of 500 | City Name: san cristobal| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20cristobal&units=imperial
    City Number: 127 of 500 | City Name: capelinha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=capelinha&units=imperial
    City Number: 128 of 500 | City Name: parambu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=parambu&units=imperial
    City Number: 129 of 500 | City Name: omboue| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=omboue&units=imperial
    City Number: 130 of 500 | City Name: kontagora| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kontagora&units=imperial
    City Number: 131 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 132 of 500 | City Name: cotonou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cotonou&units=imperial
    City Number: 133 of 500 | City Name: kitangari| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kitangari&units=imperial
    City Number: 134 of 500 | City Name: camacha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=camacha&units=imperial
    City Number: 135 of 500 | City Name: castro| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=castro&units=imperial
    City Number: 136 of 500 | City Name: riyadh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=riyadh&units=imperial
    City Number: 137 of 500 | City Name: butaritari| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=butaritari&units=imperial
    City Number: 138 of 500 | City Name: meulaboh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=meulaboh&units=imperial
    City Number: 139 of 500 | City Name: taoudenni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=taoudenni&units=imperial
    City Number: 140 of 500 | City Name: tura| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tura&units=imperial
    City Number: 141 of 500 | City Name: mchinji| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mchinji&units=imperial
    City Number: 142 of 500 | City Name: cayenne| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cayenne&units=imperial
    City Number: 143 of 500 | City Name: yarada| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=yarada&units=imperial
    City Number: 144 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 145 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 146 of 500 | City Name: brae| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=brae&units=imperial
    City Number: 147 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 148 of 500 | City Name: ikom| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ikom&units=imperial
    City Number: 149 of 500 | City Name: komsomolskiy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=komsomolskiy&units=imperial
    City Number: 150 of 500 | City Name: necochea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=necochea&units=imperial
    City Number: 151 of 500 | City Name: mahad| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mahad&units=imperial
    City Number: 152 of 500 | City Name: constitucion| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=constitucion&units=imperial
    City Number: 153 of 500 | City Name: dodoma| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dodoma&units=imperial
    City Number: 154 of 500 | City Name: port keats| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port%20keats&units=imperial
    City Number: 155 of 500 | City Name: fagundes| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=fagundes&units=imperial
    City Number: 156 of 500 | City Name: lembeni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lembeni&units=imperial
    City Number: 157 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 158 of 500 | City Name: forest hills| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=forest%20hills&units=imperial
    City Number: 159 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 160 of 500 | City Name: shadegan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=shadegan&units=imperial
    City Number: 161 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 162 of 500 | City Name: bathsheba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bathsheba&units=imperial
    City Number: 163 of 500 | City Name: albany| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany&units=imperial
    City Number: 164 of 500 | City Name: carmen| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=carmen&units=imperial
    City Number: 165 of 500 | City Name: elmadag| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=elmadag&units=imperial
    City Number: 166 of 500 | City Name: cayenne| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cayenne&units=imperial
    City Number: 167 of 500 | City Name: cedar city| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cedar%20city&units=imperial
    City Number: 168 of 500 | City Name: ariquemes| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ariquemes&units=imperial
    City Number: 169 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 170 of 500 | City Name: dwarka| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dwarka&units=imperial
    City Number: 171 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 172 of 500 | City Name: hermanus| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hermanus&units=imperial
    City Number: 173 of 500 | City Name: roald| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=roald&units=imperial
    City Number: 174 of 500 | City Name: bathsheba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bathsheba&units=imperial
    City Number: 175 of 500 | City Name: oussouye| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=oussouye&units=imperial
    City Number: 176 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 177 of 500 | City Name: torbay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=torbay&units=imperial
    City Number: 178 of 500 | City Name: mahebourg| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mahebourg&units=imperial
    City Number: 179 of 500 | City Name: pauini| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=pauini&units=imperial
    City Number: 180 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 181 of 500 | City Name: airai| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=airai&units=imperial
    City Number: 182 of 500 | City Name: sibu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sibu&units=imperial
    City Number: 183 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 184 of 500 | City Name: chuy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=chuy&units=imperial
    City Number: 185 of 500 | City Name: notse| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=notse&units=imperial
    City Number: 186 of 500 | City Name: port-gentil| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port-gentil&units=imperial
    City Number: 187 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 188 of 500 | City Name: quatre cocos| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=quatre%20cocos&units=imperial
    City Number: 189 of 500 | City Name: hobyo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hobyo&units=imperial
    City Number: 190 of 500 | City Name: busselton| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton&units=imperial
    City Number: 191 of 500 | City Name: nouadhibou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=nouadhibou&units=imperial
    City Number: 192 of 500 | City Name: san jose| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20jose&units=imperial
    City Number: 193 of 500 | City Name: meulaboh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=meulaboh&units=imperial
    City Number: 194 of 500 | City Name: marawi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=marawi&units=imperial
    City Number: 195 of 500 | City Name: kapaa| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kapaa&units=imperial
    City Number: 196 of 500 | City Name: roald| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=roald&units=imperial
    City Number: 197 of 500 | City Name: torbay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=torbay&units=imperial
    City Number: 198 of 500 | City Name: doha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=doha&units=imperial
    City Number: 199 of 500 | City Name: suez| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=suez&units=imperial
    City Number: 200 of 500 | City Name: bonthe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bonthe&units=imperial
    City Number: 201 of 500 | City Name: luena| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=luena&units=imperial
    City Number: 202 of 500 | City Name: port-gentil| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port-gentil&units=imperial
    City Number: 203 of 500 | City Name: sinnamary| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sinnamary&units=imperial
    City Number: 204 of 500 | City Name: grand-lahou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=grand-lahou&units=imperial
    City Number: 205 of 500 | City Name: sompeta| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sompeta&units=imperial
    City Number: 206 of 500 | City Name: buchanan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=buchanan&units=imperial
    City Number: 207 of 500 | City Name: sabha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sabha&units=imperial
    City Number: 208 of 500 | City Name: klaksvik| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=klaksvik&units=imperial
    City Number: 209 of 500 | City Name: kigoma| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kigoma&units=imperial
    City Number: 210 of 500 | City Name: otukpo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=otukpo&units=imperial
    City Number: 211 of 500 | City Name: la libertad| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=la%20libertad&units=imperial
    City Number: 212 of 500 | City Name: mataura| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mataura&units=imperial
    City Number: 213 of 500 | City Name: albany| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany&units=imperial
    City Number: 214 of 500 | City Name: namibe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=namibe&units=imperial
    City Number: 215 of 500 | City Name: adrar| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=adrar&units=imperial
    City Number: 216 of 500 | City Name: gamba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=gamba&units=imperial
    City Number: 217 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 218 of 500 | City Name: soyo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=soyo&units=imperial
    City Number: 219 of 500 | City Name: vila franca do campo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=vila%20franca%20do%20campo&units=imperial
    City Number: 220 of 500 | City Name: carnarvon| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=carnarvon&units=imperial
    City Number: 221 of 500 | City Name: high level| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=high%20level&units=imperial
    City Number: 222 of 500 | City Name: carupano| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=carupano&units=imperial
    City Number: 223 of 500 | City Name: guangshui| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=guangshui&units=imperial
    City Number: 224 of 500 | City Name: bandarbeyla| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bandarbeyla&units=imperial
    City Number: 225 of 500 | City Name: takoradi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi&units=imperial
    City Number: 226 of 500 | City Name: santa cruz| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=santa%20cruz&units=imperial
    City Number: 227 of 500 | City Name: matongo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=matongo&units=imperial
    City Number: 228 of 500 | City Name: bintulu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bintulu&units=imperial
    City Number: 229 of 500 | City Name: denia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=denia&units=imperial
    City Number: 230 of 500 | City Name: dubai| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dubai&units=imperial
    City Number: 231 of 500 | City Name: bambous virieux| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bambous%20virieux&units=imperial
    City Number: 232 of 500 | City Name: najran| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=najran&units=imperial
    City Number: 233 of 500 | City Name: albany| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=albany&units=imperial
    City Number: 234 of 500 | City Name: bud| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bud&units=imperial
    City Number: 235 of 500 | City Name: presidente epitacio| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=presidente%20epitacio&units=imperial
    City Number: 236 of 500 | City Name: richards bay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=richards%20bay&units=imperial
    City Number: 237 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 238 of 500 | City Name: ust-kut| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ust-kut&units=imperial
    City Number: 239 of 500 | City Name: hambantota| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hambantota&units=imperial
    City Number: 240 of 500 | City Name: omboue| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=omboue&units=imperial
    City Number: 241 of 500 | City Name: oranjemund| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=oranjemund&units=imperial
    City Number: 242 of 500 | City Name: puerto baquerizo moreno| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=puerto%20baquerizo%20moreno&units=imperial
    City Number: 243 of 500 | City Name: serenje| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=serenje&units=imperial
    City Number: 244 of 500 | City Name: obo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=obo&units=imperial
    City Number: 245 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 246 of 500 | City Name: chuy| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=chuy&units=imperial
    City Number: 247 of 500 | City Name: cayenne| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cayenne&units=imperial
    City Number: 248 of 500 | City Name: prieska| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=prieska&units=imperial
    City Number: 249 of 500 | City Name: takoradi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi&units=imperial
    City Number: 250 of 500 | City Name: iberia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=iberia&units=imperial
    City Number: 251 of 500 | City Name: torrevieja| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=torrevieja&units=imperial
    City Number: 252 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 253 of 500 | City Name: buriti dos lopes| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=buriti%20dos%20lopes&units=imperial
    City Number: 254 of 500 | City Name: taoudenni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=taoudenni&units=imperial
    City Number: 255 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 256 of 500 | City Name: aasiaat| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=aasiaat&units=imperial
    City Number: 257 of 500 | City Name: nara| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=nara&units=imperial
    City Number: 258 of 500 | City Name: labuan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=labuan&units=imperial
    City Number: 259 of 500 | City Name: toamasina| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=toamasina&units=imperial
    City Number: 260 of 500 | City Name: coquimbo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=coquimbo&units=imperial
    City Number: 261 of 500 | City Name: sao paulo de olivenca| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20paulo%20de%20olivenca&units=imperial
    City Number: 262 of 500 | City Name: vanimo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=vanimo&units=imperial
    City Number: 263 of 500 | City Name: atuona| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=atuona&units=imperial
    City Number: 264 of 500 | City Name: sokoto| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sokoto&units=imperial
    City Number: 265 of 500 | City Name: taman| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=taman&units=imperial
    City Number: 266 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 267 of 500 | City Name: east london| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=east%20london&units=imperial
    City Number: 268 of 500 | City Name: darnah| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=darnah&units=imperial
    City Number: 269 of 500 | City Name: punta arenas| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=punta%20arenas&units=imperial
    City Number: 270 of 500 | City Name: tucumcari| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tucumcari&units=imperial
    City Number: 271 of 500 | City Name: castro| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=castro&units=imperial
    City Number: 272 of 500 | City Name: agadez| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=agadez&units=imperial
    City Number: 273 of 500 | City Name: moussoro| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=moussoro&units=imperial
    City Number: 274 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 275 of 500 | City Name: port hawkesbury| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port%20hawkesbury&units=imperial
    City Number: 276 of 500 | City Name: mar del plata| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mar%20del%20plata&units=imperial
    City Number: 277 of 500 | City Name: san alberto| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20alberto&units=imperial
    City Number: 278 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 279 of 500 | City Name: nicoya| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=nicoya&units=imperial
    City Number: 280 of 500 | City Name: tsogni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tsogni&units=imperial
    City Number: 281 of 500 | City Name: turtas| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=turtas&units=imperial
    City Number: 282 of 500 | City Name: busselton| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton&units=imperial
    City Number: 283 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 284 of 500 | City Name: sabang| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sabang&units=imperial
    City Number: 285 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 286 of 500 | City Name: sao filipe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20filipe&units=imperial
    City Number: 287 of 500 | City Name: walvis bay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=walvis%20bay&units=imperial
    City Number: 288 of 500 | City Name: scarborough| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=scarborough&units=imperial
    City Number: 289 of 500 | City Name: itarema| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=itarema&units=imperial
    City Number: 290 of 500 | City Name: itarema| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=itarema&units=imperial
    City Number: 291 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 292 of 500 | City Name: kankan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kankan&units=imperial
    City Number: 293 of 500 | City Name: takoradi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi&units=imperial
    City Number: 294 of 500 | City Name: richards bay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=richards%20bay&units=imperial
    City Number: 295 of 500 | City Name: kamuli| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kamuli&units=imperial
    City Number: 296 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 297 of 500 | City Name: puerto ayora| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=puerto%20ayora&units=imperial
    City Number: 298 of 500 | City Name: wagar| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=wagar&units=imperial
    City Number: 299 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 300 of 500 | City Name: vila velha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=vila%20velha&units=imperial
    City Number: 301 of 500 | City Name: salaga| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=salaga&units=imperial
    City Number: 302 of 500 | City Name: calamar| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=calamar&units=imperial
    City Number: 303 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 304 of 500 | City Name: saint-esteve| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint-esteve&units=imperial
    City Number: 305 of 500 | City Name: saint-philippe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint-philippe&units=imperial
    City Number: 306 of 500 | City Name: ruteng| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ruteng&units=imperial
    City Number: 307 of 500 | City Name: grantham| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=grantham&units=imperial
    City Number: 308 of 500 | City Name: san patricio| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20patricio&units=imperial
    City Number: 309 of 500 | City Name: lompoc| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lompoc&units=imperial
    City Number: 310 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 311 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 312 of 500 | City Name: rakkestad| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rakkestad&units=imperial
    City Number: 313 of 500 | City Name: mecca| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mecca&units=imperial
    City Number: 314 of 500 | City Name: osypenko| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=osypenko&units=imperial
    City Number: 315 of 500 | City Name: marienburg| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=marienburg&units=imperial
    City Number: 316 of 500 | City Name: arraial do cabo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=arraial%20do%20cabo&units=imperial
    City Number: 317 of 500 | City Name: saint george| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint%20george&units=imperial
    City Number: 318 of 500 | City Name: goderich| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=goderich&units=imperial
    City Number: 319 of 500 | City Name: moura| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=moura&units=imperial
    City Number: 320 of 500 | City Name: pisco| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=pisco&units=imperial
    City Number: 321 of 500 | City Name: kudahuvadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kudahuvadhoo&units=imperial
    City Number: 322 of 500 | City Name: epe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=epe&units=imperial
    City Number: 323 of 500 | City Name: cerritos| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cerritos&units=imperial
    City Number: 324 of 500 | City Name: penzance| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=penzance&units=imperial
    City Number: 325 of 500 | City Name: umm lajj| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=umm%20lajj&units=imperial
    City Number: 326 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 327 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 328 of 500 | City Name: huarmey| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=huarmey&units=imperial
    City Number: 329 of 500 | City Name: progreso| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=progreso&units=imperial
    City Number: 330 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 331 of 500 | City Name: stromness| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=stromness&units=imperial
    City Number: 332 of 500 | City Name: cidreira| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cidreira&units=imperial
    City Number: 333 of 500 | City Name: saldanha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saldanha&units=imperial
    City Number: 334 of 500 | City Name: mweka| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mweka&units=imperial
    City Number: 335 of 500 | City Name: luanda| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=luanda&units=imperial
    City Number: 336 of 500 | City Name: sambava| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sambava&units=imperial
    City Number: 337 of 500 | City Name: notse| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=notse&units=imperial
    City Number: 338 of 500 | City Name: lindi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lindi&units=imperial
    City Number: 339 of 500 | City Name: kislovodsk| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kislovodsk&units=imperial
    City Number: 340 of 500 | City Name: tshikapa| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tshikapa&units=imperial
    City Number: 341 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 342 of 500 | City Name: sabha| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sabha&units=imperial
    City Number: 343 of 500 | City Name: yar-sale| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=yar-sale&units=imperial
    City Number: 344 of 500 | City Name: sao filipe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20filipe&units=imperial
    City Number: 345 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 346 of 500 | City Name: marsh harbour| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=marsh%20harbour&units=imperial
    City Number: 347 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 348 of 500 | City Name: doka| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=doka&units=imperial
    City Number: 349 of 500 | City Name: kamuli| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kamuli&units=imperial
    City Number: 350 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 351 of 500 | City Name: iznoski| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=iznoski&units=imperial
    City Number: 352 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 353 of 500 | City Name: anloga| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=anloga&units=imperial
    City Number: 354 of 500 | City Name: mana| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mana&units=imperial
    City Number: 355 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 356 of 500 | City Name: yenagoa| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=yenagoa&units=imperial
    City Number: 357 of 500 | City Name: frunze| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=frunze&units=imperial
    City Number: 358 of 500 | City Name: kindu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kindu&units=imperial
    City Number: 359 of 500 | City Name: namibe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=namibe&units=imperial
    City Number: 360 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 361 of 500 | City Name: carnarvon| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=carnarvon&units=imperial
    City Number: 362 of 500 | City Name: nador| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=nador&units=imperial
    City Number: 363 of 500 | City Name: japura| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=japura&units=imperial
    City Number: 364 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 365 of 500 | City Name: ponta do sol| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ponta%20do%20sol&units=imperial
    City Number: 366 of 500 | City Name: kavieng| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kavieng&units=imperial
    City Number: 367 of 500 | City Name: bambous virieux| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bambous%20virieux&units=imperial
    City Number: 368 of 500 | City Name: salalah| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=salalah&units=imperial
    City Number: 369 of 500 | City Name: broome| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=broome&units=imperial
    City Number: 370 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 371 of 500 | City Name: port elizabeth| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port%20elizabeth&units=imperial
    City Number: 372 of 500 | City Name: mahebourg| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mahebourg&units=imperial
    City Number: 373 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 374 of 500 | City Name: san antonio ilotenango| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20antonio%20ilotenango&units=imperial
    City Number: 375 of 500 | City Name: mahibadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mahibadhoo&units=imperial
    City Number: 376 of 500 | City Name: birao| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=birao&units=imperial
    City Number: 377 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 378 of 500 | City Name: kudahuvadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kudahuvadhoo&units=imperial
    City Number: 379 of 500 | City Name: busselton| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton&units=imperial
    City Number: 380 of 500 | City Name: sokoto| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sokoto&units=imperial
    City Number: 381 of 500 | City Name: maicao| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=maicao&units=imperial
    City Number: 382 of 500 | City Name: arraial do cabo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=arraial%20do%20cabo&units=imperial
    City Number: 383 of 500 | City Name: bredasdorp| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bredasdorp&units=imperial
    City Number: 384 of 500 | City Name: young| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=young&units=imperial
    City Number: 385 of 500 | City Name: filingue| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=filingue&units=imperial
    City Number: 386 of 500 | City Name: umm kaddadah| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=umm%20kaddadah&units=imperial
    City Number: 387 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 388 of 500 | City Name: pacific grove| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=pacific%20grove&units=imperial
    City Number: 389 of 500 | City Name: atar| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=atar&units=imperial
    City Number: 390 of 500 | City Name: torbay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=torbay&units=imperial
    City Number: 391 of 500 | City Name: vanimo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=vanimo&units=imperial
    City Number: 392 of 500 | City Name: torbay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=torbay&units=imperial
    City Number: 393 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 394 of 500 | City Name: marsa matruh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=marsa%20matruh&units=imperial
    City Number: 395 of 500 | City Name: lubango| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lubango&units=imperial
    City Number: 396 of 500 | City Name: luau| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=luau&units=imperial
    City Number: 397 of 500 | City Name: port elizabeth| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port%20elizabeth&units=imperial
    City Number: 398 of 500 | City Name: minas| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=minas&units=imperial
    City Number: 399 of 500 | City Name: goderich| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=goderich&units=imperial
    City Number: 400 of 500 | City Name: puerto ayora| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=puerto%20ayora&units=imperial
    City Number: 401 of 500 | City Name: monrovia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=monrovia&units=imperial
    City Number: 402 of 500 | City Name: faya| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=faya&units=imperial
    City Number: 403 of 500 | City Name: ashington| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ashington&units=imperial
    City Number: 404 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 405 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 406 of 500 | City Name: bogande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bogande&units=imperial
    City Number: 407 of 500 | City Name: san patricio| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20patricio&units=imperial
    City Number: 408 of 500 | City Name: dikson| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=dikson&units=imperial
    City Number: 409 of 500 | City Name: phuket| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=phuket&units=imperial
    City Number: 410 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 411 of 500 | City Name: opuwo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=opuwo&units=imperial
    City Number: 412 of 500 | City Name: myra| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=myra&units=imperial
    City Number: 413 of 500 | City Name: ipixuna| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ipixuna&units=imperial
    City Number: 414 of 500 | City Name: klaksvik| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=klaksvik&units=imperial
    City Number: 415 of 500 | City Name: mitsamiouli| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mitsamiouli&units=imperial
    City Number: 416 of 500 | City Name: airai| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=airai&units=imperial
    City Number: 417 of 500 | City Name: saint-philippe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint-philippe&units=imperial
    City Number: 418 of 500 | City Name: bilma| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bilma&units=imperial
    City Number: 419 of 500 | City Name: rio gallegos| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rio%20gallegos&units=imperial
    City Number: 420 of 500 | City Name: coruripe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=coruripe&units=imperial
    City Number: 421 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 422 of 500 | City Name: inhambane| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=inhambane&units=imperial
    City Number: 423 of 500 | City Name: tasiilaq| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tasiilaq&units=imperial
    City Number: 424 of 500 | City Name: jamestown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=jamestown&units=imperial
    City Number: 425 of 500 | City Name: alta floresta| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=alta%20floresta&units=imperial
    City Number: 426 of 500 | City Name: bhopal| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bhopal&units=imperial
    City Number: 427 of 500 | City Name: lorengau| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=lorengau&units=imperial
    City Number: 428 of 500 | City Name: harper| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=harper&units=imperial
    City Number: 429 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 430 of 500 | City Name: tasiilaq| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tasiilaq&units=imperial
    City Number: 431 of 500 | City Name: soyo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=soyo&units=imperial
    City Number: 432 of 500 | City Name: san juan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=san%20juan&units=imperial
    City Number: 433 of 500 | City Name: ushuaia| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ushuaia&units=imperial
    City Number: 434 of 500 | City Name: saint-philippe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=saint-philippe&units=imperial
    City Number: 435 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 436 of 500 | City Name: port-gentil| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port-gentil&units=imperial
    City Number: 437 of 500 | City Name: zhob| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=zhob&units=imperial
    City Number: 438 of 500 | City Name: tanda| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tanda&units=imperial
    City Number: 439 of 500 | City Name: mongoumba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mongoumba&units=imperial
    City Number: 440 of 500 | City Name: samarai| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=samarai&units=imperial
    City Number: 441 of 500 | City Name: micheweni| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=micheweni&units=imperial
    City Number: 442 of 500 | City Name: mogadishu| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mogadishu&units=imperial
    City Number: 443 of 500 | City Name: chivay| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=chivay&units=imperial
    City Number: 444 of 500 | City Name: axim| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=axim&units=imperial
    City Number: 445 of 500 | City Name: goderich| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=goderich&units=imperial
    City Number: 446 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 447 of 500 | City Name: acapulco| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=acapulco&units=imperial
    City Number: 448 of 500 | City Name: bubaque| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bubaque&units=imperial
    City Number: 449 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 450 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 451 of 500 | City Name: costinesti| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=costinesti&units=imperial
    City Number: 452 of 500 | City Name: ribeira grande| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ribeira%20grande&units=imperial
    City Number: 453 of 500 | City Name: djibo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=djibo&units=imperial
    City Number: 454 of 500 | City Name: castro| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=castro&units=imperial
    City Number: 455 of 500 | City Name: busselton| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=busselton&units=imperial
    City Number: 456 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 457 of 500 | City Name: shakiso| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=shakiso&units=imperial
    City Number: 458 of 500 | City Name: port elizabeth| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port%20elizabeth&units=imperial
    City Number: 459 of 500 | City Name: riyadh| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=riyadh&units=imperial
    City Number: 460 of 500 | City Name: luau| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=luau&units=imperial
    City Number: 461 of 500 | City Name: boende| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=boende&units=imperial
    City Number: 462 of 500 | City Name: cockburn town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cockburn%20town&units=imperial
    City Number: 463 of 500 | City Name: poli| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=poli&units=imperial
    City Number: 464 of 500 | City Name: anisoc| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=anisoc&units=imperial
    City Number: 465 of 500 | City Name: takoradi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi&units=imperial
    City Number: 466 of 500 | City Name: hithadhoo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=hithadhoo&units=imperial
    City Number: 467 of 500 | City Name: opuwo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=opuwo&units=imperial
    City Number: 468 of 500 | City Name: port-gentil| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=port-gentil&units=imperial
    City Number: 469 of 500 | City Name: takoradi| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=takoradi&units=imperial
    City Number: 470 of 500 | City Name: cascais| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cascais&units=imperial
    City Number: 471 of 500 | City Name: mar del plata| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mar%20del%20plata&units=imperial
    City Number: 472 of 500 | City Name: tabou| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=tabou&units=imperial
    City Number: 473 of 500 | City Name: surt| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=surt&units=imperial
    City Number: 474 of 500 | City Name: ossora| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=ossora&units=imperial
    City Number: 475 of 500 | City Name: atar| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=atar&units=imperial
    City Number: 476 of 500 | City Name: wanlaweyn| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=wanlaweyn&units=imperial
    City Number: 477 of 500 | City Name: kalangala| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=kalangala&units=imperial
    City Number: 478 of 500 | City Name: totness| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=totness&units=imperial
    City Number: 479 of 500 | City Name: bonthe| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=bonthe&units=imperial
    City Number: 480 of 500 | City Name: constitucion| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=constitucion&units=imperial
    City Number: 481 of 500 | City Name: labuhan| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=labuhan&units=imperial
    City Number: 482 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 483 of 500 | City Name: cape town| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=cape%20town&units=imperial
    City Number: 484 of 500 | City Name: roald| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=roald&units=imperial
    City Number: 485 of 500 | City Name: nampula| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=nampula&units=imperial
    City Number: 486 of 500 | City Name: georgetown| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=georgetown&units=imperial
    City Number: 487 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 488 of 500 | City Name: xuddur| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=xuddur&units=imperial
    City Number: 489 of 500 | City Name: mayumba| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=mayumba&units=imperial
    City Number: 490 of 500 | City Name: faanui| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=faanui&units=imperial
    City Number: 491 of 500 | City Name: yumen| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=yumen&units=imperial
    City Number: 492 of 500 | City Name: vila franca do campo| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=vila%20franca%20do%20campo&units=imperial
    City Number: 493 of 500 | City Name: laguna| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=laguna&units=imperial
    City Number: 494 of 500 | City Name: maua| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=maua&units=imperial
    City Number: 495 of 500 | City Name: rikitea| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=rikitea&units=imperial
    City Number: 496 of 500 | City Name: salalah| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=salalah&units=imperial
    City Number: 497 of 500 | City Name: la ronge| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=la%20ronge&units=imperial
    City Number: 498 of 500 | City Name: victoria| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=victoria&units=imperial
    City Number: 499 of 500 | City Name: veraval| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=veraval&units=imperial
    City Number: 500 of 500 | City Name: sao gabriel da cachoeira| 
     URL:http://api.openweathermap.org/data/2.5/weather?appid=25bc90a1196e6f153eece0bc0b0fc9eb&q=sao%20gabriel%20da%20cachoeira&units=imperial
    ------------------------------------------------------------------------------------------------
    End of Data Retrieval
    ------------------------------------------------------------------------------------------------
    


```python
# City Latitude vs Max Temperature
plt.scatter(weather_df["latitude"],
            weather_df["max_temp"],
#             s=<var>, 
            c="blue",
            alpha=0.8, 
            edgecolors="Black")

plt.title("Max Temperature vs Lattitude on 07/30/18")
plt.xlabel("Latitude")
plt.ylabel("Max Temperature (F)")
plt.grid(True)
plt.savefig("lat_vs_temp.png")
plt.show()
```


![png](output_4_0.png)



```python
# City Latitude vs Humidity
plt.scatter(weather_df["latitude"],
            weather_df["humidity"],
#             s=<var>, 
            c="blue",
            alpha=0.8, 
            edgecolors="Black")

plt.title("Humidity vs Latitude on 07/30/18")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.savefig("lat_vs_humidity.png")
plt.show()
```


![png](output_5_0.png)



```python
# City Latitude vs Cloudiness
plt.scatter(weather_df["latitude"],
            weather_df["cloudiness"],
#             s=<var>, 
            c="blue",
            alpha=0.8, 
            edgecolors="Black")

plt.title("Cloudiness vs Latitude on 07/30/18")
plt.xlabel("Latitude")
plt.ylabel("Humidity (%)")
plt.grid(True)
plt.savefig("lat_vs_cloudiness.png")
plt.show()
```


![png](output_6_0.png)



```python
# City Latitude vs Wind Speed
plt.scatter(weather_df["latitude"],
            weather_df["wind_speed"],
#             s=<var>, 
            c="blue",
            alpha=0.8, 
            edgecolors="Black")

plt.title("Wind Speed vs City Latitude on 07/30/18")
plt.xlabel("Latitude")
plt.ylabel("Wind Speed (mph)")
plt.grid(True)
plt.savefig("lat_vs_speed.png")
plt.show()
```


![png](output_7_0.png)


## Analysis - Observable Trends:


1. On all metrics (Temperature/Humidity/Cloudiness/Windspeed) appears to be symmetrically distributed from 0 degrees lattitude.
2. There seems to be no relationship between humidity and lattitude.
3. The hottest weather appears to be between -lattitudes 25 west and 25 east.
