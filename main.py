import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')    

@bot.command()
async def random_password(ctx):
    """Chooses between multiple choices."""
    a = random.randint(1,100000)
    await ctx.send(a)   

@bot.command()
async def random_image(ctx):
    """Chooses between multiple choices."""
    f = open('image.png', 'r')
    await ctx.send(a)      

bot.run("MTE4ODQ0ODIyOTU2NjcyMjEzMA.GPYnTa.NuE6C973JHEgLWVwOCPwCWO-wTIDjpNy3vm9tw")
