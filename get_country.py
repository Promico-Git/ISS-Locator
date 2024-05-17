import urllib.request, json

# Function to get the country name from the lat and lon
def get_countryName(lat,lon):
  
  url = f'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={lat}&longitude={lon}&localityLanguage=en'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result