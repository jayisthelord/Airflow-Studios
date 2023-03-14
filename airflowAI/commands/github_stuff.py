import discord
from discord.ext import commands

@commands.command()
async def docs(ctx):
    embed = discord.Embed(title="Check bots documentation here.", description="[Documentation Link](https://doc.icey.fr)")
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(docs)
