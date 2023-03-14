import discord
from discord.ext import commands

@commands.command()
async def info(ctx):
    embed = discord.Embed(title="Server Information", description="Here's some information about the server", color=0x00ff00)
    embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
    embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=True)
    embed.add_field(name="Total Members", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Bot Creation Date", value="<t:1674342000:D>", inline=True)
    embed.add_field(name="Text Channels", value=len(ctx.guild.text_channels), inline=True)
    embed.add_field(name="Voice Channels", value=len(ctx.guild.voice_channels), inline=True)
    await ctx.send(embed=embed)

@commands.command()
async def update(ctx):
    embed = discord.Embed(title="Last update", description=f"<t:1678575600:D>")
    embed.add_field(name="Features added", value="Commands :D")
    await ctx.send(embed=embed)

@commands.command()
async def about(ctx):
    await ctx.send("Created <t:1674342000:D>")

async def setup(bot):
    bot.add_command(info)
    bot.add_command(update)
    bot.add_command(about)