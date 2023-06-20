import discord

# create connections to discord
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event # use library
async def on_ready(): # finish logging in
    print(f'ļogged in as {client.user}')

@client.event 
async def on_message(message): # triggers on every message revieved
    if message.author == client.user:
        return
    print(message.content)
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#client.run()
