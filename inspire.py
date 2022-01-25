"""
Sends random inspiration quotes from zenquotes

Date Modified: Jan 24, 2022
Author: Chanson Tang
"""

from discord.ext import commands
import requests
import json

def get_quote():
    """
    Sends a random inspiration quote
    :return: none
    """
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + "\n-" + json_data[0]['a']
    return(quote)

class inspire(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(help='Gives you an inspiration quote')
  async def inspire(self, ctx):
    quote = get_quote()
    await ctx.send("```" + quote + "```")


def setup(client):
  client.add_cog(inspire(client))