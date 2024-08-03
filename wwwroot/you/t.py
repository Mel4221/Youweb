import moviepy.editor as mp
from pathlib import Path
from pytube import YouTube
from VideoDownloader import remove_emoji
from pathvalidate import sanitize_filepath
from Metadata import CreateFileInfo
from Tools import *
import eyed3,io
from eyed3.id3.frames import ImageFrame
import urllib.request
import emoji
import ffmpeg
from Sync import SyncIcon



def T():
        print(str(HasIcon("test.mp3")))
        return
        SyncIcon("adele.mp3","Adele - Skyfall (Lyrics)","skyfall")
        return
        link = "https://www.youtube.com/watch?v=YQHsXMglC9A"
       
        download_location = ""
        fileName = "test"
        icon = fileName+".jpg"
        video = fileName+".mp4"
        audio = fileName+".audio"
        mp3_temp = fileName+"_temp"+".mp3"
        mp3File = fileName+".mp3"
       
        print("LINK: "+link)
        yt = YouTube(link) # or any other YouTube-link
        print(yt.title)
        """
        print(yt.metadata) 
        print(yt.metadata[0]['Song']) 
        print(yt.metadata[0]['Artist'])   
        print(yt.metadata[0]['Album']) 
        """
        
        print("Downloading Icon...: "+str(yt.thumbnail_url))
        urllib.request.urlretrieve(yt.thumbnail_url, icon)
        print("Downloading Video...: "+yt.title)
        yt.streams.filter(file_extension='mp4').get_lowest_resolution().download(output_path=download_location, filename=video, filename_prefix="",
        skip_existing=False, timeout=300000, max_retries=50)
        
        #some of this will be uncommented but mainly the PrintStatus
        #PrintStatus(download_location,"95","Binding Video and Audio...")
        #yt.streams.get_by_itag(22).download(output_path="/home/mel/Music/", filename="test.mp4", filename_prefix="",skip_existing=True, timeout=15, max_retries=5)
        """
        print("Binding Audio and Video...: "+yt.title)
        video_stream = ffmpeg.input(video)
        audio_stream = ffmpeg.input(audio)

        ffmpeg.output(audio_stream, video_stream,mp3_temp).run(overwrite_output=True)
        """
         
        print("Converting to mp3...: "+yt.title+".mp3") 
        mp3 = mp.VideoFileClip(video)
        mp3.audio.write_audiofile(Path(mp3File))

        print("Adding Thumbnail!!!...: "+mp3File+".mp3") 
        audiofile = eyed3.load(mp3File)
        audiofile.initTag(version=(2, 3, 0))  # version is important
        # Other data for demonstration purpose only (from docs)
        audiofile.tag.album_artist = "Various Artists"
        audiofile.tag.title = yt.title

        audiofile.tag.images.set(ImageFrame.FRONT_COVER, open(icon,'rb').read(), 'image/jpeg')

        audiofile.tag.save()
        print("Donwload completed Successfully!!!")
        """
        yt = YouTube(link) # or any other YouTube-link

        filter = yt.streams.filter(file_extension='mp4').get_lowest_resolution().download(output_path=download_location, filename=fileName, filename_prefix="",
        skip_existing=True, timeout=300000, max_retries=50)
        
        link = "https://www.youtube.com/watch?v=t7wIg8wfNzs"
        print("LINK: "+link)
        yt = YouTube(link) # or any other YouTube-link
        print(yt.streams.get_highest_resolution())
        #print(yt.streams.order_by('resolution').desc().first())
        """
T()