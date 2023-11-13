from disnake.ext import commands
from disnake import Intents
from decouple import config


class Config:
    prefix = commands.when_mentioned_or(".")
    intent = Intents.all()
    cogs_folder = config("COGS_FOLDER")
    token = config("TOKEN")
    test_guilds = [int(config("TEST_GUILDS"))]