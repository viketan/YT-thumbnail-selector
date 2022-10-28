import subprocess
from googleapiclient.discovery import build
import pandas as pd


def get_video_details(youtube, video_ids):
    all_video_stats = []

    for i in range(0, len(video_ids), 50):
        request = youtube.videos().list(
            part='snippet,statistics',
            id=','.join(video_ids[i:i+50]))
        response = request.execute()
        for video in response['items']:
            video_stats = dict(
                Title=video['snippet']['title'],
                Published_date=video['snippet']['publishedAt'],
                Views=video['statistics']['viewCount'],
                Likes=video['statistics']['likeCount'],
                Comments=video['statistics']['commentCount']
            )
            all_video_stats.append(video_stats)

    return all_video_stats


print('[//]Input Text File is going to be opened. Please enter Video_IDs.')
subprocess.run(["notepad", "Video_IDs.txt"])
video_ids = []
f = open("Video_IDs.txt", "r")
for x in f:
    video_ids.append(str(x).strip())
f.close()

api_key = 'AIzaSyAn9gCI3iVSanYxTuVml9ahFr16FCIZimk'
youtube = build('youtube', 'v3', developerKey=api_key)
video_details = get_video_details(youtube, video_ids)

video_data = pd.DataFrame(video_details)
video_data['Published_date'] = pd.to_datetime(
    video_data['Published_date']).dt.date
video_data['Views'] = pd.to_numeric(video_data['Views'])
video_data['Likes'] = pd.to_numeric(video_data['Likes'])
video_data['Comments'] = pd.to_numeric(video_data['Comments'])
video_data.insert(loc=0, column='Video_ID', value=video_ids)
video_data.to_csv("video_stats.csv", index=False)
