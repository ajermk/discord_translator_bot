import discord
import logging
import os
from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'logged in as {bot.user}')

@bot.slash_command()
async def hello(ctx):
    await ctx.respond("hello!")
load_dotenv()
bot.run(os.getenv('TOKEN'))