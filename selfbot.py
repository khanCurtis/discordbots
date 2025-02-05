import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import asyncio
import time
import random
import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import asyncio
from pyfiglet import Figlet
import time
from discord.ext import commands
import random
import json
import time 
from time import sleep

token = ""

client = commands.Bot("$", bot=False)

MESSAGE_CONTENTS = ["@everyone nuked by sykoh. lol"]


CHANNEL_NAMES = ["nuked-by-syskoh", "beamed-by-sykoh", "nuked", "2c", "sykoh-is-sexy", "nuked", "sykoh", "2c", "malicious", "sykoh-is-sexy", "beamed-by-sykoh", "sykoh-is-sexy", "2c", "mal", "lmfao", "dumbass", "malicious"]

bot = commands.Bot(command_prefix = "$", self_bot = True)

client = commands.Bot("$", self_bot=True)

client.remove_command('help')

@client.event
async def on_ready():
  print("sykoh SelfBot Online")

with open('config.json') as f:
    config = json.load(f)

stream_url = config.get('stream_url')

@client.command(pass_contex=True)
async def start(ctx):
  await ctx.message.delete()
  print("SelfBot Is Online")
  await ctx.send("`SelfBot Online!`")
  await ctx.send("$help")

@client.command(pass_contex=True)
async def help(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"sykoh SELFBOT", description="Made and Hosted by sykoh", timestamp = ctx.message.created_at, color=discord.Colour.red())

  embed.set_author(name="sykoh", icon_url=ctx.author.avatar_url)

  embed.add_field(name="help", value="Shows this message.", inline=False)
  embed.add_field(name="purge", value="Deletes an amount of your messages.", inline=False)
  embed.add_field(name="chat", value="Chat desired message.", inline=False)
  embed.add_field(name="av", value="Shows mentioned Users Av.", inline=False)
  embed.add_field(name="whois", value="Shows Mention Users Info.", inline=False)
  embed.add_field(name="ping", value="Shows the selfbot ping.", inline=False)
  embed.add_field(name="dm", value="DMall (Message).", inline=False)
  embed.add_field(name="ban", value="Bans mentioned user.", inline=False)
  embed.add_field(name="kick", value="Kicks mentioned user.", inline=False)
  embed.add_field(name="serverinfo", value="serverinfo.", inline=False)
  embed.add_field(name="nuke", value="say $nukehelp for Nuke commands." , inline=False)
  await ctx.send(embed=embed)

@client.command(pass_contex=True)
async def purge(ctx, amount: int): # b'\xfc'
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == client.user).map(lambda m: m):
        try:
           await message.delete()
        except:
          pass 

@client.command()
async def removestatus(ctx):

    try:
        game = discord.Activity(type=-1)
        await client.change_presence(activity=game)
        await ctx.send(f"```Status has been removed```")
    except Exception as e:
        await ctx.send(f"Error: {e}")

@client.command()
async def av(ctx, member: discord.Member):
        embed = discord.Embed(color = discord.Color.from_rgb(147,112,219), timestamp=ctx.message.created_at)
        embed.set_author(name=f" {member}'s AV") 
        embed.set_image(url='{}'.format(member.avatar_url))
        embed.set_footer(text=member.id)
        await ctx.send(embed=embed)
        await ctx.message.delete()


@client.command(pass_contex=True)
async def nukehelp(ctx):
  await ctx.message.delete()
  embed = discord.Embed(title=f"sykohSB", description="sykoh Selfbot Nuker", timestamp = ctx.message.created_at, color=discord.Colour.red())

  embed.set_author(name="12Mal (sykoh.)", icon_url=ctx.author.avatar_url)

  embed.add_field(name="nukehelp", value="Shows this message.", inline=False)
  embed.add_field(name="admin", value="Gives Everyone Admin.", inline=False)
  embed.add_field(name="mention", value="Masspings Channels.", inline=False)
  embed.add_field(name="droles", value="Deletes All Roles.", inline=False)
  embed.add_field(name="roles", value="Spam Creates Roles.", inline=False)
  embed.add_field(name="banall", value="Bans All Members.", inline=False)
  embed.add_field(name="kickall", value="Kicks All Members.", inline=False)
  embed.add_field(name="channels", value="Spams Channels." , inline=False)
  await ctx.send(embed=embed)

