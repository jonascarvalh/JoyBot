import discord
from decouple import config
from discord.ext import commands, tasks
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound
from valorant_api import mmr_info

bot = commands.Bot('j.')

@bot.event
async def on_ready():
    print(f'Bot Online! {bot.user}')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.message.add_reaction('\N{no entry sign}')
        await ctx.send('Faltam argumentos para o comando!')
    elif isinstance(error, CommandNotFound):
        await ctx.message.add_reaction('\N{no entry sign}')
        await ctx.send('Esse comando não existe!')
    else:
        raise error

@bot.command(name='elo', help='Mostra seu elo e infos.\nArgumentos: <nick> <tag>')
async def elo(ctx, nick, tag):
    try:
        await ctx.message.add_reaction('\N{ballot box with check}')
        await ctx.send(content=ctx.author.mention, embed=mmr_info(bot, nick, tag))
    except:
        await ctx.send('Comando incorreto! Digite _j.elo <nickname> <tagline>_')
        await ctx.send('Caso seu nick seja separado, junte')


# Executando o BOT, deixando-o online
# Você deve passar o token obtido em:
# https://discord.com/developers/applications
TOKEN = config("TOKEN_BOT")
bot.run(TOKEN)