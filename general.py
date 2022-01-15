from discord.ext import commands
import random

class general(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(help='Flip a coin')
  async def flip(self, ctx):
    rand = random.randint(0, 1)
    if rand == 0:
      await ctx.send("Heads!")
    else:
      await ctx.send("Tails!")

  @commands.command(help='Roll a dice')
  async def dice(self, ctx):
    rand = random.randint(1, 6)
    await ctx.send("You rolled a " + str(rand) + "!")

  @commands.command(aliases=['random'], help='Generate a random number between two inputs .random x y')
  async def rand(self, ctx, *args):
    if len(args) != 2:
      await ctx.send("Usage: .random x y")
      return
    try:
      val1 = int(args[0])
      val2 = int(args[1])
    except ValueError:
      await ctx.send("Please input numbers")
      return
    if val1 >= val2:
      await ctx.send("x should be greater than y")
      return
    rand = random.randint(val1, val2)
    ctx.send("You got " + str(rand) + "!")

def setup(client):
  client.add_cog(general(client))