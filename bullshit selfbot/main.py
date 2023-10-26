import discord
from discord.ext import commands
import random
import os
# file
file = open("random.txt","r")
list = file.readlines()
#client
client = commands.Bot(command_prefix="irrelevant", self_bot=True)
# colors
black = "\033[1;30m"
red = "\033[1;31m"    
green = "\033[1;32m"
yellow = "\033[1;33m"
blue = "\033[1;34m"    
purple = "\033[1;35m"    
cyan = "\033[1;36m"    
white = "\033[1;37m"    
#token and id
token = input(f"{green}[-]{white} Inpur ur account token: ")
#event1
@client.event
async def on_ready():
    os.system("cls")
    print(f"{red}-- Logged in as {client.user} --{white}")
#event2
@client.event
async def on_message(content):
    if content.content == "" or content.author.id == client.user.id:
        pass
    else:
        message = random.choice(list)
        print(f"{red}NEW MESSAGE{white}")
        print(f"{cyan}[+]{white}{content.author} dmed you : {content.content}")
        id = content.channel.id #maybe idk
        await client.get_channel(id).send(f"{message}\n||coded with love by https://github.com/infamouskoala||")
        print(f"{green}[-]{white} I sent : {message}")
#run
client.run(token, bot=False)