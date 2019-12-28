import os
from pytube import YouTube
link=input('Paste link here:')
dest = (r'C:\Users\mhg\videos')
os.chdir(dest)
YouTube(link).streams.first().download(r'C:\Users\mhg\Documents')