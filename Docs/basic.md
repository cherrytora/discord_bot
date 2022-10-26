# Members & Command

### 參考資料
1. [Discord API members](https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#members)
2. [rixinsc Giuhub](https://github.com/rixinsc/Libereus)
3. [Youtube video 1](https://youtu.be/rFJoLrVlEHY)
4. [Youtube video 2](https://youtu.be/P0a7o5hK_Ig)

> 完整的[CODE](../Code/get_start.py)在這邊
> 小提醒：在Bot中輸入指令help可以看目前有哪些funciton喔！

## event - 成員加入/離開 
- 這邊使用兩個function，Members還有其他的功能，需要的人可以去上面Discord API members的連結看喔！
    1. `on_member_join` 當有成員加入的時候歡迎他
    2. `on_member_remove` 當有成員退出的時候跟他說掰掰
- 去頻道按右鍵 => 複製ID，就可以設定channel ID，讓機器人傳訊息到特定的channel\
<img src="../image/copy_channel_ID.png" alt="Cover" width="50%"/>

```python
# get_start.py

@bot.event ##調用 event 函式庫
# 成員加入時
async def on_member_join(member):
    # member參數會去讀取跟member有關的訊息
    channel = bot.get_channel(1026139400796639297)#這裡放剛剛複製的channel ID
    print(f'{member} JOIN!') # 在terminal印出歡迎訊息
    await channel.send(f'{member} JOIN!') # 在Discord channel中送出歡迎訊息
```
- terminal中的訊息
<img src="../image/terminal_msg.png" alt="Cover" width="50%"/>
- 到頻道去看有沒有成功讓Bot說話
<img src="../image/channel_msg.png" alt="Cover" width="50%"/>

## command - ping
- ctx是什麼？ctx指的是context，包含[發話者, 發話者id, 所在伺服器, 所在頻道]等內容，讓機器人知道是誰、在哪裡說這個訊息，然後機器人該回應到哪裡(哪個伺服器哪個頻道)。所以如果用這個就不用像上面一樣指定頻道囉！
- 寫command一定會用到ctx喔！
- function的名稱就是我們在bot中要下的指令，不要忘了指令前面要加上前面寫的特殊字串
```python
# 指令 command
@bot.command()
async def ping(ctx):
    # 1000ms = 1s，把延遲時間改成兩個小數點的毫秒
    await ctx.send(f'{round(bot.latency*1000,2)} (ms)')
    #bot.latency指的是延遲時間
```
- 在#一般頻道中的機器人回覆\
<img src="../image/command_ping1.png" alt="Cover" width="50%"/>

- 轉到#test_1頻道中，機器人也會自動回覆在#test_1中喔！\
<img src="../image/command_ping2.png" alt="Cover" width="50%"/>

## command - 傳送圖片
傳送圖片分成兩種，分別是傳送本機圖片和網路圖片
1. 傳送本機圖片：傳送本機圖片寫了傳送固定檔案，和隨機選取資料夾中檔案送出的方式，詳細的code直接在py檔中看喔！
這邊要注意的是記得要告訴discord說要傳送是檔案而不是一串文字
```python
    pic_path = discord.File('../image/channel_msg.png')
    await ctx.send(file = pic_path)
```
- 到頻道中試試看傳送圖片的指令\
<img src="../image/send_pic.png" alt="Cover" width="50%"/>

- 再看看隨機傳送圖片的功能，相同的"?r_pic"指令下，傳送了不同的圖片\
<img src="../image/send_r_pic.png" alt="Cover" width="50%"/>

2. 傳送網路圖片：這邊直接google了最近超級喜歡的歌手Jeff Satur的照片網址貼在code中，他的聲音真的超～好聽，歌曲的風格我也很喜歡～私心推薦～哈哈哈！discord可以自己辨識網址傳送圖片，所以send的部分就跟文字訊息一樣就可以囉！
<img src="../image/send_url_pic.png" alt="Cover" width="50%"/>

3. 傳送網址：到這邊我突然覺得既然圖片的網址可以辨識，那Youtube的也可以吧！所以我就加上了Jeff的一首歌的Youtube網址，果然是可以辨識的，點播放還可以直接播放～好方便啊！！！ＸＤＤＤＤ\
<img src="../image/send_y_url.png" alt="Cover" width="50%"/>

Back to [README](../README.md)