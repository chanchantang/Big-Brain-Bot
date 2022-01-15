from discord.ext import commands
import requests
import json
import random

def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    return()

class mal(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(help='')
  async def anime(self, ctx):
    quote = get_quote()
    await ctx.send("```" + quote + "```")


def setup(client):
  client.add_cog(mal(client))