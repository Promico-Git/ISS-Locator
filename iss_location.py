import urllib.request, json

# Gets the current location of the ISS
def get_location():
  url = 'http://api.open-notify.org/iss-now.json'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  lat = result['iss_position']['latitude']
  lon = result['iss_position']['longitude']
  map = f'www.google.ca/maps/place/{lat},{lon}'
  location = [lat, lon]
  return location