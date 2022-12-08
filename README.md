# discord_bot

## Discord Bot 2.0 新手上路
從0開始打造自己的Discord Bot筆記

### 參考資料：
1. [機器人從0到1超詳細教學](https://hackmd.io/@kangjw/Discordpy%E6%A9%9F%E5%99%A8%E4%BA%BA%E5%BE%9E0%E5%88%B01%E8%B6%85%E8%A9%B3%E7%B4%B0%E6%95%99%E5%AD%B8)
2. [如何创建它并将其添加到服务器](https://appmaster.io/zh/blog/discord-bot-ru-he-chuang-jian-ta-bing-jiang-qi-tian-jia-dao-fu-wu-qi)
3. [event 函式庫 API 查詢](https://discordpy.readthedocs.io/en/latest/api.html#event-reference)
4. [discord.py 官方API](https://discordpy.readthedocs.io/en/latest/api.html)
5. [youtube play list](https://www.youtube.com/watch?v=rFJoLrVlEHY&list=PLSCgthA1Anif1w6mKM3O6xlBGGypXtrtN&index=5)
6. [discord github](https://github.com/discord/discord-api-docs)
7. [discordpy documentation](https://discordpy.readthedocs.io/en/latest/index.html#getting-started)

### 主題
1. [基本設定 & 基礎功能](Docs/basic.md):event（成員加入、離開等）和 command（傳送圖片等）的使用
2. [把基礎功能寫成cog形式 & 群組命令 => discord 2.0](./Docs/cogs_group.md) 
3. [連結錢包、讀取特定NFT properties加入特定頻道](./Docs/connectwallet.md)
4. [點選表情符號加入身份組 & 移除表情符號移除身份組 & 錯誤處理 ](./Code/cmds/event.py)
5. [Embeds & 按鈕連結設定](./Docs/reaction_button.md)
6. [音樂機器人](./Code/cmds/music.py)

### bot 
1. 啟動基礎的bot
`python basic_bot.py`
2. 啟動有一堆功能的bot
`python cogs_bot.py`
- 小提醒：使用reload的功能時，打?help的時候顯示的cogs都是class的名稱，但relaod的其實是python的檔名，而不是class的名稱，所以把檔名和class的名稱取一樣比較不會搞混。

### 目前建立的指令們 & Cogs
```python
# cogs
Jeff:
  play_list #顯示可以點選的youtube歌曲
  s    # 群組指令，加上可以播放的歌曲就會跳youtube連結     
  url_pict #傳送網路圖片
Main: 
  cmdA      
  pict #傳送本機端圖片 
  ping      
  r_pict # 隨機傳送本機圖片
Music:
  join # 把機器人加到語音頻道   
  leave # 叫機器人離開語音頻道
  rplay # 開始隨機播放 
  stop # 停止隨機播放
Satur:
  channel 
# 寫在cogs_bot裡的，不屬於cog的指令 
​No Category:
  help      Shows this message
  load # load 某個cog
  reload # reload 某個cog    
  unload  # unload 某個cog  
```

### NFT contract address
0x041d32E7612c2b6A4cEA5c5d9cCF1A9CC87fbbde


