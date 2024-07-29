"""
Copyright (c) <2024> <Melquiceded Balbi Villanueva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import moviepy.editor as mp
import regex
from pathlib import Path
import os
import gc
from pytube import YouTube
from Searcher import *
import emoji
from Metadata import CreateFileInfo
import ffmpeg
from Tools import PrintStatus





Attemps = 0 
"""
def CreateFileInfo(yt,fileInfo,fileName):
          a = open(fileInfo,"a")
          a.write("KEY=VIDEO_FILE;\nVALUE="+fileName+";\n")
          a.write("KEY=VIDEO_TITLE;\nVALUE="+yt.title+";\n")
          a.write("KEY=VIDEO_LENGTH;\nVALUE="+str(yt.length)+";\n")
          a.write("KEY=VIDEO_DESCRIPTION;\nVALUE="+str(yt.description)+";\n")
          a.write("KEY=VIDEO_THUMBNAIL_URL;\nVALUE="+str(yt.thumbnail_url)+";\n")
          a.close()

"""



def remove_emoji(string):
    s = emoji.replace_emoji(string, replace="")
    if s.__contains__("/"):
            s = s.replace("/","")
    if s.__contains__("\""):
            s = s.replace("\\")
    return s 
    #return emoji.replace_emoji(string, replace='')

def DownloadVideo(videoLink,videoQuality,download_location,tempId):
        global Attemps
        #Clear()
        print("Downloading Video: "+videoLink)
        fileInfo = download_location+tempId+".mp4.info"

        #videoQuality = "1080p"
        try:
                yt = YouTube(videoLink)
                fileName = download_location+regex.sub(r'[^\w]', ' ',yt.title)+".mp4"
                audio = fileName+".audio"
                video = fileName+".video"
                #create a file that contains the info from the video
                CreateFileInfo(yt,fileInfo,fileName)
                
                if videoQuality=="":
                        videoQuality = "720"
                if videoQuality.find("p") == -1:
                        videoQuality = videoQuality+"p"
                
                PrintStatus(download_location,"50","Downloading... "+yt.title+" Attemp: "+str(Attemps)+" Video Quality: "+videoQuality)
                
                #filter = yt.streams.filter(resolution=videoQuality)#.first().download(output_path="downloads/videos/", filename=yt.title+".mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
                filter = yt.streams.filter(resolution=videoQuality,adaptive=True).first().download(output_path=download_location, filename=video, filename_prefix="",skip_existing=False, timeout=35, max_retries=10)
                
                PrintStatus(download_location,"75","The Video has been downloaded Sucessfully "+yt.title+" Downloading Audio...")  
                yt.streams.filter(only_audio=True).first().download(output_path=download_location, filename=audio, filename_prefix="",skip_existing=False, timeout=35, max_retries=10)
                
                PrintStatus(download_location,"95","Binding Video and Audio...")
                #yt.streams.get_by_itag(22).download(output_path="/home/mel/Music/", filename="test.mp4", filename_prefix="",skip_existing=True, timeout=15, max_retries=5)
                video_stream = ffmpeg.input(video)
                audio_stream = ffmpeg.input(audio)
                
                ffmpeg.output(audio_stream, video_stream,fileName).run(overwrite_output=True)
                
                PrintStatus(download_location,"100","File Location: "+fileName)
                #.get_lowest_resolution().download(output_path="downloads/videos/", filename="video.mp4", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
                sucess = open(fileInfo+".sucess","a",encoding="utf-8")
                sucess.close()
        except Exception as e:
                print(e)
                gc.collect()
                #global Attemps
                Attemps = Attemps + 1
                if Attemps == 1:
                        print("Attempting again due to an error...")
                        DownloadVideo(videoLink,"",download_location,tempId)
                        return
                if Attemps == 2:
                        print("Download Quality Set to Default '720p' Due to TOO MANY ATTEMPS")
                        print("Please try a lower Video Quality if the video keeps Attempting...")
                        DownloadVideo(videoLink,"720",download_location,tempId)
                        return
                if Attemps == 3:
                        print("Download Quality Set to Default '480p' Due to TOO MANY ATTEMPS")
                        print("Please try a lower Video Quality if the video keeps Attempting...")
                        DownloadVideo(videoLink,"480",download_location,tempId)
                        return
                if Attemps == 4:
                        print("Download Quality Set to Default '360p' Due to TOO MANY ATTEMPS")
                        print("Please try a lower Video Quality if the video keeps Attempting...")
                        DownloadVideo(videoLink,"360",download_location,tempId)
                        return
                if Attemps == 5:
                        print("Download Quality Set to Default '144p' Due to TOO MANY ATTEMPS")
                        print("Please try a lower Video Quality if the video keeps Attempting...")
                        DownloadVideo(videoLink,"144",download_location,tempId)
                        return
                fail = open(fileInfo+".fail","a",encoding="utf-8")
                fail.write(e.message)
                fail.close()
        return
                
        #<Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">,
        #().download(output_path="downloads/video/", filename="video", filename_prefix="",skip_existing=True, timeout=10000, max_retries=10)
      
