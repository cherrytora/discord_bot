from discord.ext import commands
import discord
from discord.ui import Button, View
import pandas as pd

# 讀取利用Youtube API抓下來的播放清單資訊
mv = pd.read_csv("../database/mv_list.csv", nrows=5)
cover = pd.read_csv("../database/cover_list.csv", nrows=5)

class Satur(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def channel(self, ctx):
        # embed 基本設定
        embed=discord.Embed(title="Jeff Satur's Youtube channel", url="https://www.youtube.com/channel/UCSFWkjQRmSJoz9QQ4lkwlDA", description="Artist under Wayfer Records, Warner Music Thailand.",color=0x0eacfb)
        embed.set_thumbnail(url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGQucI0UakUD4S14jACm42rQXg191f7RIG7A&usqp=CAU")
        # 設定按鈕，按鈕的形式可以參考discord的文件
        button1 = Button(label="Offical MVs", style=discord.ButtonStyle.primary)#, emoji="😍")
        button2 = Button(label="Cover Songs", style=discord.ButtonStyle.success)#, emoji="🥰")
        # 設定按下按鈕的反應
        button1.callback = self.b1_reaction
        button2.callback = self.b2_reaction
        # 把按鈕加入
        view = View()
        view.add_item(button1) 
        view.add_item(button2)
        # 傳送embed和按鈕
        await ctx.send(embed=embed,view=view)

    # 第一個按鈕點下去的反應
    async def b1_reaction(self, interaction: discord.Interaction):
        # embed 基本設定
        embed=discord.Embed(title="Jeff Satur's MV playlist", url="https://www.youtube.com/watch?v=k9aI7dHj8GM&list=PLYiCUslCeCVoCCYEqvMQhi3PrHAV3jYCO",description="Top 5 MVs", color=0x9121c4)
        embed.set_thumbnail(url=str(mv["Pic_URL"][0]))
        view = View()
        # 利用for迴圈去讀取播放清單資訊，照順序放到embed和設定按鈕
        for i in range(5):
            embed.add_field(name=f"Top{i+1}", value=mv["Title"][i], inline=False)
            button = Button(label=f"Top{i+1}", style=discord.ButtonStyle.primary, url=f'https://www.youtube.com/watch?v={mv["V_ids"][i]}')
            view.add_item(button)
        # 傳送embed和按鈕
        await interaction.response.send_message(embed = embed,view=view)

    # 第二個按鈕點下去的反應
    async def b2_reaction(self, interaction: discord.Interaction):
        # embed 基本設定
        embed=discord.Embed(title="Jeff Satur's Cover songs playlist", url="https://www.youtube.com/watch?v=cQBp4wGGrbo&list=PLYiCUslCeCVpv5rg_hobqp8UkI8qvV13f",description="Top 5 Cover Songs", color=0xffee38)
        embed.set_thumbnail(url=str(cover["Pic_URL"][0]))
        view = View()
        # 利用for迴圈去讀取播放清單資訊，照順序放到embed和設定按鈕
        for i in range(5):
            embed.add_field(name=f"Top{i+1}", value=cover["Title"][i], inline=False)
            button = Button(label=f"Top{i+1}", style=discord.ButtonStyle.primary, url=f'https://www.youtube.com/watch?v={cover["V_ids"][i]}')
            view.add_item(button)
        # 傳送embed和按鈕
        await interaction.response.send_message(embed = embed,view=view)

async def setup(bot):
   await bot.add_cog(Satur(bot))