from urllib.request import urlretrieve
import subprocess

print('[//]Input Text File is going to be opened. Please enter Video_IDs.')
subprocess.run(["notepad", "Video_IDs.txt"])
video_ids = []
f = open("Video_IDs.txt", "r")
for x in f:
    video_ids.append(str(x).strip())
f.close()


print("Downloading "+str(len(video_ids))+" thumbnails")
i = 1
for video in video_ids:
    url = 'https://img.youtube.com/vi/'+video+'\hqdefault.jpg'
    print("Thumbnail "+str(i)+" Downloading...")
    i = i + 1
    file_path = r'C:\Users\HW798MH\OneDrive - EY\Desktop\YT-thumbnail selector\Data' + \
        '\\'+video + '.jpg'
    urlretrieve(url, file_path)
