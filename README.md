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

### Intents

### 功能設定 
#### 1. Initial
```python
async def on_ready():
    print('目前登入身份：', bot.user)
# 也可以用 on_connect()
```
整個code的最下面記得要把bot啟動喔！
```python
bot.run('Bot Token') 
```
#### 2. 成員加入/離開 [CODE](get_start.py)
- [Discord API members](https://discordpy.readthedocs.io/en/latest/api.html?highlight=on_ready#members)
```python

```


- 先看terminal
![](image/terminal_msg.png)
- 回到頻道去看Bot有沒有說話
![](image/channel_msg.png)

這樣就是成功了！

#### 3. 鸚鵡機器人

#### 4. 傳送圖片

#### 5. ......



