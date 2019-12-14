#Name: Jhoel
#Date: 10/13/2018
#BOT ID: 500745224730181652
#token = NTAwNzQ1MjI0NzMwMTgxNjUy.DqPT9g.wR6Tzh5zhmR8L71OXh_5esj4zp4
#permission = 67648
#hhtps://discordapp.com/oauth2/authorize?client_id=500745224730181652&scope=bot&permissions=67648
#hhtps://discordapp.com/oauth2/authorize?client_id=545751123332694016&scope=bot&permissions=67648
#https://pythonprogramming.net/discordpy-basic-bot-tutorial-introduction/
import discord
import random
from discord.ext import commands
import asyncio
import time
#545751123332694016
Dict = []
vocablo_file = "vocablo.txt"

description = '''Flama 1.1.2'''
token = "NTQ1NzUxMTIzMzMyNjk0MDE2.XfQHTw.jDdhFp6weHw-PCLkC5z2xIKVR3k"
guild_id = 483848903717027862
bot = commands.Bot(command_prefix='?', description=description)


# async def user_metrics():
#     await client.wait_until_ready()
#     global guild
#     guild = client.get_guild(guild_id)
#
#     while not client.is_closed():
#
#         try:
#             online, idle, offline = community_report(guild)
#             with open("user_metrics.csv","a") as file:
#                 file.write(f"{int(time.time())},{online},{offline},{idle}\n")
#             await asyncio.sleep(5)
#
#         except Exception as e:
#             print(str(e))
#             await asyncio.sleep(5)\\



# def community_report(self.guild):
#     online = 0
#     idle=0
#     offline = 0
#
#     for i in guild.members:
#         if str(i.status)== "online":
#             online+=1
#         if str(i.status)== "idle":
#             idle+=1
#         if str(i.status)== "offline":
#             offline+=1
#     return online, idle, offline

#---------------PHRASING
# vocablo = open("vocablo.txt","r")
# for frase in vocablo:
#     Dict.append(str(frase))
# vocablo.close()

#----------------MAIN
class mmClient(discord.Client):
    # def __init__(self,description,guild_id):
    #     self.name = description
    #     self.guild_id = guild_id

    async def on_ready(self):
        global guild
        print("ON READY ...")
        vocablo_loader(vocablo_file,"$$$")
        print(self.user.name,description)
        print(self.user.id)

        print('--READY--')

    async def on_message(self,msg):
        global guild
        print(f"{msg.channel}: {msg.author.name}: {msg.content}")

        em = []
        em = client.emojis
        latency =  client.latency
        limit = 4

        Greet = []
        Help = ["añade una frase usando !!"]
        command = ["ese","spam","emoji shower"]

        emoji_list = [":flag_ve:"]

        #spit random from avail commands
        if command[0] in msg.content.lower():
            if len(Dict) < 1:
                print("MUTE!")
                return
            if len(Dict) == 1 :
                await msg.channel.send(Dict[0])
            else:
                r = random.randint(0,len(Dict)-1)
                await msg.channel.send(Dict[r])

        #store emojis
        elif msg.content.startswith(':'):
            for n in msg.content:
                if n == ":":
                    emoji.append(msg.content)

        elif msg.content.startswith('!!'):
            f = str(msg.content)
            m = f[2:]
            Dict.append(m)

        elif msg.content.startswith("help"):
            for cmd in Help:
                await msg.channel.send(cmd)

        #-----------------PHRASING
        elif msg.content.startswith("69#"):
            sms = msg.content.lower()

            new = sms.split('#')[1]

            for cmd in Help:
                await msg.channel.send(new + " \n Poemas pa ti chamita!")
                vocablo_loader(vocablo_file,new)
                print("|||"+ new +"|||")

        #spam generator
        elif command[1] in msg.content.lower() and msg.author.name == "hyle909":
            for n in range(10):
                r = random.randint(0,len(Dict)-1)
                await msg.channel.send(Dict[r])
                await asyncio.sleep(1)

        #save hhtp links on local .csv
        elif msg.content.startswith('http'):
            channel = msg.channel
            await channel.send('Ese link de hentai yonaikel')
            with open("HTTP.csv","a") as file:
                file.write(f"{str(time.ctime())} -> {str(msg.content)}\n")

        #emoji shower
        elif msg.content.startswith(command[2]):
            r = random.randint(0,len(emoji_list)-1)
            await msg.channel.send(emoji_list[r])
            await asyncio.sleep(1)

        elif "latency" == msg.content.lower():
            if latency == []:
                await msg.channel.send("no latency avail")
            else:
                await msg.channel.send(f" lat: {latency}\n")

        elif "cuantos somos" == msg.content.lower():
            await msg.channel.send(f" somos {guild.member_count } hasta ahora")

        elif "chat_online" == msg.content.lower() and msg.author.name == "hyle909":
            online, idle, offline = community_report(guild)
            await msg.channel.send(f" online:{ online} | idle:{ idle} | offline: { offline}")

        elif msg.content.startswith('flama'):
            await msg.channel.send('mira {0.author.mention}'.format(msg) + ' flamame esta ps.')

        #shutdown
        elif ("gg" in msg.content.lower()) and msg.author.name == "hyle909":
            await msg.channel.send("chao chiguire")

            vocablo_loader(vocablo_file,"###")

            await client.close()

def vocablo_loader(file,voc):
    #starting
    if voc == "$$$":
        vocablo = open(file,"r")
        for f in vocablo:
            Dict.append(f)
        vocablo.close()

    #ending
    elif voc == "###":
        vocablo = open(file,"a")
        for f in Dict:
            vocablo.write(f+"\n")
        vocablo.close()
        return

    #new word add
    else:
        print('adding new $$$$')
        Dict.append(voc)

# try:
client = mmClient()
# client.loop.create_task(user_metrics())
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
