"""
Represents an 8ball to send randon responses

Date Modified: Jan 24, 2022
Author: Chanson Tang
"""

from discord.ext import commands
import random

class eightball(commands.Cog):
  """
  Eightball class represents an eightball
  """
  def __init__(self, client):
    """
    Initialize the object
    :param client: client, the Discord bot
    """
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
    """
    Sends a random 8 ball response
    :param ctx: client
    :return: none
    """
    quote = random.choice(self.responses)
    await ctx.send("`" + quote + "`")


def setup(client):
  client.add_cog(eightball(client))