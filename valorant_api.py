from rank_select import rank_image
import json, requests
import discord

# API: https://dash.valorant-api.com/
def api_info(nick, tagline):
    base = 'https://api.henrikdev.xyz/valorant/v1/mmr'
    region = 'na'

    # Build Url to request
    def build_url(base, region, nick, tagline):
        return f'{base}/{region}/{nick}/{tagline}'

    # Get response API
    try:
        response = requests.get(build_url(base, region, nick, tagline))
        data = response.json()
    except:
        print('Erro na API henrikdev')
    data = data['data']

    # Getting signal of last match
    sinal = ''
    if data['mmr_change_to_last_game'] > 0: sinal = '+'

    # Build Message
    msg = (f"**:trophy: Elo:** {data['currenttierpatched']}"+ f"\n**Nick:** {data['name']}#{data['tag']}"+f"\n**Última Partida:** {sinal}{data['mmr_change_to_last_game']}")

    # Build Embed
    embed_elo = discord.Embed (
        title = f'<:valorant_logo:992931378482135160> Estatísticas Valorant',
        description = (msg),
        color = 0xFF4455
    )
    image = rank_image(data['currenttierpatched'])
    embed_elo.set_thumbnail(url=image)
    
    return embed_elo

