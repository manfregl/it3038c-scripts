import json
import requests

print('Please enter your zip code:')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=5851157ef2c47c4d944bce5bb1336e8e' % zip)
data=r.json()
print(data['weather'][0]['description'])
