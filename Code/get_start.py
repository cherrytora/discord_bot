from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load .env
load_dotenv()

# Initail Bot 
# Set Intents 
intents=discord.Intents.all()

# command_prefix 呼叫bot的時候要用的特殊字串
bot = commands.Bot(command_prefix="?", intents=intents)

# Bot功能設置  ##調用 event 函式庫
@bot.event
# 當機器人完成啟動時
# 也可以用 on_connect()
async def on_ready():
    print('目前登入身份：', bot.user)

@bot.event
# 成員加入時
async def on_member_join(member):
    channel = bot.get_channel(1026139400796639297)
    print(f'{member} JOIN!')
    await channel.send(f'{member} JOIN!')

@bot.event
# 成員離開時
async def on_member_remove(member):
    channel = bot.get_channel(1026139400796639297)
    print(f'{member} BYE!')
    await channel.send(f'{member} BYE!')

# 啟動Bot
bot.run(os.getenv('bot_token')) 
