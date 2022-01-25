"""
Uses animechan WebAPI to get anime quotes

Date Modified: Jan 24, 2022
Author: Chanson Tang
"""
from discord.ext import commands
import requests
import json
import random

def get_quote():
    """
    Returns a random quote from a random anime character in a formatted text
    :return: string, quote
    """
    response = requests.get("https://animechan.vercel.app/api/random")
    json_data = json.loads(response.text)
    quote = json_data['quote'] + "\n-" + json_data['character'] + " from " + json_data['anime']
    return(quote)

def get_quote_by(character):
    """
    Returns a random quote from the character of input in a formatted text
    :param character: string, character for quote
    :return: string, quote
    """
    response = requests.get("https://animechan.vercel.app/api/quotes/character?name={}".format(character))
    json_data = json.loads(response.text)
    if 'error' in json_data:
      return(json_data['error'])
    rand = random.choice(json_data)
    quote = rand['quote'] + "\n-" + rand['character'] + " from " + rand['anime']
    return(quote)

def get_quote_from(title):
    """
    Returns a random quote from an anime series of input in a formatted text
    :param title: string, series title for quote
    :return: string, quote
    """
    response = requests.get("https://animechan.vercel.app/api/quotes/anime?title={}".format(title))
    json_data = json.loads(response.text)
    if 'error' in json_data:
      return(json_data['error'])
    rand = random.choice(json_data)
    quote = rand['quote'] + "\n-" + rand['character'] + " from " + rand['anime']
    return(quote)

class anime_quote(commands.Cog):
  """
  Bot command class
  """
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['aq'], help='Gives you a random anime quote')
  async def anime_quote(self, ctx):
    quote = get_quote()
    await ctx.send("```" + quote + "```")

  @commands.command(aliases=['aqc'], help='Gives you a random anime quote from a specific character .aqc character')
  async def anime_quote_character(self, ctx, *, character):
    quote = get_quote_by(character)
    await ctx.send("```" + quote + "```")

  @commands.command(aliases=['aqt'], help='Gives you a random anime quote from a certain title .aqt title')
  async def anime_quote_title(self, ctx, *, title):
    quote = get_quote_from(title)
    await ctx.send("```" + quote + "```")

def setup(client):
  client.add_cog(anime_quote(client))