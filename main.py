from lib2to3.pgen2 import token
import discord
from discord.ext import commands
import asyncio, json, colorama, os, sys
from colorama import Fore
colorama.init(autoreset=True)



config = json.load(open('config.json', 'r'))
token = config['token']
msg = config['msg']
owner = config['owner-id']
bl = config['blacklist-id']

intents = discord.Intents.all()
intents.members=True
client = commands.Bot(command_prefix = "+", intents = intents)
client.remove_command('help')

@client.event
async def on_ready():
    os.system('cls')

@client.command()
async def dmall(ctx):
    if str(ctx.author.id) == owner:
        await ctx.message.delete()
        members = ctx.guild.members
        for member in members:
            if str(member.id) in bl:
                print(f"{Fore.BLUE}Didn't send on the member : {member.name} because his id is on the blacklist.")
            else:
                try:
                    await member.send(msg)
                    print(f"{Fore.GREEN}message sent > {member.name} !")
                except:
                    print(f"{Fore.RED}Error > {member.name}")
                    continue
        print(f"{Fore.YELLOW}="*50)
        print(f"{Fore.YELLOW}DMALL FINISH ON {ctx.guild.name} !")
                
client.run(token)