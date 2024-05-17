import urllib.request, json

# Gets the flag of a country using country code
def get_country_flag(code):
  url = f'https://restcountries.com/v3.1/alpha/{code}'
  request = urllib.request.urlopen(url)
  result = json.loads(request.read())
  return result
  