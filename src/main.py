import requests
import json
import time as tm

while True:
    url = 'https://blaze.com/api/roulette_games/recent'
    response = requests.get(url)
    r = response.json()
    arr = []

    for x in range(len(r)):
        val = r[x]['color']

        if val == 0:
            val = 'Branco'
        if val == 1:
            val = 'Vermelho'
        if val == 2:
            val = 'Preto'
        arr.append(val)

    print(arr)
    tm.sleep(7)