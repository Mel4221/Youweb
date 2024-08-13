"""
Copyright (c) <2024> <Melquiceded Balbi Villanueva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
from shelve import Shelf
from traceback import print_tb
from unittest import result
import shutil
import os 
from SongDownloader import DownloadSong
from VideoDownloader import DownloadVideo
from Searcher import *
from Tools import * 
 
'''
MP3
MP4_720P
MP4_1080P
'''
def CheckArgs(list):
    type = list[0]
    if type=="help" or type=="--help" or type=="-h":
    	print("[MP3] or [720p,480p...] [LINK] [DOWNLOAD_LOCATION] [TEMP_ID]")
    	return
    print(list) 
    print("Action: "+list[0])
    """TYPE LINK LOCATION ID"""
    link = list[1]
    download_location = list[2]
    tempId=list[3]
    if type=="SEARCH_MANY":
        SearchMany(link,download_location,tempId)
        return
    if type=="MP3":
        print("Downloading song: ")
        DownloadSong(link,download_location,tempId)
        return
    if type == "GET_ICON":
        GetSongIcon(link,download_location,tempId)
        return
    else:
        DownloadVideo(link,type,download_location,tempId)
        return

            

