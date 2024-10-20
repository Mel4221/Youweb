import moviepy.editor as mp
from pathlib import Path
from pytubefix import YouTube
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
from Searcher import *
from JMetadata import * 

def add(list,item):
        l = list
        if not any(existing_value == item for existing_value in l):
                l.append(item)
                print("Resolution added..: "+item)
                return l
        else:
                return l
def sort_resolutions(resolution_str):
    # Step 1: Parse the input string into a list
    resolutions = resolution_str.split(',')
    
    # Step 2: Define the resolution order, including more resolutions
    resolution_order = {
        '144p': 1,
        '240p': 2,
        '360p': 3,
        '480p': 4,
        '720p': 5,
        '1080p': 6,
        '1440p': 7,
        '2160p': 8
    }
    
    # Step 3: Sort the resolutions based on the predefined order
    sorted_resolutions = sorted(resolutions, key=lambda x: resolution_order.get(x, 0), reverse=True)
    
    # Step 4: Join the sorted list into a string, removing any empty strings
    sorted_resolutions_str = ','.join(resolution for resolution in sorted_resolutions if resolution)
    
    return sorted_resolutions_str


def T():
        link = "https://www.youtube.com/watch?v=77DpsYLurO0"
        temp_file = "temp.video"
        download_path = "~/Downloads/"

        yt = YouTube(link)#,use_oauth=True, allow_oauth_cache=True)
        filter = yt.streams.filter(type="video")
        resolutions = [] 
        resolutions_str = ""
        
        for item in filter:
                resolutions = add(resolutions,item.resolution)
        for resolution in resolutions:
                resolutions_str = resolutions_str+resolution+","
        
        resolutions_str = sort_resolutions(resolutions_str)
        meta = JMetadata("video.json")
        meta.write("title",yt.title)
        meta.write("description",yt.description)
        meta.write("length",yt.length)
        meta.write("video_url",link)
        meta.write("icon_url",yt.thumbnail_url)
        meta.write("resolutions",resolutions_str)
        meta.write("temp_file",temp_file)
        meta.write("download_path",download_path)
        meta.write("progress","0")
        meta.write("message","working...")
        meta.write("complete_status","0|1")# [0]: sucess [1]: failed

        """
        info.write(fileName+"\n")
                info.write(yt.title+"\n")
                info.write(str(yt.length)+"\n")
                info.write(str(yt.thumbnail_url)+"\n")
        """
        return 
        link = "https://www.youtube.com/watch?v=77DpsYLurO0"
        link = "https://www.youtube.com/watch?v=Jvnb0d_FDac"
        link = "https://www.youtube.com/watch?v=4xPnpE-dHHY"
        yt = YouTube(link,use_oauth=True, allow_oauth_cache=True)
        print(yt.streams)
        #print(yt.streams.filter().first())
        filter = yt.streams.filter().first().download()
        
        
        
        
        return
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