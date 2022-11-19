import discord
from discord.ext import commands
from youtube_dl import YoutubeDL
import pandas as pd
import random
import asyncio
from discord.ui import Button, View
'''
1. 用youtube_dl找出audio連結，連結voice channel播放
2. 設定頻道限定和特定人員播放 & 加入 why don't you stay!!
3. 寫成embed & 播放按鈕 
4. 下一首按鈕
5. 隨機播放按鈕
'''

# 讀取利用Youtube API抓下來的播放清單資訊
mv = pd.read_csv("../database/mv_list.csv")

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mv_l = []

    '''
    先設定空的list，play的時候用load_list去把東西裝到list中（每次?rplay的時候都重新load一次)
    stop的時候把list清空，不然stop之後還是會重新播放
    '''
    def load_list(self):
    # 把why don't you stay加入play list
        mv_l = mv["V_ids"].tolist()
        mv_l.append("6ZF8RXvV9sQ")
        return mv_l

    '''
    設定next函數，塞在after中，讓他下一首繼續播放，不然播完這首歌就會停止
    播放的歌曲隨機選取
    '''
    def next(self, ctx, play_list):
        # 隨機產生0~9的數（因為目前list裡有10首歌）
        num = random.randint(0,len(play_list)-1)
        # YoutubeDL設定
        YDL_OPTIONS = {'format': 'bestaudio'}
        url = f'https://www.youtube.com/watch?v={play_list[num]}'
        info = YoutubeDL(YDL_OPTIONS).extract_info(url, download=False)
        # url是audio link的key
        ctx.voice_client.play(discord.FFmpegPCMAudio(info['url']), after = lambda e: self.next(ctx, play_list))
        # ctx.send一定要await，所以要用asyncio來啟動他
        asyncio.run_coroutine_threadsafe(ctx.send(f'正在播放 📣 {info["title"]} 📣'),self.bot.loop)  

    # 讓機器人加入語音頻道
    @commands.command()
    async def join(self,ctx):
        channel = ctx.author.voice.channel
        await channel.connect()
    
    # 機器人離開語音頻道
    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

    # 停止播放
    @commands.command()
    async def stop(self, ctx):
        self.mv_l.clear()
        ctx.voice_client.stop()
        await ctx.send('Music Stop')

    # 開始隨機播放
    @commands.command()
    async def rplay(self,ctx):
        if ctx.channel.name == "test_1": # 設定頻道在test_1才可以有播音樂的功能
            self.mv_l = self.load_list()
            self.next(ctx, self.mv_l)
        else:
            await ctx.send('在test_1頻道才可以播音樂喔～')
        '''
        ctx.guild:str => 伺服器名稱
        ctx.channel.name:str => 頻道名稱 ctx.channel不是str喔！但我也不知道實際的型態是什麼，總之要加上name才會是True
        # info回傳一個字典，keys如下
        dict_keys(['id', 'title', 'formats', 'thumbnails', 'description', 'upload_date', 'uploader', 
            'uploader_id', 'uploader_url', 'channel_id', 'channel_url', 'duration', 'view_count', 'average_rating', 
            'age_limit', 'webpage_url', 'categories', 'tags', 'is_live', 'subtitles', 'channel', 'extractor', 
            'webpage_url_basename', 'extractor_key', 'playlist', 'playlist_index', 'thumbnail', 'display_id', 
            'requested_subtitles', 'asr', 'filesize', 'format_id', 'format_note', 'fps', 'height', 'quality', 'tbr', 
            'url', 'width', 'ext', 'vcodec', 'acodec', 'abr', 'downloader_options', 'container', 'format', 'protocol', 
            'http_headers'])
        '''

async def setup(bot):
   await bot.add_cog(Music(bot))


