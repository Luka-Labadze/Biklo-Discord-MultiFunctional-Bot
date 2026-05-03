import discord
from discord.ext import commands
from datetime import datetime
import os
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)


@bot.event
async def on_ready():
    print("Bot is ready!")


@bot.command(name='date')
async def current_date(ctx):
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'The current date and time is: {current_date}')



bot.run(bot_token)