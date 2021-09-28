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

#/Users/eque/opt/anaconda3/bin/python /Users/eque/Desktop/bot_lora_2021/lora_radio.py


#Dependencies
import discord
from discord.ext import commands,tasks
import asyncio

import random
import time
import sys
import os

path = os.getcwd()
description = '''Flama 2.2.1'''
guild_id = 483848903717027862
online = False
TIMER = 0

phrase_char = '!'
radio_file = "Radio.csv"
http_file = "HTTP.csv"

'''

Radio class requirements
discord.py==1.6.0
python-dotenv==0.15.0
youtube-dl==2021.2.10

source: https://medium.com/pythonland/build-a-discord-bot-in-python-that-plays-music-and-send-gifs-856385e605a1
'''

import youtube_dl
from dotenv import load_dotenv

'''
NO class requirements
Load vocab on vocab file
Dynamicallly updates list of phraes if the phase_char character is used w/ a phrase
At end of programmed file is updated w/ new phrases only!
'''
#list of word from vocab
Dict = []
vocab_file = "vocab.txt"
token_file = "token.txt"
#discord chat roles
chat_slave = "Valadrium"
chat_master = "hyle909"

class Vocab():
    def __init__(self,fi):
        self.clean = False
        self.file = fi
        self.Phrases = []
        self.token = self.get_file_vocab(token_file)[0]

        #on start load up vocabulary file
        if(self.file_exists()):
            self.Load()
        else:
            sys.exit()
            print(str(self.fi) + " file is not on directory " + os.getcwd())

    def get_token(self):
        return str(self.token)

    def get_file_vocab(self,file_vocab):
        tmp = []

        with open(file_vocab,"r") as words:
            for f in words:
                tmp.append(f)
        return tmp

    def Load(self):
        self.Phrases = self.get_file_vocab(self.file)
        print("Loading %s ... "%(self.file))

    def file_exists(self):
        if os.path.exists(path + "//" + str(self.file)):
            return True
        else:
            print("File does not exist. :" + path + "\\" + str(self.file))
            sys.exit()

    def Write(self,Dictionary):
        self.Load()
        tmp = self.get_file_vocab(self.file)

        if tmp == []:
            print("Phrases in Vocab is empty!")

        #check for repeated phrases
        for phrase in Dictionary:
            if phrase not in self.Phrases:
            #     print("Phrase already in Vocab: ")
            # else:
                print("Adding %s to local dictionary "%(phrase))
                with open(self.file,"a") as file:
                    file.write(f"{str(phrase)}\n")

class mmClient(discord.Client):

    #__init__
    async def on_ready(self):
        #define chat client
        self.bot_client = discord.Client
        #global variables
        self.Dict = []
        global guild
        #vocab file object
        self.files_obj = Vocab(vocab_file)

        #__init__ info
        print(self.user.name,description)
        print("--------------------")
        # print(self.user.id)
        print("--------------------")
        self.Dict = self.files_obj.get_file_vocab(vocab_file)
        print(self.Dict)
        print("--------------------")

    def get_bot_token(self):
        self.bot_token = Vocab(vocab_file).get_token()
        print(self.bot_token)
        return self.bot_token

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
        url -> add song url to radio playlist
        '''
        command = ["ese","help","http",'url',"spam"]

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
            await msg.channel.send("Teach me new phrases using '" + phrase_char + " + Phrase'" )
            await msg.channel.send("Add new song to radio using '" + phrase_char + "url + your_url" )
            await msg.channel.send("Add new link to server file using '" + phrase_char + "https + your_url" )
            await msg.channel.send("Spam phrases on chat using th word 'spam' " )
            # print("Last updated " + os.path.getmtime("\\bot.py"))

        ##HTTP##
        #---------------------
        #save hhtp links on local .csv
        #! + 'http' + space + URL ->  to add link to server url storage file
        elif m[0] == phrase_char and m[1:5] == 'http':
            # channel = msg.channel
            await msg.channel.send('Ese link de hentai yonaikel')
            with open(http_file,"a") as file:
                file.write(f"{str(msg.content[6:])}\n")

        ##URL##
        #---------------------
        #add url to radio playlist
        #! + 'url' + space + URL ->  to add youtube link to server playlist
        # print(command[3])
        elif m[0] == phrase_char and m[1:4] == 'url':
            # channel = msg.channel
            await msg.channel.send('Escuchala en la radio menoraaaaa')

            with open(radio_file,"a") as file:
                file.write(f"{str(msg.content[5:])}\n")

        ## ! ## Add PHRASE
        #---------------------
        elif (m[0] == phrase_char) and m[1:4]!= command[3]:
            f = str(msg.content)
            m = f[1:]
            self.Dict.append(str(m))
            await msg.channel.send("Escuchala Chamita!! Paz Paz Paz")

        ##RADIO##
        #---------------------
        #Radio __init__
        elif ("radio" in msg.content.lower()) and msg.author.name == chat_master:
            await msg.channel.send("24/7, Se prendio el bochinche ...")

            # try:
            await self.join(msg.channel)
            time.sleep(4)
            music_list = self.files_obj.get_file_vocab(radio_file)
            if music_list != [] : await self.play(url[0])
            else: print("there is no music to play")

            await msg.channel.send('91.4 Studio 1 FM')
            await msg.channel.send('SAUDI ARAMCOOO')

            # except Exception as e:
            #     print("cannot join voice channel or play music ",e)


        #shutdown
        elif ("gg" in msg.content.lower()) and msg.author.name == chat_master:
            await msg.channel.send("chao chiguire")

            #final and only write
            self.files_obj.Write(self.Dict)
            await msg.channel.send("recordare nuestros momentos juntos ... ")

            #close client connection
            # await client.close()
            await self.bot_client.close(self)

        #conflict instigator
        elif msg.author.name == chat_slave:
            await msg.channel.send('yo me provoques ' + chat_slave)
            for n in range(2):
                r = random.randint(0,len(self.Dict)-1)
                await msg.channel.send(self.Dict[r])
                await asyncio.sleep(1)

        #spam generator
        elif command[4] in msg.content.lower():
            for n in range(10):
                r = random.randint(0,len(self.Dict)-1)
                await msg.channel.send(self.Dict[r])
                await asyncio.sleep(1)


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
def main():
    try:
        print("Connection to client ...")
        print("--------------------")

        client = mmClient()
        bot_token = client.get_bot_token()
        client.run(bot_token)

    except Exception as e:
        print(e)
        print("END!")

## BOF ##
if __name__ == '__main__':
    main()
