from discord.ext import commands
from dotenv import load_dotenv
import os
# Load .env
load_dotenv()

class Event(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Reaction ready.")

    # @commands.Cog.listener()
    # async def on_reaction_add(self, reaction, user):
    #    print(reaction)
    #    print(user)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # print(payload)
        # print(payload.member)
        # 判斷新增的貼圖 == 指定的貼圖 => 給他對應的Role（身份組）
        if payload.emoji.name == '👀':
            guild = self.bot.get_guild(payload.guild_id) # 伺服器 = bot(取得目前所在之伺服器id)
            role = guild.get_role(int(os.getenv('role_id'))) # 身份組 = 伺服器.身份組id(身份組id直接去身份組複製)
            await payload.member.add_roles(role) # 將成員加入身份組

async def setup(bot):
    await bot.add_cog(Event(bot))