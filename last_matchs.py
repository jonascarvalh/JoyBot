import requests, json

# API: https://api.henrikdev.xyz/valorant/v3/matches/na/sofia/ggez?filter=competitive

base = 'https://api.henrikdev.xyz/valorant/v3/matches'
region = 'na'
nick = 'sofia'
tag = 'ggez'
filter = '?filter=competitive'

def BuildUrl(base,region,nick,tag,filter):
    return f'{base}/{region}/{nick}/{tag}{filter}'

url = BuildUrl(base,region,nick,tag,filter)

try:
    response = requests.get(url)
    data = response.json()
except:
    print('error')

print(json.dumps(data, indent=4))