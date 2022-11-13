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
from discord.ext.commands import has_role

python = sys.executable

class console: # Yay, first comment! :D I made this class to make my small brain only have to run console.log() instead of silly code :D
               # Also, big thanks to spotify for giving me music to listen to while I code :D
               # Cause im smart the code is extremely messy and full of bugs and no comments <3

    def log(message):
        with open("log.txt", "a") as f:
            f.write(f"{message} + \n Command has been run at: {time.ctime()}")
            f.close()


class SlashClient(discord.Client): # This is the class that handles slash commands, big thanks to Google for letting me copy paste code. Cause, honestly, who wants to write code when you can copy paste it? and thats what programmers do, right?
        
    def __init__(self) -> None:
        super().__init__(intents=discord.Intents.default())
        self.tree = discord.app_commands.CommandTree(self)
    
    async def setup_hook(self) -> None:
        self.tree.copy_global_to(guild=discord.Object(id=12345678900987654))
        await self.tree.sync()

async def on_slash_command_error(self, ctx, error):
    await ctx.respond(f"Error: {error}")

client = SlashClient()
os.system("echo $! > $HOME/bread-bot/pid.txt")
with open('log.txt', "a") as f:
    f.write("\nStarting bot... \n Started sucessfuly at: " + time.ctime())
    f.close()


@client.tree.command(name="easter", description="egg") # Lol u thought, funny
async def ping(interaction: discord.Interaction) -> None:
        await interaction.respond("Egg", ephemeral=True)



@client.event # Ready event :)
async def on_ready():
    print(f'Bot connected as {client.user}')
    

@client.tree.command(name="bread", description="Bread") # Pretty self explanatory
async def bread(interaction: discord.Interaction) -> None:
    await interaction.response.send_message('BREAD FOR LIFE BREAD FOR LOVE :bread:')

@client.tree.command(name="catcutie", description="Catcutie") # I think you can guess what this does
async def catcutie(interaction: discord.Interaction) -> None:
    catURL = 'http://aws.random.cat/meow'

    imageURL = json.loads(requests.get(catURL).content)["file"]

    img = Image(requests.get(imageURL).content)
    await interaction.response.send_message(imageURL)
    with open('log.txt', "a") as f:
        f.write("\nCatcutie command ran \n Command has been run at: " + time.ctime())
        f.close()

