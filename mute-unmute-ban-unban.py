import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()

bot_token = os.getenv("BOT_TOKEN")
intents = discord.Intents.all()

bot = commands.Bot(command_prefix=".", intents=intents)

@bot.command(name='mute')
async def mute(ctx, member: discord.Member):
    
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if not muted_role:
        muted_role = await ctx.guild.create_role(name="Muted")

    await member.add_roles(muted_role)
    await ctx.send(f"{member.mention} has been muted.")

@bot.command()
async def unmute(ctx, member: discord.Member):
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("You don't have permission to use this command.")
        return

    # Get the Muted role
    muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
    if muted_role:
        await member.remove_roles(muted_role)
        await ctx.send(f"{member.mention} has been unmuted.")
    else:
        await ctx.send("The Muted role does not exist.")

@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if not ctx.author.guild_permissions.kick_members:
        await ctx.send("You don't have permission to use this command.")
        return

    await member.kick(reason=reason)
    await ctx.send(f"{member.mention} has been kicked.")

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use this command.")
        return

    await member.ban(reason=reason)
    await ctx.send(f"{member.mention} has been banned.")

@bot.command()
async def unban(ctx, *, member):
    if not ctx.author.guild_permissions.ban_members:
        await ctx.send("You don't have permission to use this command.")
        return

    banned_users = await ctx.guild.bans();
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f"{user.mention} has been unbanned.")
            return

    await ctx.send("Member not found in the ban list.")



bot.run(bot_token)
