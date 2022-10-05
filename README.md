# discord_bot

## Discord Bot 新手上路
從0開始打造自己的Discord Bot筆記

### 參考資料：
1. [機器人從0到1超詳細教學](https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8)
2. [如何创建它并将其添加到服务器](https://appmaster.io/zh/blog/discord-bot-ru-he-chuang-jian-ta-bing-jiang-qi-tian-jia-dao-fu-wu-qi)
3. [event 函式庫 API 查詢](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
4. [discord.py 官方API](https://discordpy.readthedocs.io/en/latest/api.html)
5. [youtube play list](https://www.youtube.com/watch?v=rFJoLrVlEHY&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=5)
6. [discord github](https://github.com/discord/discord-api-docs)
7. [discordpy documentation](https://discordpy.readthedocs.io/en/latest/index.html#getting-started)

### 設定
1. 到[discord developers](https://discord.com/developers/applications) New Application => create => 點選側邊欄 Bot => add Bot
2. 前往「OAuth2」， 在「SCOPES」中點選 bot，選擇權限後把下方連結複製到瀏覽器，就可以將機器人邀請進去你自己的伺服器！詳細的步驟[這邊](https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8))有
3. 新環境記得要安裝discord套件
```
python -m pip install -U discord.py
```
4. 要放連結bot的token，新增一個`.env`檔把token和未來可能會用到其他的敏感資訊收起來
5. Discord 在1.5版本針對安全性上進行了重大更新，所以上面的設定完之後還要再設定其他的東西，接下來才能順利進行！
    - discord developer中的Bot頁面把Privileged Gateway Intents下面的按鈕打開
    ![](image/Intents_setting.png)
    - 在discord的使用者設定（discord帳號，不是developers喔！） => 進階 => 開發者模式打開，這樣才能複製頻道ID
    ![](image/developer_mode.png)


下面還在努力填內容中.....

### 功能設定 
#### 1. Initial
- [discord.Intents API](https://discordpy.readthedocs.io/en/latest/api.html#discord.Intents)    
- Intents 可以理解成權限設定，一共有三個分類
```python
# 開啟所有的權限
intents = discord.Intents.all()

# 開啟預設的權限
# 預設的部分是除了presences、members和message_content以外的都有
intents = discord.Intents.default()

# 所有的權限都不開啟
intents = discord.Intents.none()
```
當然，也可以自行設定
```python
# 自行定義要開啟的權限
intents = discord.Intents(message = True, guild = True)
# 另外把reaction打開
intents.reaction = True
```
或是這樣
```python
# 或是在設定好的權限下做調整等等
intents = discord.Intents.default()
# 在default下，把typing和preence關起來
intents.typing = False
intents.preence = False
```  
- 設定完intents後就可以設定Bot了！
```python
# command_prefix是呼叫bot的時候要用的特殊字串
bot = commands.Bot(command_prefix="?", intents=intents)
```
接下來就要開始建置Bot的功能了！

#### 2. 成員加入/離開 [CODE](get_start.py)
- [Discord API members](https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#members)
這邊使用兩個function，Members還有其他的功能，需要的人可以去上面Discord API members的連結看喔！
    1. `on_member_join` 當有成員加入的時候歡迎他
    2. `on_member_remove` 當有成員退出的時候跟他說掰掰
- 去頻道按右鍵 => 複製ID，就可以設定channel ID，讓機器人傳訊息到特定的channel
![](image/copy_channel_ID.png)

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
![](image/terminal_msg.png)
- 到頻道去看有沒有成功讓Bot說話
![](image/channel_msg.png)

#### 3. 鸚鵡機器人

#### 4. 傳送圖片

#### 5. 連結錢包、讀取特定NFT properties加入特定頻道
https://collabland.freshdesk.com/support/home

#### 6. 還沒想到.....



#### Final Step
所有功能都建置好之後加上`bot.run('你的Bot Token')`去啟動寫好的Bot



