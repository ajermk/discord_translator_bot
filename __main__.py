import logging
import os
import discord
from dotenv import load_dotenv
from bot import Bot
from translator import Translator

load_dotenv()
translator = Translator(os.getenv('DEEPL_TOKEN'))
intents = discord.Intents.default()
intents.message_content = True

bot = Bot(intents=intents)
bot.run(os.getenv('DISCORD_TOKEN'))