from pprint import pprint

import requests
heroes = [{'name': 'Hulk'}, {'name': 'Captain America'}, {'name': 'Thanos'}]
intelligence_heroes = {}
for hero in heroes:
    hero = hero['name']
    response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{hero}')
    intelligence_heroes[hero] = int(response.json()['results'][0]['powerstats']['intelligence'])
    pprint(response.json())
print(max(intelligence_heroes, key=intelligence_heroes.get))
