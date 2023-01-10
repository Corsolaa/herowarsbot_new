import os

import discord
from dotenv import load_dotenv
from discord.ext import commands

from mysql_configuration import mysql_execute
from mysql_configuration import mysql_check_table
from mysql_configuration import mysql_create_message_table


def get_bot():
    load_dotenv()
    prefix = ">>"
    intents = discord.Intents.default()
    intents.message_content = True
    return commands.Bot(intents=intents, command_prefix=prefix, case_insensitive=True)


bot = get_bot()

# print(mysql_check_table("messages"))
print(mysql_execute("INSERT INTO messages VALUES ('server', 'channel', 'username', 'this is the message');"))


@bot.event
async def on_ready():
    mysql_create_message_table()
    print(f"{bot.user.name} has connected to Discord!")


@bot.command()
async def ping(ctx):
    await ctx.send("pong")


@bot.command(name="purge")
async def delete_messages(ctx, number: int = 99):
    await ctx.channel.purge(limit=number + 1)


@bot.event
async def on_message(message):
    print(f"{message.guild.name} -=- {message.channel} >> {message.author}: {message.content}")
    if message.content.lower() == "hello julius":
        await message.channel.send(f"Hello {message.author.name}, how are you doing?")
    await bot.process_commands(message)


if __name__ == "__main__":
    bot.run(os.getenv("TOKEN"))
