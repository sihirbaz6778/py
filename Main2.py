import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send("Hi!")



async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


bot.run("MTE2NjgwOTE3MjU4MzY0OTMzMQ.GnBbqU.evqpZE2wmaXgsAi2gwJOXNm_vsZQ0C2wGdaa7U")







