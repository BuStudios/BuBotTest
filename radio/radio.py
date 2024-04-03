# basic music voice channel bot

import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv("config/.env") # load the bot token
bot_token = os.getenv("BOT_TOKEN")

bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.slash_command()
async def join(ctx): # ctx means context
    channel = ctx.author.voice.channel
    await channel.connect()
    ctx.voice_client.play(discord.FFmpegPCMAudio("radio/music/cow.mp3")) # use ffmpeg to play audio
    # if you don'nt have ffmpeg installed this will not work!

bot.run(bot_token)
