from bs4 import BeautifulSoup
import requests
from discord.ext import commands

def price_search(game_input):
  html_text = requests.get(f'https://store.steampowered.com/search/?term={game_input}&category1=998').text

  soup = BeautifulSoup(html_text, 'lxml')

  games = soup.find_all('a', class_ = "search_result_row ds_collapse_flag")

  details = ""

  count = 0

  for game in games:
    count += 1
    title = game.find('span', class_ = "title").text.strip()
    price = game.find('div', class_ = 'col search_price responsive_secondrow')
    more_info = game['href']

    try:
      price = price.text.strip()
    except:
      price = game.find('div', class_ = 'col search_price discounted responsive_secondrow').text.strip()
      x = price.split("$")
      price = "Old price: $" + x[1] + "\nNew price: $" + x[2]

    if price == "":
      price = "Not released"

    details += title + "\n"
    details += price + "\n"
    details += "Link: " + more_info + "\n"
    details += "\n"

    if count == 10:
      break

  if not details:
    return "No results found"
  return details

class steam(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.command(aliases=['s'], help='Find steam game prices in USD .steam game')
  async def steam(self, ctx, *, game):
    await ctx.send("```" + price_search(game) + "```")

def setup(client):
  client.add_cog(steam(client))