# basic music voice channel bot

import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv("config/.env")
bot_token = os.getenv("BOT_TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    ctx.voice_client.play(discord.FFmpegPCMAudio("radio/music/cow.mp3"))

bot.run(bot_token)