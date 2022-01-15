from discord.ext import commands

class format(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['f'], help='Format your text in a certain way')
  async def format(self, ctx, *args):
    await ctx.send("")

def setup(client):
  client.add_cog(format(client))