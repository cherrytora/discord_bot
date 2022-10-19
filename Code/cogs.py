from fileinput import filename
from dotenv import load_dotenv
import os
import discord
from discord.ext import commands
import asyncio


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

# 定義load unload reload 功能
@bot.command()
async def load(ctx, extension):
    await bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'Load {extension} done!')

@bot.command()
async def unload(ctx, extension):
    await bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'Unload {extension} done!')

@bot.command()
async def reload(ctx, extension):
    await bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f'Reload {extension} done!')

async def load_cogs():
# 把cmds中的檔案都load進來
    for fn in os.listdir('./cmds'):
        # 只選擇副檔名是.py的檔案
        if fn.endswith(".py"):
            # load 這些檔案（但是去掉".py"的字樣)
            await bot.load_extension(f'cmds.{fn[:-3]}')

async def main():
    await load_cogs()
    await bot.start(os.getenv('bot_token'))

if __name__ == '__main__':
    asyncio.run(main())



