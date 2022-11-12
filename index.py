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



class SlashClient(discord.Client):
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)
    
    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
        await self.tree.sync()


client = SlashClient()
with open('log.txt', "a") as f:
    f.write("\nStarting bot... \n Started sucessfuly at: " + time.ctime())
    f.close()

cooldown = 0

@client.tree.command(name="ping", description="Pong!")
async def ping(interaction: discord.Interaction) -> None:
    await interaction.response.send_message("Pong!")




@client.event
async def on_ready():
    print(f'Bot connected as {client.user}')
    

@client.tree.command(name="bread", description="Bread")
async def bread(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('BREAD FOR LIFE BREAD FOR LOVE :bread:')

@client.tree.command(name="catcutie", description="Catcutie")
async def catcutie(interaction: discord.Interaction) -> None:
    catURL = 'http://aws.random.cat/meow'

    imageURL = json.loads(requests.get(catURL).content)["file"]

    img = Image(requests.get(imageURL).content)
    await interaction.response.send_message(imageURL)
    with open('log.txt', "a") as f:
        f.write("\nCatcutie command ran \n Command has been run at: " + time.ctime())
        f.close()

@client.tree.command(name = "feedpeasant", description = "Feed the peasants")
async def feedpeasant(interaction: discord.Interaction, arg:str) -> None:
    role = discord.utils.find(lambda r: r.name == 'mod', interaction.message.author.roles)
    if role in interaction.author.roles:
        if arg == 'None':
          await interaction.response.send_message('You must specify a peasant to feed')
        else:
         if arg == 'all':
            await interaction.response.send_message('Feeding all peasants :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed all peasants \n Command has been run at: " + time.ctime())
                f.close()
         elif arg == interaction.message.author.mention:
            await interaction.response.send_message('You cannot feed yourself goofy')
            with open('log.txt', "a") as f:
                f.write("\nA mod has tried to feed themselves \n Command has been run at: " + time.ctime())
                f.close()
        if arg != 'all' and arg != interaction.message.author.mention:
            await interaction.response.send_message(f'Feeding {arg} :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed {arg} \n Command has been run at: " + time.ctime())
                f.close()
    else:
        await interaction.response.send_message('You are not a mod, you peasant. Get back to bread farming.')
        with open('log.txt', "a") as f:
            f.write("\nA peasant tried to feed someone \n Command has been run at: " + time.ctime())
            f.close()
@client.tree.command(name="bully", description="bullies a user")
async def bully(interaction: discord.Interaction, arg:str) -> None:
    if cooldown == 1:
        await interaction.response.send_message(f'You are on cooldown, peasant for {timeleft - time.time()} seconds')
    else:
        if arg == '724342400641925180' or arg == '@breb':
            await interaction.response.send_message('Dont bully our lord and savior')
        else:
            for i in range(5):
                if '@' in arg:
                    await interaction.response.send_message(str(arg) + ":bread:")
                    cooldown = 1
                    timeleft = time.coundown(10)
                    with open('log.txt', "a") as f:
                        f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                        f.close()
                else:
                    await interaction.response.send_message("<@" + str(arg) + ">:bread:")
                    cooldown = 1
                    timeleft = time.coundown(10)

                    with open('log.txt', "a") as f:
                        f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                        f.close()
@client.tree.command(name="breadedcat", description="Breaded cat")
async def breadedcat(interaction: discord.Interaction) -> None:
    await interaction.response.send_message(file=discord.File("cats.jpg"))
    with open('log.txt', "a") as f:
        f.write("\nBreadedcat command \n Command has been run at: " + time.ctime())
        f.close()
@client.tree.command(name="sunglassescat", description="Sunglasses cat")
async def sunglassescat(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('https://imgur.com/a/waJ1h7w')
    with open('log.txt', "a") as f:
        f.write("\nSunglassescat command \n Command has been run at: " + time.ctime())
        f.close()
@client.tree.command(name="commandlist", description="Command list to help you")
async def commandlist(interaction: discord.Interaction, arg:str) -> None:
    role = discord.utils.find(lambda r: r.name == 'mod', interaction.message.author.roles)
    
    if arg == 'None':
        embedVar = discord.Embed(title="Peasant Commands", description="Commands for stinky peasants :heart:", color=0x00ff00)
        embedVar.add_field(name="Peasant commands", value="!bread, !catcutie, !bully (user id) or (ping user), !breadedcat, !sunglassescat, !wetbread ,!commandlist, !wetbread", inline=False)
        embedVar.add_field(name="Special Commands", value="For now, the only other command you have is !feedpeasant (peasant). More will be added later", inline=False)
        await interaction.response.send_message(embed=embedVar)
        with open('log.txt', "a") as f:
            f.write("\n(Normal) commandlist \n Command has been run at: " + time.ctime())
            f.close()

    
    elif arg == 'admin' and role in interaction.author.roles:
        embedVar = discord.Embed(title="Admin Commands", description="Commands only availible to mods/admins of the server :heart:", color=0x00ff00)
        embedVar.add_field(name="Peasant commands", value="You are able to access all the commands peasants can. To see their commands, simply run !commandlist", inline=False)
        embedVar.add_field(name="Special Commands", value="Lol none", inline=False)
        await interaction.response.send_message(embed=embedVar)
        with open('log.txt', "a") as f:
            f.write("\n(Admin) commandlist \n Command has been run at: " + time.ctime())
            f.close()
    elif arg == 'admin' and role not in interaction.author.roles:
        await interaction.response.send_message('Bro youre such a goofy, you dont even have the right permissions to use this command')
        with open('log.txt', "a") as f:
            f.write("\n(Admin) commandlist was tried to be run by a peasant \n Command has been run at: " + time.ctime())
            f.close()
@client.tree.command(name = "dumplogs", description="Dump the command logs")
async def dumpLogs(interaction: discord.Interaction):
    role = discord.utils.find(lambda r: r.name == 'tech support', interaction.message.author.roles)
    if role in interaction.author.roles:
        await interaction.response.send_message(file=discord.File("log.txt"))
    else:
        await interaction.response.send_message('No, just, no')

@client.tree.command(name="newupdate", description="New updates to the bread bot")
async def newupdate(interaction : discord.Interaction):
    channel = client.get_channel(1039251976682229824)
    await channel.send("**New update to the bread bot!**\nRun the command !updateInfo to see the new command!")
    await interaction.response.send_message("Update has been sent to the update channel!")

@client.tree.command(name="updateinfo", description="Info about the new update")
async def update_info(interaction: discord.Interaction):
    await interaction.response.send_message("**New update:** Migrated to slash commands, there are still many bugs. Please be patient for patches")


@client.tree.command(name = "wetbread", description="Wet bread")
async def wetbread(interaction: discord.Interaction):
    await interaction.response.send_message("https://imgur.com/a/HqrvEEO")
    
@client.tree.command(name = "restartbread", description="Restart the bread bot")
async def restart_bread(interaction: discord.Interaction, reason: str):
    role = discord.utils.find(lambda r: r.name == 'tech support', interaction.message.author.roles)
    if role in interaction.author.roles:
        await interaction.response.send_message("Restarting bread bot...")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been restarted for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        os.system("python breadbot.py")
        os.execl(python, python, * sys.argv)
    else:
        await interaction.response.send_message('WHY?!?!?')
        with open('log.txt', "a") as f:
            f.write("\nSomeone has tried to restart the bot \n Command has been run at: " + time.ctime())
            f.close()
#
#@client.tree.command()
#async def breadMute(ctx, user='None', reason = 'None'):
#    role = discord.utils.find(lambda r: r.name == 'mod', ctx.message.author.roles)
#    if role in ctx.author.roles:
#        if user == 'None':
#            await ctx.send('Please specify a user to mute :bread:')
#        else:
#            await ctx.send(f"Muting {user} :bread: lol imagine being muted")
#            await timeout(20, user, reason)
#            with open('log.txt', "a") as f:
#                f.write("\nSomeone has muted " + user + "\n Command has been run at: " + time.ctime())
#                f.close()
#    else:
#        await ctx.send('Youre goofy, you dont have the right permissions to use this command')
#        with open('log.txt', "a") as f:
#            f.write("\nSomeone has tried to mute " + user + "\n Command has been run at: " + time.ctime())
#            f.close()
#

#user = ctx.message.author
#await ctx.send(f'{user.mention} !bread is a command that sends a message saying "BREAD FOR LIFE BREAD FOR LOVE :bread:"') 
    
client.run("token")

while True:
    if cooldown == 1:
        time.sleep(300)
        cooldown = 0