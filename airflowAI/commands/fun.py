import discord
from discord.ext import commands
import random 

@commands.command()
async def pfp(ctx, *, user: discord.User=None):
    if user is None:
        user = ctx.author
    avatar_url = user.avatar.url # get user avatear and set it to be an func
    embed=discord.Embed(title=f"{user} Avatar", color=0xeeeeec)
    embed.set_thumbnail(url=f"{avatar_url}")
    await ctx.send(embed=embed) # Send embed with the pfp

@commands.command()
async def hello(ctx):
    await ctx.send('Hello!')

@commands.command()
async def goodbye(ctx):
    await ctx.send('Goodbye!')

@commands.command()
async def chat(ctx):
    await ctx.send('coming soon!!')

@commands.command()
async def say(ctx, *, message):
    """Repeats the specified message"""
    await ctx.send(message)

@commands.command(name='flipcoin')
async def flip_coin(ctx):
    """Flips a coin and outputs either heads or tails."""
    coin = random.choice(['heads', 'tails'])
    await ctx.send(f"The coin landed on **{coin}**!")

@commands.command(name='roll')
async def roll_dice(ctx):
    """Rolls a dice and outputs a number between 1 and 6."""
    dice = random.randint(1, 6)
    await ctx.send(f"You rolled a **{dice}**!")

@commands.command(name='8ball')
async def eight_ball(ctx, *, question):
    """Outputs a random answer to a yes/no question."""
    answers = ['It is certain.', 'Without a doubt.', 'You may rely on it.', 'Yes, definitely.',
               'It is decidedly so.', 'As I see it, yes.', 'Most likely.', 'Yes.', 'Outlook good.',
               'Signs point to yes.', 'Reply hazy, try again.', 'Better not tell you now.', 'Ask again later.',
               'Cannot predict now.', 'Concentrate and ask again.', 'Don’t count on it.', 'Outlook not so good.',
               'My sources say no.', 'Very doubtful.', 'My reply is no.', '🎱 im an 8ball, not a deal with ur shit ball']
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(answers)}")

@commands.command(name='choose')
async def choose_option(ctx, *options):
    """Chooses a random option from a list of options."""
    chosen_option = random.choice(options)
    await ctx.send(f"I choose **{chosen_option}**!")

@commands.command()
async def serverinfo(ctx):
    """Displays information about the server in an embed format."""
    embed = discord.Embed(title=f"{ctx.guild.name} Server Information", color=0x00ff00)
    embed.set_thumbnail(url=ctx.guild.icon.url)
    embed.add_field(name="Server Owner", value=ctx.guild.owner, inline=False)
    embed.add_field(name="Total Members", value=ctx.guild.member_count, inline=False)
    embed.add_field(name="Online Members", value=sum(member.status != discord.Status.offline for member in ctx.guild.members), inline=False)
    embed.add_field(name="Server Region", value=ctx.guild.region, inline=False)
    embed.add_field(name="Creation Date", value=ctx.guild.created_at.strftime("%b %d, %Y"), inline=False)
    await ctx.send(embed=embed)

async def setup(bot):
    bot.add_command(pfp)
    bot.add_command(hello)
    bot.add_command(goodbye)
    bot.add_command(chat)
    bot.add_command(flip_coin)
    bot.add_command(roll_dice)
    bot.add_command(eight_ball)
    bot.add_command(choose_option)
    bot.add_command(serverinfo)