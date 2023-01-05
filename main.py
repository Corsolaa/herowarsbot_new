import os
from dotenv import load_dotenv
from discord.ext import commands

import discord

load_dotenv()
token = os.getenv("TOKEN")
prefix = os.getenv("PREFIX")
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(intents=intents, command_prefix=prefix, case_insensitive=True)


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command()
async def purge(ctx, number: int = 99):
    await ctx.channel.purge(limit=number + 1)


@bot.event
async def on_message(message):
    print(f"{message.guild.name} -=- {message.channel} >> {message.author}: {message.content}")
    if message.content.lower() == "hello julius":
        await message.channel.send(f"Hello {message.author.name}, how are you doing?")
    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(token)
