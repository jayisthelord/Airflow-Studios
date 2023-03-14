from discord.ext import commands
import discord

@commands.command()
async def invite(ctx):
    embed = discord.Embed(title="Invite the bot here", description="[Add Me](https://discord.com/api/oauth2/authorize?client_id=1066628149686833153&permissions=8&scope=bot)")
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(invite)