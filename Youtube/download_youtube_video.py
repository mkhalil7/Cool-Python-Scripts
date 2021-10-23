import youtube_dl
def run():
    video_url = "https://www.youtube.com/watch?v=k-VcA7C6meg"
    video_info = youtube_dl.YoutubeDL().extract_info(
        url = video_url,download=False
    )
    options={
        'format':'best',
    }

    with youtube_dl.YoutubeDL(options) as ydl:
        ydl.download([video_info['webpage_url']])

    print("Download complete... ")

if __name__=='__main__':
    run()
