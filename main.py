import discord
from discord.ext import commands

def getToken():
    try:
        tokenFile = open("token.ini", "r")
        tokenData = tokenFile.readline()
    except(FileNotFoundError):
        tokenFile = open("token.ini", "w")
        print("No token file found, creating one. Please enter the bot token in 'token.ini' \n")
        input("Press enter to continue")
        tokenFile.close()
        return None
    tokenFile.close()
    if tokenData == "":
        print("Token File empty, please enter in Bot Token in 'token.ini'")
        input("Press enter to continue\n")
        return None
    else:
        return tokenData

TOKEN = None

while TOKEN is None:
    TOKEN = getToken()

#Hang's here until token file is confirmed

client = commands.Bot(command_prefix = ".") 

@client.event 
async def on_ready():
    print("Bot Connected and is ready to recieve commands")

@client.command(pass_context=True)
async def copy(ctx):
    await client.say(ctx.message.content[5:])



client.run(TOKEN)

