import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)


staff_members = [
    {"name": "Jworkerz", "role": "Administrator / Developer", "Staff Member Since": 2023},
    {"name": "Michael", "role": "Administrator / Technical Support", "Staff Member Since": 2023},
    {"name": "Prostoskill", "role": "Administrator / Designer", "Staff Member Since": 2023}
]

@bot.event
async def on_ready():
    print("ბოტი მზადაა!!!")



@bot.command(name='staff')
async def staff_info(ctx):
    embed = discord.Embed(title='Staff Members', color=0x3498bd)

    for staff_member in staff_members:
        embed.add_field(name=staff_member['name'], 
                        value=f'Role: {staff_member["role"]}\nStaff Member Since: {staff_member["staff_member"]}',
                          inline=False)

        await ctx.send(embed=embed)




bot.run(bot_token)