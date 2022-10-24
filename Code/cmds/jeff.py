from discord.ext import commands
import os 
from dotenv import load_dotenv
import discord

# Load .env
load_dotenv()

## 把剛剛在get_start.py中url_pict和Jeff兩個指令搬過來
class Jeff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 傳送網路圖片
    @commands.command()
    async def url_pict(self, ctx):
        pic_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ090g9KzhdPZifbHKyKMRUARuaAbrA753IPg&usqp=CAU'
        await ctx.send(pic_url)
    
    @commands.command()
    async def play_list(self, ctx):
        embed=discord.Embed(title="Jeff Satur channel", url="https://www.youtube.com/channel/UCSFWkjQRmSJoz9QQ4lkwlDA", color=0x0eacfb)
        embed.set_author(name="Jeff Satur", url="https://www.youtube.com/channel/UCSFWkjQRmSJoz9QQ4lkwlDA", icon_url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGQucI0UakUD4S14jACm42rQXg191f7RIG7A&usqp=CAU")
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGQucI0UakUD4S14jACm42rQXg191f7RIG7A&usqp=CAU")
        for i, j in zip(["Hide", "Loop", "Why", ],["Jeff Satur - แค่เงา (Hide)【Official Music Video】", "Jeff Satur - วันนี้คือพรุ่งนี้ของเมื่อวาน (Loop)【Official Music Video】", "Jeff Satur - Why Don't You Stay (WorldTour Ver.)[Official MV]"]):
            embed.add_field(name=f'輸入 ?s {i}', value=j, inline=False)
        await ctx.send(embed=embed)

    @commands.group()
    async def s(self,ctx):
       pass

    @s.command()
    async def Hide(self,ctx):
        embed=discord.Embed(title="Jeff Satur - แค่เงา (Hide)【Official Music Video】", url="https://www.youtube.com/watch?v=k9aI7dHj8GM", color=0x0eacfb)
        embed.set_thumbnail(url="https://i.ytimg.com/vi/k9aI7dHj8GM/sddefault.jpg")
        await ctx.send(embed=embed)
    
    @s.command()
    async def Loop(self,ctx):
        embed=discord.Embed(title="Jeff Satur - วันนี้คือพรุ่งนี้ของเมื่อวาน (Loop)【Official Music Video】", url="https://www.youtube.com/watch?v=AfeEOrQHBAo", color=0x0eacfb)
        embed.set_thumbnail(url="https://i.ytimg.com/vi/k9aI7dHj8GM/sddefault.jpg")
        await ctx.send(embed=embed)
    
    @s.command()
    async def Why(self,ctx):
        embed=discord.Embed(title="Jeff Satur - Why Don't You Stay (WorldTour Ver.)[Official MV]", url="https://youtu.be/6ZF8RXvV9sQ", color=0x0eacfb)
        embed.set_thumbnail(url="https://i.ytimg.com/vi/6ZF8RXvV9sQ/sddefault.jpg")
        await ctx.send(embed=embed)
        
    # # 來建立一個Jeff播放清單，讓使用者可以自行選擇歌曲
    # # 用youtube api去更新他的播放清單ＸＤ

async def setup(bot):
   await bot.add_cog(Jeff(bot))