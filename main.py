from iss_location import get_location
from get_weather import get_currentWeather
from get_country import get_countryName
from get_flag import get_country_flag
import geopy.distance # pip install geopy
from flask import Flask, render_template
from my_location import get_my_location



app = Flask(__name__)
@app.route('/')
def index():

  # get the location of the ISS
  location = get_location()
  lat = location[0]
  lon = location[1]

  # get the weather at ISS location
  weather = get_currentWeather(lat,lon)
  temp = round(weather['main']['temp'] - 273.15)
  map = f'https://www.google.ca/maps/place/{lat},{lon}'
  

  # get the country the ISS is over
  country = get_countryName(lat,lon)
  countryName = ''
  countryCode = ''
  flag_image = ''
  


  countryName = country['countryName']
  
  
  # Determine if the iss is over water or land
  if countryName == '':
    countryName = 'The ISS is over water'
    flag_image = 'static/images/over_water.jpg'
    countryCode = '---'


  else:
    countryCode = country['countryCode']
    flag = get_country_flag(countryCode)
    flag_image = flag[0]["flags"]["png"]


  # Getting distance between my location and the ISS

  #. 1. Get the user's location
  device_location = get_my_location()
  my_location = device_location['loc']
  my_lat, my_lon = my_location.split(',')  # Split location string into two numbers
  
  # 2. Get distance
  iss_coord = (lat, lon)
  my_coord = (my_lat, my_lon)
  distance = round(geopy.distance.distance(iss_coord, my_coord).km,2)
  
  return render_template('index.html', lat=lat, lon=lon, temp=temp, map=map, countryName=countryName, flag_image=flag_image, distance=distance, countryCode = countryCode)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)