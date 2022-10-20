# Cogs => discord 2.0
- 小提醒：discord 2.0把cog的功能改成async了喔！有些教學是舊的版本，嘗試了之後發現舊版本已經不能再建立cog功能了～

[youtube api 教學](https://medium.com/%E5%BD%BC%E5%BE%97%E6%BD%98%E7%9A%84%E8%A9%A6%E7%85%89-%E5%8B%87%E8%80%85%E7%9A%84-100-%E9%81%93-swift-ios-app-%E8%AC%8E%E9%A1%8C/101-%E4%BD%BF%E7%94%A8-youtube-data-api-%E6%8A%93%E5%8F%96%E6%9C%89%E8%B6%A3%E7%9A%84-youtuber-%E5%BD%B1%E7%89%87-mv-d05c3a0c70aa)
[Embeds | Discord.py 2.0](https://www.youtube.com/watch?v=urLZoyLUDdE)
[Embeds code 生成器](https://cog-creators.github.io/discord-embed-sandbox/)
[群組＆子命令](https://youtu.be/NE4yG7e5zq0)



.....還在努力生內容中

run bot 改成這樣
```python
async def main():
    await load_cogs()
    await bot.start(os.getenv('bot_token'))

if __name__ == '__main__':
    asyncio.run(main())
```

Back to [README](../README.md)