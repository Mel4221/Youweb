"""
Copyright (c) <2024> <Melquiceded Balbi Villanueva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import moviepy.editor as mp
from pathlib import Path
#from pytube import YouTube
from pytubefix import YouTube
from VideoDownloader import remove_emoji
from pathvalidate import sanitize_filepath
from Metadata import CreateFileInfo
from Tools import PrintStatus
#REQUIRES INSTALATION BEFORE DEPLOYMENT

""" from FileReader import * """


DownloadDir = Path("downloads")
DownloadCount = 0
Completed = 0 
Fail = 0 
Attemps = 1

def DownloadSong(link,download_location,tempId):

       fileName = download_location+tempId+".mp4"
       fileInfo = fileName+".info"
       
       try:

              print("LINK: "+link)
              yt = YouTube(link,use_oauth=True, allow_oauth_cache=True)
              PrintStatus(download_location,"50","Downloading... "+yt.title)

              reg_filter = remove_emoji(sanitize_filepath(yt.title)+".mp3") #regex.sub(r'[^\w]', ' ',yt.title+".mp3")
              
              reg_filter = download_location+reg_filter
              
              print("Clean File Name: "+reg_filter)
              CreateFileInfo(yt,fileInfo,fileName)

              print("Temporal FileName: "+fileName)
              '''download_location = download_location + fileName'''
              print("Download Location: "+download_location)
              print("Download Started")
              
              
              filter = yt.streams.filter(file_extension='mp4').get_lowest_resolution().download(output_path=download_location, filename=fileName, filename_prefix="",
                     skip_existing=False, timeout=300000, max_retries=50)

              print("Comverting to mp3")
              print("File located: "+str(Path(fileName).is_file))
              PrintStatus(download_location,"95","Downloading... "+yt.title)

              mp3 = mp.VideoFileClip(fileName)
       
              print("Saiving Song As: "+reg_filter)
              
              mp3.audio.write_audiofile(Path(reg_filter))
              sucess = open(fileInfo+".sucess","a",encoding="utf-8")
              sucess.close()
       except Exception as e:
              fail = open(fileInfo+".fail","a",encoding="utf-8")
              fail.write(str(e))
              fail.close()

          
          

          
          
     
