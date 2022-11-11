## 貼圖給予身份組 ＆ 處理指令發生的錯誤 (Error Handler)  
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load .env
load_dotenv()

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    '''
    貼圖給予身份組
    '''
    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Reaction ready.")
    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user):
    #    print(reaction)
    #    print(user)

    """
    on_reaction_add 和 on_raw_reaction_add 的差別
    on_reaction_add當Bot關掉之後資料就會清空，再新增reaction就不會有反應
    on_raw_reaction_add在Bot關掉之後也不會被清空，重啟Bot之後reaction還是會有反應
    """
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # print(payload)
        # print(payload.member)
        # 判斷新增的貼圖 == 指定的貼圖 => 給他對應的Role（身份組）
        if payload.emoji.name == '👀':
            # 這邊要注意payload.emoji == '👀' 的話會沒反應～因為payload.emoji的型態不是字串，所以要用payload.emoji.name才對喔！
            guild = self.bot.get_guild(payload.guild_id) # 伺服器 = bot(取得目前所在之伺服器id)
            role = guild.get_role(int(os.getenv('role_id'))) # 身份組 = 伺服器.身份組id(身份組id直接去身份組複製)=>型態int
            await payload.member.add_roles(role) # 將成員加入身份組

    '''
    例外處理
    '''
    ## 全域指令的錯誤處理
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        '''
        小知識：這邊的error就是一個instance喔～
        isinstance(object, type) 例如說判斷5是不是整數 => isinstance(5, int) => 會回傳True
        command errors 的型態這邊看
        https://discordpy.readthedocs.io/en/stable/ext/commands/api.html?highlight=command_error#discord.ext.commands.CommandError
        '''
        if isinstance(error, commands.errors.CommandNotFound): 
            '''
            去看Error是不是屬於discord中已經有定義的CommandNotFound error
            '''
            await ctx.send("沒有這個指令！")
        else:
            await ctx.send(error)

async def setup(bot):
    await bot.add_cog(Event(bot))