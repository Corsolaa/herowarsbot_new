import os
from dotenv import load_dotenv
from discord.ext import commands

import discord

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix=prefix)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message):
    print(f"{message.guild.name} -=- {message.channel} >> {message.author}: {message.content}")
    if message.content.lower() == "hello julius":
        await message.channel.send(f"Hello {message.author.name}, how are you doing?")


if __name__ == "__main__":
    bot.run(token)
