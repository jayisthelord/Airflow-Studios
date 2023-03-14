import discord
from discord.ext import commands

@commands.command()
async def help(ctx):
    embed=discord.Embed(title="airflowAI Help", color=0xffffff)
    embed.add_field(name="Airflow Basic", value=f"AirflowAI Official ~/icey#0001 bot\nWebsite: [click here](https://icey.fr/)\n Server Link: [invite](https://discord.gg/ZD7jmbb3zc)", inline=False)
    embed.add_field(name="Basic", value="` ~/pfp - Show users pfp in embed\n ~/hello - Make bot say hello to you\n ~/goodbye - Make bot say goodbye to you\n ~/chat - Use AI Chat bot\n ~/ping - Check bots latency\n ~/invite - Get invite link for the bot\n ~/creator - Inofrmation about creator`", inline=True)
    embed.add_field(name="Admin Commands", value=f"` ~/say - Make bot say something\n ~/mute - Mute selected member\n ~/kick - Kick selected member\n ~/unmute - Unmute user\n ~/ban - Ban user\n ~/lock - Lock the channel\n ~/unlock - Unlock the channel\n ~/announce - Create an announcement\n ~/load - Load cogs when they did not load\n ~/unload - Unload cogs for fix or reload but use ~/reload for that, its easier and better because it does reload of all cogs (does not load new cogs use ~/load for that)`", inline=True)
    embed.add_field(name="Games", value=f"` ~/snake - Play snake game\n ~/8ball - Ask 8ball a question\n ~/roll - Roll a dice\n ~/flipcoin - Flip a coin\n ~/choose - Make bot choose something like ~/choose ronaldo rl11`", inline=False)
    await ctx.send(embed=embed)

@commands.command()
async def creator(ctx):
    embed = discord.Embed(title="~/icey#0001", description="Cool gui and CEO of airflow")
    await ctx.send(embed=embed)


async def setup(bot):
    bot.add_command(help)
    bot.add_command(creator)
