#Name: Jhoel
#Date: 10/13/2018
#BOT ID: 500745224730181652
#token = NTAwNzQ1MjI0NzMwMTgxNjUy.DqPT9g.wR6Tzh5zhmR8L71OXh_5esj4zp4
#permission = 67648
#hhtps://discordapp.com/oauth2/authorize?client_id=500745224730181652&scope=bot&permissions=67648
#https://pythonprogramming.net/discordpy-basic-bot-tutorial-introduction/
import discord
import random
from discord.ext import commands

description = '''Flama 1.0.1'''

bot = commands.Bot(command_prefix='?', description=description)

##CLIENT
client = discord.Client()

##EVENTS
#event wrapper

# @bot.event
# async def on_ready():
#     print('Spam')
#
# @bot.command()
# async def add(ctx, left: int, right: int):
#     """Adds two numbers together."""
#     await ctx.send(left + right)

@client.event
async def on_ready():
    # print(bot.user.name)
    # print(bot.user.id)
    # print('------')
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(msg):
    #print(f"{msg.channel}: {msg.author.name}: {msg.content}")

    if "ese" in msg.content.lower():
        await msg.channel.send("Que lo que becerro!")

    if msg.content.startswith('flama'):
        await msg.channel.send('mira {0.author.mention}'.format(msg) + ' flamame esta ps.')


client.run("NTAwNzQ1MjI0NzMwMTgxNjUy.DqPT9g.wR6Tzh5zhmR8L71OXh_5esj4zp4")
