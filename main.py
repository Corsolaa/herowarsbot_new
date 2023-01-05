import os
import pymysql
import discord
from dotenv import load_dotenv
from discord.ext import commands


def get_bot():
    load_dotenv()
    prefix = os.getenv("PREFIX")
    intents = discord.Intents.default()
    intents.message_content = True
    return commands.Bot(intents=intents, command_prefix=prefix, case_insensitive=True)


bot = get_bot()


def mysql_execute(mysql_string):
    cur.execute(mysql_string)
    output = cur.fetchall()
    return output


connection = pymysql.connect(
    host="localhost",
    user="hero_wars",
    passwd="",
    database="hero_wars"
)
cur = connection.cursor()
output1 = mysql_execute("SHOW TABLES LIKE 'messages'")
print(output1)
connection.close()


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
    bot.run(os.getenv("TOKEN"))
