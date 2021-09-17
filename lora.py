#Name: Jhoel Perez
#Date: 12/15/2019
#BOT_ID: 545751123332694016
#permissions number = 67648

#Obtain permission integer from discord developer BOT  webpage:
#https://discordapp.com/developers/applications/(BOT_ID)/bots

#Activate bot to work on specific channel with permission integer:
#hhtps://discordapp.com/oauth2/authorize?client_id=(BOT_ID)&scope=bot&permissions=(permision_token)
#hhtps://discordapp.com/oauth2/authorize?client_id=545751123332694016&scope=bot&permissions=67648

#Resoruces:
#https://pythonprogramming.net/discordpy-basic-bot-tutorial-introduction/


#Source Code
import discord
import random
from discord.ext import commands
import asyncio
import time
import sys
import os

path = os.getcwd()
description = '''Flama 2.2.0'''
guild_id = 483848903717027862
online = False
TIMER = 0

token = "NTQ1NzUxMTIzMzMyNjk0MDE2.XGX8Vw.qy1shjuY2aYB8A57kzZ5ViYz1x8"

phrase_char = '!'

#list of word from vocab
Dict = []
vocablo_file = "vocab.txt"

class Radio():
    

class Vocab():

    # def clean_up(self,crop):
    #     print("---CLEAN UP--- \n")
    #     tmp = []
    #     # print(crop)
    #
    #     # print(crop[0])
    #
    #     for n in crop:
    #         tmp.append(n)
    #     self.clean = True
    #     # print("--- END CLEAN UP--- \n")
    #     return tmp

    def get_vocab(self,file_vocab):
        tmp = []

        with open(file_vocab,"r") as words:
            for f in words:
                tmp.append(f)

        # if not self.clean:
        #     tmp = self.clean_up(tmp)
        return tmp

    def Load(self):
        print("Loading Vocab ... ")
        tmp = []

        self.Phrases = self.get_vocab(self.file)
        # for f in self.Phrases:
        #     print(f)
            # print("Failed loading vocab")

    def __init__(self,fi):
        self.clean = False
        self.file = fi
        self.Phrases = []

        if os.path.exists(path + "//" + str(self.file)):
            self.Load()
        else:
            print("File does not exist. :" + path + "\\" + str(self.file))
            sys.exit()


    def Write(self,Dictionary):
        self.Load()
        tmp = self.get_vocab(self.file)

        if tmp == []:
            print("Phrases in Vocab is empty!")

        #check for repeated phrases
        for phrase in Dictionary:
            if phrase in self.Phrases:
                print("Phrase already in Vocab: ")
            else:
                print(phrase)
                with open(self.file,"a") as file:
                    file.write(f"{str(phrase)}\n")

class mmClient(discord.Client):
    #__init__
    async def on_ready(self):
        #global variables
        self.Dict = []
        global guild

        #__init__ info
        print(self.user.name,description)
        print("--------------------")
        print(self.user.id)
        print("--------------------")
        vocablo = Vocab(vocablo_file)
        self.Dict = vocablo.get_vocab(vocablo_file)
        print(self.Dict)
    #triggered by new message on authoirized server
    async def on_message(self,msg):
        global guild

        #Message chat output to cmd line
        print(f"{msg.channel}: {msg.author.name}: {msg.content}")

        #COMMANDS LIST
        '''
        ese -> says hi
        ! -> symbol to add characters after it to vocab on local 'vocab.txt' file
        help -> display all commands
        http -> save all send url to local 'HTTP.csv' file
        '''
        command = ["ese","help"]

        #Last message from discord server
        m = msg.content.lower()
        #COMMANDS

        ##ESE##
        #---------------------

        if (m == command[0]):
            #empty vocab
            if len(self.Dict) == 0:
                print("MUTE!")
                await msg.channel.send("esee mool")
            #send random phrase from non empty vocab
            elif len(self.Dict)!= 0:
                r = random.randint(0,len(self.Dict)-1)
                await msg.channel.send(self.Dict[r])

        ##HELP##
        #---------------------
        elif (m == command[1]):
            print(description)
            await msg.channel.send(description)
            await msg.channel.send("Teach me new phrases using '" + phrase_char + "Phrase'" )
            # print("Last updated " + os.path.getmtime("\\bot.py"))

        ##PHRASES
        #---------------------
        elif ( m[0] == phrase_char):
            f = str(msg.content)
            m = f[1:]
            self.Dict.append(str(m))
            await msg.channel.send("Escuchala Chamita!! Paz Paz Paz")

        #save hhtp links on local .csv
        elif msg.content.startswith('http'):
            channel = msg.channel
            await channel.send('Ese link de hentai yonaikel')
            with open("HTTP.csv","a") as file:
                file.write(f"{str(time.ctime())} -> {str(msg.content)}\n")

        #shutdown
        elif ("gg" in msg.content.lower()) and msg.author.name == "hyle909":
            await msg.channel.send("chao chiguire")

            #final and only write
            vocablo = Vocab(vocablo_file)
            vocablo.Write(self.Dict)
            await msg.channel.send("recordare nuestros momentos juntos ... ")

            #close client connection
            # await client.close()
            await client.close()


        #timer
        # if(time)

        # #store emojis
        # elif msg.content.startswith(':'):
            # for n in msg.content:
                # if n == ":":
                    # emoji.append(msg.content)

        # elif msg.content.startswith("<@!545751123332694016> "):
            # sms = msg.content.lower()

            # new = sms.split('#')[1]

            # await msg.channel.send(new + " \n Poemas pa ti chamita!")
            # print("|"+ new +"|")

        # elif msg.content.startswith("help"):
            # for cmd in Help:
                # await msg.channel.send(cmd)


        # #spam generator
        # elif command[1] in msg.content.lower() and msg.author.name == "hyle909":
            # for n in range(10):
                # r = random.randint(0,len(Dict)-1)
                # await msg.channel.send(Dict[r])
                # await asyncio.sleep(1)

        # #save hhtp links on local .csv
        # elif msg.content.startswith('http'):
            # channel = msg.channel
            # await channel.send('Ese link de hentai yonaikel')
            # with open("HTTP.csv","a") as file:
                # file.write(f"{str(time.ctime())} -> {str(msg.content)}\n")

        # #emoji shower
        # elif msg.content.startswith(command[2]):
            # r = random.randint(0,len(emoji_list)-1)
            # await msg.channel.send(emoji_list[r])
            # await asyncio.sleep(1)

        # elif "latency" == msg.content.lower():
            # if latency == []:
                # await msg.channel.send("no latency avail")
            # else:
                # await msg.channel.send(f" lat: {latency}\n")

        # elif "cuantos somos" == msg.content.lower():
            # await msg.channel.send(f" somos {guild.member_count } hasta ahora")

        # elif "chat_online" == msg.content.lower() and msg.author.name == "hyle909":
            # online, idle, offline = community_report(guild)
            # await msg.channel.send(f" online:{ online} | idle:{ idle} | offline: { offline}")

        # elif msg.content.startswith('flama'):
            # await msg.channel.send('mira {0.author.mention}'.format(msg) + ' flamame esta ps.')

#BOT START
#----------------------
try:
    print("run client")
    client = mmClient()
    client.run(token)

except Exception as e:
    print(e)
    print("END!")