@client.tree.command(name = "feedpeasant", description = "Feed the peasants") # Hehehe :D
@discord.app_commands.checks.has_role("mod")
async def feedpeasant(interaction: discord.Interaction, arg:str) -> None:
        if arg == 'None':
          await interaction.response.send_message('You must specify a peasant to feed')
        else:
         if arg == 'all':
            await interaction.response.send_message('Feeding all peasants :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed all peasants \n Command has been run at: " + time.ctime()) # I could replace this with my console.log() class, but I'm lazy
                f.close()
         elif arg == interaction.message.author.mention:
            await interaction.response.send_message('You cannot feed yourself goofy')
            with open('log.txt', "a") as f:
                f.write("\nA mod has tried to feed themselves \n Command has been run at: " + time.ctime()) # I could replace this with my console.log() class, but I'm lazy
                f.close()
        if arg != 'all' and arg != interaction.message.author.mention:
            await interaction.response.send_message(f'Feeding {arg} :bread:')
            with open('log.txt', "a") as f:
                f.write("\nA mod has fed {arg} \n Command has been run at: " + time.ctime()) # I could replace this with my console.log() class, but I'm lazy
                f.close()
@client.tree.command(name="bully", description="bullies a user")
async def bully(interaction: discord.Interaction, arg:str) -> None:
    #if cooldown == 1:
       # await interaction.response.send_message(f'You are on cooldown, peasant for {timeleft - time.time()} seconds') # failed attempt at cooldown but i kept it in cause why not
    if arg == '724342400641925180' or arg == '@breb':
        await interaction.response.send_message('Dont bully our lord and savior')
    else:
        for i in range(5):
            if '@' in arg:
                await interaction.channel.send(str(arg) + ":bread:")
                with open('log.txt', "a") as f:
                    f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                    f.close()


            else:
                await interaction.channel.send('<@' + str(arg) + '>:bread:')
                with open('log.txt', "a") as f:
                    f.write("\n Someone has been bullied \n Command has been run at: " + time.ctime())
                    f.close()
        await interaction.response.send_message("User has been bullied!", ephemeral=True)
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
async def commandlist(interaction: discord.Interaction) -> None:    

    embedVar = discord.Embed(title="Peasant Commands", description="Commands for stinky peasants :heart:", color=0x00ff00)
    embedVar.add_field(name="Peasant commands", value="/bread, /catcutie, /bully (ping user), /breadedcat, /sunglassescat, /wetbread ,/commandlist, /wetbread, /breadattack", inline=False)
    await interaction.response.send_message(embed=embedVar)
    with open('log.txt', "a") as f:
        f.write("\n(Normal) commandlist \n Command has been run at: " + time.ctime())
        f.close()

@client.tree.command(name="admin_commands", description="admin_commands")
@discord.app_commands.checks.has_role("mod")
async def admincommands(interaction: discord.Interaction) -> None:
    embedVar = discord.Embed(title="Admin Commands", description="Commands only availible to mods/admins of the server :heart:", color=0x00ff00)
    embedVar.add_field(name="Peasant commands", value="You are able to access all the commands peasants can. To see their commands, simply run /commandlist", inline=False)
    embedVar.add_field(name="Special Commands", value="/feedpeasant (@peasant/all), /admin_commands. More coming soon!", inline=False)
    await interaction.response.send_message(embed=embedVar)
    with open('log.txt', "a") as f:
        f.write("\n(Admin) commandlist \n Command has been run at: " + time.ctime())
        f.close()

@client.tree.command(name = "dumplogs", description="Dump the command logs")
async def dumpLogs(interaction: discord.Interaction):
    role = discord.utils.find(lambda r: r.name == 'tech support', interaction.message.author.roles)
    if role in interaction.author.roles:
        await interaction.response.send_message(file=discord.File("log.txt"))
    else:
        await interaction.response.send_message('No, just, no')

@client.tree.command(name="newupdate", description="New updates to the bread bot")
@discord.app_commands.checks.has_role("tech support")
async def newupdate(interaction : discord.Interaction):
    channel = client.get_channel(1039251976682229824)
    await channel.send("**New update to the bread bot!**\nRun the command /updateinfo to see the new command!")
    await interaction.response.send_message("Update has been sent to the update channel!", ephemeral=True)

@client.tree.command(name="updateinfo", description="Info about the new update")
async def update_info(interaction: discord.Interaction):
    await interaction.response.send_message("**New update:** Finally fixed and completed the breadmanage command")


@client.tree.command(name = "wetbread", description="Wet bread")
async def wetbread(interaction: discord.Interaction):
    await interaction.response.send_message("https://imgur.com/a/HqrvEEO")
    
@client.tree.command(name = "breadmanage", description="Manage the bread bot")
@discord.app_commands.checks.has_role("tech support")

async def breadmanage(interaction: discord.Interaction, reason: str, type: str):
    if type == "restart":
        await interaction.response.send_message("Restarting bread bot... this may take up to a minute")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been restarted for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        with open('pid.txt', "r") as f:
            pid = f.read()
            f.close()
        pid = int(pid)
        if pid == '':
            console.log("No pid found")
        os.system(f"kill {pid}")
        os.system("nohup python index.py &")
        os.system("echo $! > $HOME/bread-bot/pid.txt")
    elif type == "shutdown":
        
        await interaction.response.send_message("Shutting down bread bot...")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been shutdown for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        for i in range(2):
            with open('pid.txt', "r") as f:
                pid = f.read()
                f.close()
            pid = int(pid)
            if pid == '':
                console.log("No pid found")
            os.system(f"kill {pid}")
            os.system("nohup python index.py &")
            os.system("echo $! > $HOME/bread-bot/pid.txt")
    elif type == "update":
        await interaction.response.send_message("Updating bread bot from github... this may take up to two minutes")
        channel = client.get_channel(1039251976682229824)
        await channel.send("**New update to the bread bot!**\nRun the command /updateinfo to see the new command!")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been updated for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        os.system("git stash")
        os.system("git pull https://github.com/WhineyMonkey10/Bread-bot")
        with open('pid.txt', "r") as f:
            pid = f.read()
            f.close()
        if pid == '':
            console.log("No pid found")
        os.kill(pid, 9)
        os.system("nohup python index.py &")
        os.system("echo $! > $HOME/bread-bot/pid.txt")
        

    elif type == "debug":
        await interaction.response.send_message("Debugging bread bot... allow up to 5 minutes for the bot to try to locate the issue")
        await interaction.channel.send(file=discord.File("log.txt"))
        await interaction.channel.send("Logs dumped")
        await interaction.channel.send("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+-=,./<>?;':[]{}|#~`")
        await interaction.channel.send("Restart, then the bot should be working again this will take up to 1 minute. If the bot is still not working, please contact tech support or if the issue is not fixed, please report the bug to fix it in the next update")
        await interaction.channel.send("Restarting bread bot...")
        with open('log.txt', "a") as f:
            f.write(f"\nBread bot has been debugged for the reason {reason} \n Command has been run at: " + time.ctime())
            f.close()
        os.system("python breadbot.py")
        os.execl(python, python, * sys.argv)
    else:
        await interaction.response.send_message("Invalid type! Valid types are: restart, shutdown, update, debug")





@client.tree.command(name = "breadattack", description="Funny bread attack gif")
async def breadattack(interaction: discord.Interaction):
    await interaction.response.send_message("https://cdn.discordapp.com/emojis/708895481886932992.gif?size=64")

@client.tree.command(name = "breadhelp", description="Help with the bread bot")
async def breadhelp(interaction: discord.Interaction):
    embedVar = discord.Embed(title="Bread Bot Help", description="Help with the bread bot", color=0x00ff00)
    embedVar.add_field(name="Commands", value="Run /commandlist to see the commands", inline=False)
    embedVar.add_field(name="Support", value="If you need support, please contact tech support", inline=False)
    embedVar.add_field(name="Bugs", value="If you find a bug, please report it to tech support", inline=False)
    embedVar.add_field(name="Suggestions", value="If you have a suggestion, please contact tech support", inline=False)
    await interaction.response.send_message(embed=embedVar)
@client.tree.command(name ="testupdateee", description="Test the update command")
async def testupdate(interaction: discord.Interaction):
    await interaction.response.send_message("This is a test update, please ignore this command")

#@client.tree.command(name = "deletemessage", description="Delete a message") #this command is no longer needed
#@discord.app_commands.checks.has_role("tech support")
#async def deletemessage(interaction: discord.Interaction, messageid: ):
#    channel = interaction.channel
#    message = await channel.fetch_message(1040641649606410310)
#    await message.delete()
#    await interaction.response.send_message("Message deleted!", ephemeral=True)
 


#@client.tree.command(name = "kick", description="Kick a peasant")
#@discord.app_commands.checks.has_role("mod")
#async def kick(interaction: discord.Interaction, member: discord.Member, *, reason=None):
#    await member.kick(reason=reason)
#    await interaction.response.send_message(f"Kicked {member.mention}")
#    with open('log.txt', "a") as f:
#        f.write(f"\n{member} has been kicked for the reason {reason} \n Command has been run at: " + time.ctime())
#        f.close()
#

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
    

from dotenv import load_dotenv
load_dotenv()
client.run(os.getenv('TOKEN'))

