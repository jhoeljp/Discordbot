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
guild_id = 483848903717027862
bot = commands.Bot(command_prefix='?', description=description)

class mmClient(discord.Client):
    async def on_ready(self):
        print(self.user.name,description)
        print(self.user.id)
        print('------')

    async def on_message(self,msg):
        print(f"{msg.channel}: {msg.author.name}: {msg.content}")
        guild = client.get_guild(guild_id)
        em = []
        em = client.emojis
        latency =  client.latency
        limit = 4

        Dict = ["Puros apatridas aca fos","Maria Corina me domina \n -Cesar M",
        "Gorilon, malvado, gordo abusador","Viva Chavez Nojodaaa",
        "Marico denme agua pol favol","Subule al Linkin Park ",
        "Ledezma me lo mama","Llevo tu luz y tu aroma en mi piel",
        "Cesar es marico oyo","Capriles principal mmgb","Te amo hyle909",
        "La ONU es un fraude", "Hagamos un trato con el demonio",
        "Ramos Allup es un perro flauta"]

        #spit random from avail commands
        if "ese" in msg.content.lower():
            r = random.randint(0,len(Dict)-1)
            await msg.channel.send(Dict[r])

        #word commands
        elif "squirtle" == msg.content.lower():
            if em == []:
                await msg.channel.send("no emojis avail")
            for i in em:
                await msg.channel.send(i)

        elif "latency" == msg.content.lower():
            if latency == []:
                await msg.channel.send("no latency avail")
            else:
                await msg.channel.send(f" lat: {latency}\n")

        elif "cuantos somos" == msg.content.lower():
            await msg.channel.send(f" somos {guild.member_count } hasta ahora")

        elif "chat_online" == msg.content.lower() and msg.author.name == "hyle909":
            online = 0
            idle=0
            offline = 0

            for i in guild.members:
                if str(i.status)== "online":
                    online+=1
                if str(i.status)== "idle":
                    idle+=1
                if str(i.status)== "offline":
                    offline+=1
            await msg.channel.send(f" online:{ online} | idle:{ idle} | offline: { offline}")

        elif ("muerete" in msg.content.lower()) and msg.author.name == "hyle909":
            await msg.channel.send("chao chiguire")
            await client.close()

        elif msg.content.startswith('$up'):
            channel = msg.channel
            await channel.send('Tamos pendiente \N{THUMBS UP SIGN} mmgb')

        elif msg.content.startswith('http'):
            channel = msg.channel
            await channel.send('Ese link de hentai yonaikel')

        elif msg.content.startswith('flama'):
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
