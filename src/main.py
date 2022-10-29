import requests
import json
import time as tm
import os

while True:
    url = 'https://blaze.com/api/roulette_games/recent'
    response = requests.get(url)
    r = response.json()
    arr = []

    for x in range(len(r)):
        val = r[x]['color']
        val_i = r[x]

        if val == 0:
            val = 'Branco'
        if val == 1:
            val = 'Vermelho'
        if val == 2:
            val = 'Preto'
        arr.append(val)

    os.system('cls')
    print(arr)
    tm.sleep(7)