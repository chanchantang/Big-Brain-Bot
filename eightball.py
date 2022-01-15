from discord.ext import commands
import random

class eightball(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.responses = [
        "It is Certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I can see it, yes.",
        "Most likely.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
        ]

  @commands.command(aliases=['8'], help='Asks the 8ball a question .8 question')
  async def eightball(self, ctx, *, question):
    quote = random.choice(self.responses)
    await ctx.send("`" + quote + "`")


def setup(client):
  client.add_cog(eightball(client))