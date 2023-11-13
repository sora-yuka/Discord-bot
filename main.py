import os
from disnake.ext import commands
from config import Config


client = commands.Bot(
    command_prefix=Config.prefix,
    intents=Config.intent,
    test_guilds=Config.test_guilds,
)

@client.event
async def on_ready() -> None:
    print(f"{client.user} is ready to work!")
    

@client.command()
async def load(ctx: commands.Context, extension) -> None:
    print(f"{extension} - {type(extension)}")
    client.load_extension(f"cogs.{extension}")
    
@client.command()
async def unload(ctx: commands.Context, extension) -> None:
    client.unload_extension(f"cogs.{extension}")


for filename in os.listdir(Config.cogs_folder):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")
        

if __name__ == "__main__":
    client.run(Config.token)