from config import TOKEN
import discord
import time
from discord.ext import commands


intents = discord.Intents.all()
intents.members = True

app = commands.Bot(command_prefix='!', intents=intents)


def is_me(m):
    return m.author == client.user

@app.event
async def on_ready():
    await app.change_presence(status=discord.Status.online, activity=None)

@app.command()
async def hello(ctx):
    await ctx.send("야 조정현 너 친구한테 그러지마!")

@app.command()
async def 롤체(ctx):
    await ctx.send("https://lolchess.gg/meta")

@app.command()
async def 강동혁(ctx):
    await ctx.send("롤체 개못함")

@app.command()
async def 청소(ctx):
    time.sleep(0.5) 
    await ctx.channel.purge()

app.run(TOKEN)