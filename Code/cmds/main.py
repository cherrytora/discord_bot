import os
import discord
from discord.ext import commands
import random

## 把剛剛在get_start.py中ping、pic和r_pict三個指令搬過來
class Main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def ping(self,ctx):
        await ctx.send(f'{round(self.bot.latency*1000,2)} (ms)')
    
    # 傳送本機端圖片
    @commands.command()
    async def pict(self,ctx):
        pic_path = discord.File('../image/channel_msg.png')
        await ctx.send(file = pic_path)

    # 隨機傳送本機圖片
    @commands.command()
    async def r_pict(self,ctx):
        pic_files = os.listdir('../image')
        r_pic = random.choice(pic_files)
        pic_path = discord.File(f'../image/{r_pic}')
        await ctx.send(file = pic_path)

    @commands.Cog.listener()
    async def on_row_reaction_add(self,payload):
        print(payload.emoji)
        print(payload.member)

    @commands.command()
    async def cmdA(self,ctx, num:int):
        await ctx.send(num)

    # @cmdA.error
    # async def cmdA_error(self, ctx, error):
    #     await ctx.send(error)

async def setup(bot):
    await bot.add_cog(Main(bot))