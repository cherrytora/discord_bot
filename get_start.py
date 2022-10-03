from dotenv import load_dotenv
import os
import discord
from discord.ext import commands

# Load .env
load_dotenv()

# Initail Bot ## command_prefix 呼叫bot的時候要用的特殊字串
# Intents中記錄了對應的事件和啟用的緩存類型，訂閱特定事件
'''
## default
intents = discord.Intents.default()
intents.typing = False
intents.preence = False
intents.member要另外設定啟用

## 自行設定
intents = discord.Intents(message = True, guild = True)
if you want reaction events enaable the following:
intents.reaction = True
'''
intents=discord.Intents.all()

bot = commands.Bot(command_prefix="?", intents=intents)

# Bot功能設置  ##調用 event 函式庫
@bot.event
#當機器人完成啟動時
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

bot.run(os.getenv('bot_token')) 
