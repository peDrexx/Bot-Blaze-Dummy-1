import requests
import json
import time as tm

url = 'https://blaze.com/api/roulette_games/Double'
response = requests.get(url)
r = response.json()

print(r)