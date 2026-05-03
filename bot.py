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
    print("bot is ready")


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong! Latency: {:.2f}ms'.format(bot.latency * 1000))

@bot.command(name='clear')
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount + 1)

@bot.command(name='bot-info')
async def bot_info(ctx):
    embed = discord.Embed(title='Bot Information', color=0x0000ff)
    embed.add_field(name='Creators', value='EV Jworkerz', inline=False)
    embed.add_field(name='Version', value='1.0.0', inline=False)
    embed.add_field(name='Rank', value='Server Bot', inline=False)
    await ctx.send(embed=embed)


@bot.command(name='Help')
async def help_command(ctx):
    embed = discord.Embed(title='Bot Commands', color=0x3498db)
    embed.add_field(name='!ping', value='Check bot latency', inline=False)
    embed.add_field(name='!help', value='Display this help message', inline=False)

    await ctx.send(embed=embed)

@bot.command(name='serverinvite', aliases=['invite'])
async def server_invite(ctx):
    invite_embed = discord.Embed(title='Server Invite', color=0x3498db)
    invite_embed.description = f'Invite link: [https://discord.gg/pR2dxygYdn]'
    await ctx.send(embed=invite_embed)


@bot.command(name='poll')
async def create_poll(ctx, question, *options):
    if len(options) < 2 or len(options) > 9:
        await ctx.send('Please provide at least 2 and up to 9 options for the poll.')
        return

    formatted_options = '\n'.join([f'{i + 1}. {option}' for i, option in enumerate(options)])
    poll_embed = discord.Embed(title=f'Poll: {question}', description=formatted_options, color=0x3498db)

    poll_message = await ctx.send(embed=poll_embed)
    for i in range(len(options)):
        await poll_message.add_reaction(chr(127462 + i))  # Emoji: 1️⃣, 2️⃣, ..., 9️⃣


bot.run(bot_token)