@client.command()
async def mention(ctx, amount=10000000000000000000000000):
    await ctx.message.delete()
    if not amount is None:
        for _ in range(amount):
            for channel in ctx.guild.text_channels:
              await channel.send(random.choice(MESSAGE_CONTENTS))
    else:
        while True:
            for channel in ctx.guild.text_channels: 
              await channel.send(random.choice(MESSAGE_CONTENTS))


@client.command(pass_contex=True)
async def chat(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)



@client.command(pass_context=True)
async def banall(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    print ("Action Completed: banall")

@client.command()
async def channels(ctx, amount=500):
    await ctx.message.delete()
    guild = ctx.message.guild 
    for i in range(amount):
        await guild.create_text_channel(random.choice(CHANNEL_NAMES))

@client.command()
async def stream(ctx, *, message):
    await ctx.message.delete()
    stream = discord.Streaming(
        name=message,
        url=stream_url, 
    )
    await client.change_presence(activity=stream) 

@client.command(pass_context=True)
async def kickall(ctx):
    guild = ctx.message.guild
    for member in list(ctx.message.guild.members):
        try:    
            await guild.kick(member)
            print ("User " + member.name + " has been kicked")
        except:
            pass
    print ("Action Completed: kickall")



@client.command(pass_contex=True)
async def whois(ctx, member: discord.Member):
  await ctx.message.delete()
  member = ctx.author if not member else member
  roles = [role for role in member.roles]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
  
  embed.set_author(name=f"{member} - info")
  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  embed.add_field(name="User ID", value=member.id)
  embed.add_field(name="Nickname", value=member.display_name)

  embed.add_field(name="Creation Date", value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))
  embed.add_field(name="Guild Join Date", value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Highest Role", value=member.top_role.mention)

  embed.add_field(name="Bot?", value=member.bot)

  await ctx.send(embed=embed)



@client.command()
async def droles(ctx):
  await ctx.message.delete()
  for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")

@client.command(pass_context=True)
async def admin(ctx):
    guild = ctx.message.guild
    perms = discord.Permissions(8)
    await guild.create_role(name='$', permissions=perms)
    member = ctx.message.author
    role = discord.utils.get(guild.roles, name="$")
    await member.add_roles(role)
    print ("Admin Given!")


@client.command(pass_context=True)
async def ping(ctx):
	channel = ctx.message.channel
	t1 = time.perf_counter()
	await channel.trigger_typing()
	t2 = time.perf_counter()
	embed=discord.Embed(title=None, description='Ping: {}'.format(round((t2-t1)*1000)), color=0x2874A6)
	await channel.send(embed=embed)

@client.command(pass_contex=True)
async def embed(ctx, *, text):
  await ctx.message.delete()
  await ctx.send(embed = discord.Embed(description = text))
  embed = discord.Embed(color = discord.Color.from_rgb(147,112,219), timestamp=ctx.message.created_at)

@client.command(pass_context=True)
async def dm(ctx, *, message):
  await ctx.message.delete()
  for user in ctx.guild.members:
    try:
       await user.send(message)
       print(f"{user.name} has recieved the message.")
    except:
      print(f"{user.name} has NOT recieved the message.")
      print("Action Completed: dm")

@client.command(pass_centex=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@client.command(pass_centex=True)
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.message.delete()

@client.command(pass_contex=True)
async def serverinfo(ctx, guild: discord.Guild = None):
  guild = ctx.guild if not guild else guild
  embed = discord.Embed(title=f"Server info about {guild}", description="sykoh SelfBot", timestamp = ctx.message.created_at, color=discord.Color.green())
  embed.set_thumbnail(url=guild.icon_url)
  embed.add_field(name="**Description:**", value=guild.description, inline=False)
  embed.add_field(name="**Channel count:**", value=len(guild.channels), inline=False)
  embed.add_field(name="**Role count:**", value=len(guild.roles), inline=False)
  embed.add_field(name="**Booster count:**", value=guild.premium_subscription_count, inline=False)
  embed.add_field(name="**Server created at:**", value=guild.created_at, inline=False)
  embed.add_field(name="**Max Emoji:**", value=guild.emoji_limit, inline=False)
  embed.add_field(name="**Owner**:", value=guild.owner, inline=False)
  embed.set_footer(text=f"Command sent by {ctx.author}", icon_url=ctx.author.avatar_url)
  
  await ctx.send(embed=embed)
  await ctx.message.delete()

@client.command()
async def spam(ctx, amount:int, *, msg:str):
    while amount > 0:
        await ctx.send(msg)
        amount -= 1


client.run(token, bot=False)
