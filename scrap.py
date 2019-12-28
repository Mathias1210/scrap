from pytube import YouTube
yt = YouTube("https://www.youtube.com/watch?v=kGTT1QbWwlk")
yt = yt.get('mp4',720p')
yt.download('C:\Users\mhg\Documents\Py'