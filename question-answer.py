import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents=intents)
@bot.event
async def on_ready():
    print("Bot is ready!")

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content in ["როგორ ხარ?", "როგორ ხარ", "როგორხარ?", "როგორხარ", "rogor xar?", "rogor xar", "rogorxar?", "rogorxar"]:
        await msg.channel.send ("კარგად, თავად როგორ გიკითხოთ?")

@bot.event
async def on_message(msg):
    if msg.author.bot:
        return
    if msg.content in ["მითხარი 1 ფაქტი"]:
       await msg.channel.send ("დედამიწა მრგვალია")



@bot.command(name='date')
async def current_date(ctx):
    current_date = ctx.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'The current date and time is: {current_date}')

bot.run(bot_token)