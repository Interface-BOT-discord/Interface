from os import getenv
from dotenv import load_dotenv

from utils import Interface_Bot
load_dotenv()
token = getenv('TOKEN')
bot = Interface_Bot()
bot.load_cog('cogs')
bot.run(token)
