from discord.ext import commands

## 把剛剛在get_start.py中url_pict和Jeff兩個指令搬過來，避免class名稱和function相同，所以把原本的Jeff指令改成song
class Jeff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    # 傳送網路圖片
    @commands.command()
    async def url_pict(self, ctx):
        pic_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ090g9KzhdPZifbHKyKMRUARuaAbrA753IPg&usqp=CAU'
        await ctx.send(pic_url)

    # 傳送Why don't you stay 歌曲 Youtube網址
    @commands.command()
    async def song(self, ctx):
        jeff_url = 'https://youtu.be/6ZF8RXvV9sQ'
        await ctx.send(jeff_url)

async def setup(bot):
   await bot.add_cog(Jeff(bot))