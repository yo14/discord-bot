import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

client.run('your_secret_token_put_here')



