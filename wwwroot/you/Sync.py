from Searcher import FindSong,SearchMany
from pytube import YouTube
import urllib.request
import eyed3,io
from eyed3.id3.frames import ImageFrame
from Tools import *

def SyncIcon(file_location,download_location,songName,tempId):
        
        mp3File = file_location
        icon = download_location+tempId+".jpg"
        print("Sync in progress..: "+file_location)
        link = FindSong(songName)
        yt = YouTube(link)
        print(yt.title)
        print("Downloading Icon...: "+str(yt.thumbnail_url))
        urllib.request.urlretrieve(yt.thumbnail_url, icon)

        print("Adding Thumbnail!!!...: "+mp3File+".mp3") 
        audiofile = eyed3.load(mp3File)
        audiofile.initTag(version=(2, 3, 0))  # version is important
        # Other data for demonstration purpose only (from docs)
        audiofile.tag.album_artist = "Various Artists"
        audiofile.tag.title = yt.title

        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(icon,'rb').read(), 'image/jpeg')

        audiofile.tag.save()
        print("Icon updated successfully!!!")
