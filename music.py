"""
Takes music from YouTube and plays it on to the channel

Date Modified: Jan 24, 2022
Author: Chanson Tang
"""

import discord
from discord.ext import commands
import youtube_dl

class music(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(help='Bot will join your channel')
  async def join(self, ctx):
    """
    Joins the channel of the caller
    :param ctx: client
    """
    if ctx.author.voice is None:
      await ctx.send("`You're not in a voice channel`")
    voice_channel = ctx.author.voice.channel
    if ctx.voice_client is None:
      await voice_channel.connect()
    else:
      await ctx.voice_client.move_to(voice_channel)

  @commands.command(help='Bot will disconect from channel')
  async def disconnect(self, ctx):
    """
    Disconnects from the channel
    :param ctx: client
    """
    await ctx.voice_client.disconnect()

  @commands.command(help='Bot play music from given link, .play url')
  async def play(self, ctx, url):
    """
    Plays music from a given input in the form of a link
    :param ctx: client
    :param url: string, the link of the music to be played
    """
    ctx.voice_client.stop()
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    YDL_OPTIONS = {'format': 'bestaudio'}
    vc = ctx.voice_client

    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
      info = ydl.extract_info(url, download=False)
      url2 = info['formats'][0]['url']
      source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
      vc.play(source)

  @commands.command(help='Bot pauses music if music is playing')
  async def pause(self, ctx):
    """
    Pauses music being played
    :param ctx: client
    """
    await ctx.voice_client.pause()
    await ctx.send("`Paused`")

  @commands.command(help='Bot resumes music if music is playing')
  async def resume(self, ctx):
    """
    Resumes music being played
    :param ctx: client
    """
    await ctx.voice_client.resume()
    await ctx.send("`Resumed`")

def setup(client):
  client.add_cog(music(client))