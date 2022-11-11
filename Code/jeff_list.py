from dotenv import load_dotenv
import os
import pandas as pd
import requests

# Load .env
load_dotenv()

# 從YOUTUBE播放清單的網址把播放清單的ID複製下來
mv = 'PLYiCUslCeCVoCCYEqvMQhi3PrHAV3jYCO'
cover = 'PLYiCUslCeCVpv5rg_hobqp8UkI8qvV13f'

# api_key去google申請，詳細的看參考資料中的教學喔
api_key = os.getenv('youtubeAPI')

# 寫一個function利用Youtube API傳入播放清單ID，把播放清單中的影片的資訊存下來
def j_info(playlist_id, API_KEY):
  # 抓取播放清單內影片資訊
  p_url = f'https://www.googleapis.com/youtube/v3/playlistItems?part=snippet,contentDetails,status&playlistId={playlist_id}&key={API_KEY}&maxResults=20'
  j_df = pd.DataFrame(columns=["V_ids","Counts","Title","Pic_URL"])
  play_list = requests.get(p_url).json()
  # 把影片ID存成list
  ids = [i['contentDetails']['videoId'] for i in play_list['items']]
  # 利用影片ID去找出每一個影片的觀看次數、標題和照片url，存到dataframe中
  for i in range(len(ids)):
    v_url=f'https://www.googleapis.com/youtube/v3/videos?id={ids[i]}&key={API_KEY}&part=snippet,contentDetails,statistics,status'
    j_video = requests.get(v_url).json()
    if len(j_video["items"]) > 0:
      viewCount = j_video["items"][0]["statistics"]["viewCount"]
      title = j_video["items"][0]["snippet"]['title']
      pic_url = j_video["items"][0]['snippet']['thumbnails']['medium']['url']
      j_df.loc[i] = [ids[i], viewCount, title, pic_url]
      j_df["Counts"] = j_df["Counts"].astype(int)
      j_df.sort_values(by = ["Counts"],ascending=False, inplace = True)
  return j_df

# 分別抓取mv和cover的影片資訊
mv_df = j_info(mv,api_key)
cover_df = j_info(cover,api_key)

# 資料很小所以直接存csv檔
mv_df.to_csv("../database/mv_list.csv", index=False)
cover_df.to_csv("../database/cover_list.csv", index=False)