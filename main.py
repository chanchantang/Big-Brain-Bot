import os
import discord
from discord.ext import commands

from replit import db
from keep_alive import keep_alive

import music
import inspire
import eightball
import pals
import anime_quotes
import general
import steam

client = commands.Bot(command_prefix='.', intents = discord.Intents.all())

cogs = [music, inspire, eightball, pals, anime_quotes, general, steam]
for i in range(len(cogs)):
  cogs[i].setup(client)

@client.event
async def on_ready():
  message = ".help"
  await client.change_presence(activity=discord.Game(message))
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_member_join(member):
  await client.get_channel(os.getenv('CHANNEL_ID')).send("`{} has joined the server`".format(member.name))

@client.event
async def on_member_remove(member):
  await client.get_channel(os.getenv('CHANNEL_ID')).send("`{} has left the server`".format(member.name))

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

keep_alive()
client.run(os.getenv('TOKEN'))