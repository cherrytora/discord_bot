# Reaction & Exception & Embeds & Botton

### Reaction & Exception的參考資料
1. [【Proladon】Code a discord bot](https://youtu.be/vlqGTZRIefY)
2. [makupi github(Reaction)](https://gist.github.com/makupi/c508c9d33bb01dcc04e57d1a93c23ae1)
> Button 的三種做法
3. [discord button 1](https://youtu.be/f-TK7EcWbUY)
4. [discord button 2](https://youtu.be/82d9s8D6XE4)
5. [discord button 3](https://youtu.be/kNUuYEWGOxA)
6. [discord development docs](https://discord.com/developers/docs/interactions/message-components#buttons)
7. [youtube api 教學](https://medium.com/%E5%BD%BC%E5%BE%97%E6%BD%98%E7%9A%84%E8%A9%A6%E7%85%89-%E5%8B%87%E8%80%85%E7%9A%84-100-%E9%81%93-swift-ios-app-%E8%AC%8E%E9%A1%8C/101-%E4%BD%BF%E7%94%A8-youtube-data-api-%E6%8A%93%E5%8F%96%E6%9C%89%E8%B6%A3%E7%9A%84-youtuber-%E5%BD%B1%E7%89%87-mv-d05c3a0c70aa)
### Embeds的參考資料
1. [Setup Discord Message Embeds! (2022)](https://www.youtube.com/watch?v=wlMCDXf2b4E)
2. [discohook](https://discohook.org/)
3. [Discord Custom Embeds - Make Your Server Beautiful](https://www.youtube.com/watch?v=4j-zqrcVtJ8)

## Reaction & Exception
- 內容很簡單，說明直接寫在[Code](../Code/cmds/event.py)裡
### on_reaction_add 和 on_raw_reaction_add 的差別
- 在官方文件中關於on_reaction有兩種指令，要選擇哪一個就看使用情境：
    1. `on_reaction_add`當Bot關掉之後資料就會清空，再新增reaction就不會再有反應
    2. `on_raw_reaction_add`在Bot關掉之後也不會被清空，重啟Bot之後reaction還是會有反應

## Embeds & Botton
- Embeds的Code用[Embeds產生器](https://cog-creators.github.io/discord-embed-sandbox/)產出
- 其他的說明也直接寫在[Code](../Code/cmds/satur.py)裡
- 另外寫了一個用youtube api 把播放清單資訊存下來的[Code](../Code/jeff_list.py)，可以設定自動排程讓他固定時間更新！

結合Embeds和Botton可以做成這樣~

https://user-images.githubusercontent.com/45777647/201389899-34fe67f7-2d9b-4b36-a05c-cdebb800419f.mp4


然後我就把他做成Music Bot了～哈哈哈哈！

https://user-images.githubusercontent.com/45777647/202845325-f4cb28c2-18af-4903-8345-f25780b2ee46.mp4

