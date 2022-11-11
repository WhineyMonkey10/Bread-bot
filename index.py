import discord
from discord.ext.commands import Bot
from discord.utils import get
from discord import Intents
from IPython.display import Image
import requests, json 
import time
import os
from os import system
import sys
from os import system
import sys
import os
python = sys.executable




cooldown = 0

with open('log.txt', "a") as f:
    f.write("\nStarting bot... \n Started sucessfuly at: " + time.ctime())
    f.close()

intents = Intents.all()
client = Bot(intents=discord.Intents.all(), command_prefix='!') 


@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')
    

@client.command()
async def bread(ctx):
    await ctx.send('BREAD FOR LIFE BREAD FOR LOVE :bread:')

@client.command()
async def catcutie(ctx):
    catURL = 'http://aws.random.cat/meow'

    imageURL = json.loads(requests.get(catURL).content)["file"]

    img = Image(requests.get(imageURL).content)
    await ctx.send(imageURL)
    with open('log.txt', "a") as f:
        f.write("\nCatcutie command ran \n Command has been run at: " + time.ctime())
        f.close()

@client.command()
async def feedpeasant(ctx, arg='None'):
    role = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.roles)
    if role in ctx.author.roles:
        if arg == 'None':
          await ctx.send('You must specify a peasant to feed')
        else:
         if arg == 'all':
            await ctx.send('Feeding all peasants :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed all peasants \n Command has been run at: " + time.ctime())
                f.close()
         elif arg == ctx.message.author.mention:
            await ctx.send('You cannot feed yourself goofy')
            with open('log.txt', "a") as f:
                f.write("\nA mod has tried to feed themselves \n Command has been run at: " + time.ctime())
                f.close()
        if arg != 'all' and arg != ctx.message.author.mention:
            await ctx.send(f'Feeding {arg} :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed {arg} \n Command has been run at: " + time.ctime())
                f.close()
    else:
        await ctx.send('You are not a mod, you peasant. Get back to bread farming.')
        with open('log.txt', "a") as f:
            f.write("\nA peasant tried to feed someone \n Command has been run at: " + time.ctime())
            f.close()
@client.command()
async def bully(ctx, arg='None'):
    if cooldown == 1:
        await ctx.send(f'You are on cooldown, peasant for {timeleft - time.time()} seconds')
    else:
        if arg == '724342400641925180' or arg == '@breb':
            await ctx.send('Dont bully our lord and savior')
        else:
            for i in range(5):
                if '@' in arg:
                    await ctx.send(str(arg) + ":bread:")
                    cooldown = 1
                    timeleft = time.coundown(10)
                    with open('log.txt', "a") as f:
                        f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                        f.close()
                else:
                    await ctx.send("<@" + str(arg) + ">:bread:")
                    cooldown = 1
                    timeleft = time.coundown(10)

                    with open('log.txt', "a") as f:
                        f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                        f.close()
@client.command()
async def breadedcat(ctx):
    await ctx.send(file=discord.File("cats.jpg"))
    with open('log.txt', "a") as f:
        f.write("\nBreadedcat command \n Command has been run at: " + time.ctime())
        f.close()
@client.command()
async def sunglassescat(ctx):
    await ctx.send('https://imgur.com/a/waJ1h7w')
    with open('log.txt', "a") as f:
        f.write("\nSunglassescat command \n Command has been run at: " + time.ctime())
        f.close()
@client.command()
async def commandlist(ctx, arg = 'None'):
    role = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.roles)
    
    if arg == 'None':
        embedVar = discord.Embed(title="Peasant Commands", description="Commands for stinky peasants :heart:", color=0x00ff00)
        embedVar.add_field(name="Peasant commands", value="!bread, !catcutie, !bully (user id) or (ping user), !breadedcat, !sunglassescat, !wetbread ,!commandlist, !wetbread", inline=False)
        embedVar.add_field(name="Special Commands", value="For now, the only other command you have is !feedpeasant (peasant). More will be added later", inline=False)
        await ctx.send(embed=embedVar)
        with open('log.txt', "a") as f:
            f.write("\n(Normal) commandlist \n Command has been run at: " + time.ctime())
            f.close()

    
    elif arg == 'admin' and role in ctx.author.roles:
        embedVar = discord.Embed(title="Admin Commands", description="Commands only availible to mods/admins of the server :heart:", color=0x00ff00)
        embedVar.add_field(name="Peasant commands", value="You are able to access all the commands peasants can. To see their commands, simply run !commandlist", inline=False)
        embedVar.add_field(name="Special Commands", value="Lol none", inline=False)
        await ctx.send(embed=embedVar)
        with open('log.txt', "a") as f:
            f.write("\n(Admin) commandlist \n Command has been run at: " + time.ctime())
            f.close()
    elif arg == 'admin' and role not in ctx.author.roles:
        await ctx.send('Bro youre such a goofy, you dont even have the right permissions to use this command')
        with open('log.txt', "a") as f:
            f.write("\n(Admin) commandlist was tried to be run by a peasant \n Command has been run at: " + time.ctime())
            f.close()
@client.command()
async def dumpLogs(ctx):
    role = discord.utils.find(lambda r: r.name == 'tech support', ctx.message.author.roles)
    if role in ctx.author.roles:
        await ctx.send(file=discord.File("log.txt"))
    else:
        await ctx.send('No, just, no')

@client.command()
async def newUpdate(message='None'):
    channel = client.get_channel(1039251976682229824)
    await channel.send("**New update to the bread bot!**\nRun the command !updateInfo to see the new command!")

@client.command()
async def updateInfo(ctx):
    await ctx.send("New update: Improved the !bully command")


@client.command()
async def wetbread(ctx):
    await ctx.send("https://imgur.com/a/HqrvEEO")
    
@client.command()
async def restartBread(ctx, reason = 'None'):
    role = discord.utils.find(lambda r: r.name == 'tech support', ctx.message.author.roles)
    if role in ctx.author.roles:
        await ctx.send("Restarting bread bot...")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been restarted for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        os.system("python breadbot.py")
        os.execl(python, python, * sys.argv)
    else:
        await ctx.send('WHY?!?!?')
        with open('log.txt', "a") as f:
            f.write("\nSomeone has tried to restart the bot \n Command has been run at: " + time.ctime())
            f.close()


#user = ctx.message.author
#await ctx.send(f'{user.mention} !bread is a command that sends a message saying "BREAD FOR LIFE BREAD FOR LOVE :bread:"') 
    
client.run("token")

while True:
    if cooldown == 1:
        time.sleep(300)
        cooldown = 0