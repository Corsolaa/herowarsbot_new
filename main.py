import os
from dotenv import load_dotenv
from discord.ext import commands

import discord

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
bot = commands.Bot(intents=discord.Intents.default(), command_prefix=prefix, case_insensitive=True)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.event
async def on_message(message):
    print(f"{message.channel} >> {message.author}: {message.content}")
    if message.author != bot.user:
        await message.channel.send(message.author)


if __name__ == "__main__":
    bot.run(token)
