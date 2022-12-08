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

# 指令 command
@bot.command()
async def ping(ctx):
    # 1000ms = 1s
    await ctx.send(f'{round(bot.latency*1000,2)} (ms)')
    #bot.latency指的是延遲時間

# 傳送本機端圖片
@bot.command()
async def pict(ctx):
    pic_path = discord.File('../image/channel_msg.png')
    await ctx.send(file = pic_path)

# 隨機傳送本機圖片
import random
pic_files = os.listdir('../image')
@bot.command()
async def r_pict(ctx):
    r_pic = random.choice(pic_files)
    pic_path = discord.File(f'../image/{r_pic}')
    await ctx.send(file = pic_path)

# 傳送網路圖片
pic_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ090g9KzhdPZifbHKyKMRUARuaAbrA753IPg&usqp=CAU'
@bot.command()
async def url_pict(ctx):
    await ctx.send(pic_url)

# 傳送Youtube網址ＸＤ
jeff_url = 'https://youtu.be/6ZF8RXvV9sQ'
@bot.command()
async def Jeff(ctx):
    await ctx.send(jeff_url)

# 啟動Bot
bot.run(os.getenv('bot_token')) 
