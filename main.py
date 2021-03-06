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
prefix = "."
client = commands.Bot(command_prefix = prefix) 

@client.event 
async def on_ready():
    await client.change_presence(game=discord.Game(name="GnoMeD"))
    print("Bot Connected and is ready to recieve commands")


# Utility Commands

@client.command(pass_context = True)
async def copy(ctx):
    
    async for message in client.logs_from(ctx.message.channel, limit = 1):
            await client.delete_message(message)
            await client.say(ctx.message.content[len(prefix)+4:])

@client.command(pass_context = True)
async def clear(ctx, amount=10):
    messages = []
    async for message in client.logs_from(ctx.message.channel, limit = int(amount)):
        messages.append(message)
    await client.delete_messages(messages)

@client.command()
async def count(amount = 5):
    for counter in range(amount):
        await client.say(counter)

#Music Bot Commands
'''
@client.command(pass_context = True)
async def join(ctx):
    channel = ctx.message.author.voice_channel
    if channel == None:
        await client.say("Join a voice chat first nig")
        return False
    await client.join_voice_channel(channel)

@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    
'''


client.run(TOKEN)

