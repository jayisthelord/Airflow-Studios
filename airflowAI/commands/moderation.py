from discord.ext import commands
import discord
import asyncio

@commands.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member} has been kicked.')

@commands.command()
@commands.has_permissions(kick_members=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name="Muted")
    await member.remove_roles(role)
    await ctx.send(f'{member} has been unmuted.')

@commands.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member} has been banned.')

@commands.command()
@commands.has_permissions(manage_channels=True)
async def lock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=False)
    await ctx.send('This channel has been locked.')

@commands.command()
@commands.has_permissions(manage_channels=True)
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role, send_messages=True)
    await ctx.send('This channel has been unlocked.')

@commands.command()
@commands.has_permissions(manage_roles=True)
async def tempmute(ctx, member: discord.Member, duration: int, unit: str, *, reason=None):
    # Convert the duration to seconds
    if unit == 's':
        seconds = duration
    elif unit == 'm':
        seconds = duration * 60
    elif unit == 'h':
        seconds = duration * 60 * 60
    elif unit == 'd':
        seconds = duration * 60 * 60 * 24
    else:
        await ctx.send(f'Invalid unit "{unit}". Please use s, m, h, or d.')
        return

    # Get the muted role
    muted_role = discord.utils.get(ctx.guild.roles, name='Muted')

    # If the muted role doesn't exist, create it
    if not muted_role:
        muted_role = await ctx.guild.create_role(name='Muted')

        # Loop through all the channels in the server and deny send messages permission for the muted role
        for channel in ctx.guild.channels:
            await channel.set_permissions(muted_role, send_messages=False)

    # Add the muted role to the member
    await member.add_roles(muted_role, reason=reason)

    # Send a message confirming the mute
    await ctx.send(f'{member.mention} has been muted for {duration} {unit}. Reason: {reason}')

    # Wait for the duration and then remove the muted role from the member
    await asyncio.sleep(seconds)
    await member.remove_roles(muted_role, reason='Mute duration expired')
    await ctx.send(f'{member.mention} has been unmuted after {duration} {unit}.')


async def setup(bot):
    bot.add_command(kick)
    bot.add_command(unmute)
    bot.add_command(ban)
    bot.add_command(lock)
    bot.add_command(unlock)
    bot.add_command(tempmute)