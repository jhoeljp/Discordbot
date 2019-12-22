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


Dict = []
vocablo_file = "vocablo.txt"
phrase_char = '!'

description = '''Flama 2.0'''
token = "private"

#later
guild_id = 483848903717027862
online = False
TIMER = 0

# def vocablo_loader(file,voc):
    # #starting
    # if voc == "$$$":
        # vocablo = open(file,"r")
        # if vocablo is not null:
            # for f in vocablo:
                # Dict.append(f)
            # vocablo.close()
        # else:
            # print('MUTE!')

    # #ending
    # elif voc == "###":
        # vocablo = open(file,"a")
        # for f in Dict:
            # vocablo.write(f+"\n")
        # vocablo.close()
        # return

    # #new word add
    # else:
        # print('adding new $$$$')
        # Dict.append(voc)
        
class Vocab():

    def clean_up(self,crop):
        print("---CLEAN UP---")
        tmp = []
        clean = crop[0].split("|")
        for i in range(0,len(clean)):
            # list[0][:-1]
            tmp.append(clean[i][:])
        return tmp


    def get_vocab(self,file_vocab):
        tmp = []

        with open(file_vocab,"r") as words:
            for f in words:
                tmp.append(f)
        print(tmp)

        if not self.clean:
            tmp = self.clean_up(tmp)
            print(tmp)

        return tmp

    def Load(self):
        # print("Loading Vocab ... ")
        tmp = [] 
        
        self.Phrases = self.get_vocab(self.file)
        for f in self.Phrases:
            print(f)
            # print("Failed loading vocab")

    def __init__(self,fi):
        self.clean = False
        self.file = fi
        self.Phrases = []

        if os.path.exists(path + "\\" + str(self.file)):
            self.Load()
        else:
            print("File does not exist. ")
            sys.exit()
        
        
    def Write(self,Dictionary):
        self.Load()
        tmp = self.get_vocab(self.file)

        if tmp == []:
            print("Phrases in Vocab is empty!")
        
        with open(self.file,"a") as file:
            for new in Dictionary:
                file.write(f"{str(new)}|")
            for old  in tmp:
                file.write(f"{str(old)}|")

class mmClient(discord.Client):
    # def __init__(self):
        # on_ready()
    
    async def on_ready(self):
        self.Dict = []
        global guild
        
        print('--VOCAB--')
        vocablo = Vocab(vocablo_file)
        self.Dict = vocablo.get_vocab(vocablo_file)                
        
        print(self.user.name,description)
        print(self.user.id)
        print(self.Dict)

        print('--READY--')

    async def on_message(self,msg):
        global guild
        print(f"{msg.channel}: {msg.author.name}: {msg.content}")

        em = []
        # emoji_list = [":flag_ve:"]
        # em = client.emojis
        # latency =  client.latency
        limit = 4
        
        #COMMANDS LIST
        command = ["ese","help"]

        #COMMANDS
        ##ESE##
        m = msg.content.lower()
        # msg.channel.send(m)
        
        if (m == command[0]):
            if len(self.Dict) == 0:
                print("MUTE!")
                await msg.channel.send("esee mool")
            if len(self.Dict) == 1 :
                await msg.channel.send(self.Dict[0])
            elif len(self.Dict)!= 0:
                r = random.randint(0,len(self.Dict)-1)
                await msg.channel.send(self.Dict[r])
        
        ##HELP##
        elif (m == command[1]):
            print(description)
            await msg.channel.send(description)
            #print("Teach me new phrases using " + phrase_char + "+'Devilish'" )
            await msg.channel.send("Teach me new phrases using '" + phrase_char + "Phrase'" )
            # print("Last updated " + os.path.getmtime("\\bot.py"))
            # for cmd in [1,2,3]:
                # print(cmd)
        
        ##PHRASES
        elif ( m[0] == phrase_char):
            f = str(msg.content)
            m = f[1:]
            Dict.append(m)

            await msg.channel.send("Escuchala Chamita!! Paz Paz Paz")

        #save hhtp links on local .csv
        elif msg.content.startswith('http'):
            channel = msg.channel
            await channel.send('Ese link de hentai yonaikel')
            with open("HTTP.csv","a") as file:
                file.write(f"{str(time.ctime())} -> {str(msg.content)}\n")
        
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

        #shutdown
        elif ("gg" in msg.content.lower()) and msg.author.name == "hyle909":
            await msg.channel.send("chao chiguire")
            
            #final and only write
            vocablo = Vocab(vocablo_file)
            vocablo.Write(Dict)
            await msg.channel.send("recordare nuestros momentos juntos ... ")
            
            #close client connection
            await client.close()
            sys.exit()
            

# def Flama():
try:
    client = mmClient()
    client.run(token)

except Exception as e: 
    print(e)
    print("END!")

#BOOT
# try:
    # print("START")
    # Flama()
# except:
    # sys.exit()
