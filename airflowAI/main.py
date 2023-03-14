import discord
from discord.ext import commands
import os
from config.all import *
import settings

bot = commands.Bot(command_prefix=commands.when_mentioned_or(f"{prefix}"), activity=activity, help_command=None, intents=intents)

@bot.event
async def on_ready():
    channel = discord.utils.get(bot.get_all_channels(), name='icey.fr')
    # Connect to the voice channel
    await channel.connect()
    print(f"2023-03-12 00:31:30 INFO     discord.client Bot connected.")
    print(f"2023-03-12 00:31:30 INFO     discord.client Prefix: {prefix}")
    print(f"2023-03-12 00:31:30 INFO     discord.client Token: {token}")
    print(f"2023-03-12 00:31:30 INFO     discord.client BASE_DIR: {settings.BASE_DIR}")
    print(f"2023-03-12 00:31:30 INFO     discord.client Pinging: {settings.PING}")
    for cmd_file in settings.CMDS_DIR.glob("*.py"):
        if cmd_file !="__init__.py":
            await bot.load_extension(f"commands.{cmd_file.name[:-3]}")
            print(f"Loaded {bot.cogs}")


@bot.event
async def on_member_join(member):
    avatar_url = member.avatar.url
    channel = bot.get_channel(1084221042739912725) # Replace YOUR_CHANNEL_ID with the ID of the channel you want to send the welcome message to
    embed = discord.Embed(title=f"Welcome to {member.guild.name}, {member.name}!", description="Thanks for joining our server.", color=0xeeeeec)
    embed.set_thumbnail(url=avatar_url)
    embed.add_field(name="About", value="This is a friendly community for discussing various topics. Be sure to read the rules before posting.")
    embed.add_field(name="Useful Links", value="Here are some links you might find helpful:\n [Website](https://icey.fr/)\n [Rules](https://icey.fr/rules/)")
    embed.set_footer(text=f"Member #{len(member.guild.members)}")
    await channel.send(embed=embed)

@bot.event
async def on_member_join(member):
    guild = bot.get_guild(GUILD_ID)
    role = guild.get_role(ROLE_ID)
    await member.add_roles(role)

@bot.command()
async def reload(ctx):
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            await bot.unload_extension(f'commands.{filename[:-3]}')
            await bot.load_extension(f'commands.{filename[:-3]}')
    embed = discord.Embed(title="Reloading Commands", description="⚙️ Reloaded commands succesfully")
    await ctx.send(embed=embed)

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        bot.load_extension(f'commands.{filename[:-3]}')

@bot.command()
async def load(ctx, arg):
    await bot.load_extension(arg)

@bot.command()
async def unload(ctx, arg):
    await bot.unload_extension(arg)

bot.run(f"{token}")
