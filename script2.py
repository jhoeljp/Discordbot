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

description = '''Flama 1.0.2'''
token = "NTAwNzQ1MjI0NzMwMTgxNjUy.DqPT9g.wR6Tzh5zhmR8L71OXh_5esj4zp4"

bot = commands.Bot(command_prefix='?', description=description)

class mmClient(discord.Client):
    async def on_ready(self):
        print(self.user.name,description)
        print(self.user.id)
        print('------')

    async def on_message(self,msg):
        print(f"{msg.channel}: {msg.author.name}: {msg.content}")

        if "ese" in msg.content.lower():
            await msg.channel.send("Que lo que becerro!")

        if ("muerete" in msg.content.lower()) and msg.author.name == "hyle909":
            await msg.channel.send("chao chiguire")
            await client.close()

        if msg.content.startswith('$up'):
            channel = msg.channel
            await channel.send('Tamos pendiente \N{THUMBS UP SIGN} mmgb')

        if msg.content.startswith('flama'):
            await msg.channel.send('mira {0.author.mention}'.format(msg) + ' flamame esta ps.')

# try:
client = mmClient()
client.run(token)
# @bot.event
# async def on_ready():
#     print("GO")
#
# @bot.command()
# async def add(self,msg,left: int, right:int):
#     await msg.send(left+right)
#
# bot.run(token)

#     #client.run_until_complete(start(*args, **kwargs))
# except KeyboardInterrupt:
#     client.run_until_complete(logout())
# # cancel all tasks lingering
# finally:
#     client.close()
