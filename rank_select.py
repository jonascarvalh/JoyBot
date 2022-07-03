import requests, json

# API: https://valorant-api.com/v1/competitivetiers
def rank_image(rank):
    # Rank to upper
    rank = rank.upper()

    # Get API response
    url = 'https://valorant-api.com/v1/competitivetiers'
    try:
        response = requests.get(url)
    except:
        print('Erro ao consultar valorant-api.com!')
    response = response.json()

    # Refining the field
    data = response['data']
    data = data[0]['tiers']

    # Looking for rank ocurrence and returning matching image
    for i in range(len(data)):
        if rank == data[i]['tierName']:
            return data[i]['largeIcon']