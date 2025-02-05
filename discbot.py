import discord
import discord.ext 
import commands
from discord import Interaction
from dotenv import load_dotenv, find_dotenv
import os
import asyncio

client = commands.Bot(command_prefix="$", intents= discord.intents.all())

@client.event
async def on_ready():
    print(f'{client.user.name} is ready')

async def client_startr():
    await client.start(TOKEN)