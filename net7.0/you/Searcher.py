"""
Copyright (c) <2024> <Melquiceded Balbi Villanueva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import sys
from pytube import Search
from pytube import YouTube
from Tools import PrintStatus,Status

# this finds the song's link using the name provided
searchData = ""

def SaveSearch(links,download_location,tempId):
    try:
        default = download_location+tempId
        with open(default+".links", 'w', encoding="utf-8") as file:
                pass
        with open(default+".icons", 'w', encoding="utf-8") as file:
                pass
        with open(default+".durations", 'w', encoding="utf-8") as file:
                pass
        with open(default+".titles", 'w', encoding="utf-8") as file:
                pass
        
        linksList = open(default+".links","a",encoding="utf-8")
        icons = open(default+".icons","a",encoding="utf-8")
        duration = open(default+".durations","a",encoding="utf-8")
        title = open(default+".titles","a",encoding="utf-8")
        
        #print(links)
        #print(download_location+" >> "+tempId)
        
        current = 0
        goal = len(links)
        
        for link in links:
            current = current+1
            print("Link Saved: "+link)
            
            yt = YouTube(link)

            linksList.write(link+"\n")
            icons.write(str(yt.thumbnail_url)+"\n")
            duration.write(str(yt.length)+"\n")
            title.write(yt.title+"\n")
            PrintStatus(download_location,Status(current,goal),"Getting icons and metadata..."+yt.title)
        linksList.close()
        icons.close()
        duration.close()
        title.close()
        print("Saved Search Location: "+download_location+tempId+".links")
    except Exception as e:
         print("There was an error while sayving the links..: "+str(e))


def SearchMany(song,download_location,tempId):
    try:
        links = []
        s  = Search(song.replace("_"," "))
        for link in s.results:
        #print(link)
                defaultLink = "https://www.youtube.com/watch?v="
                ida = str(link).index('=')+1
                idb = str(link).index('>')
                videoId = str(link)[ida:idb]
                video = defaultLink+videoId
                print("LINK: "+video)
                links.append(video)
        PrintStatus(download_location,"10","List of links Downloaded Sucessfully ["+str(len(s.results))+"] links Found!!!")
        SaveSearch(links,download_location,tempId)
        #print(links)
        sucess = open(download_location+tempId+".sucess","w",encoding="utf-8")
        sucess.write("List downloaded sucessfully!!!")
        sucess.close()
    except Exception as e:
        print(str(e))
        fail = open(download_location+tempId+".fail","w",encoding="utf-8")
        fail.write("There was an error while trying to collect the list: "+str(e))
        fail.close()



def FindSong(song):
    #try:
    songName = song     
    print("Finding Link for : "+songName) 
    if songName.find("http") >=0:
        songName = songName[songName.index('=')+1:len(songName)-1]
    #print("Finally: "+songName)
    
    s  = Search(songName)
    global MetaData
    youTubeLink = "https://www.youtube.com/watch?v="
    listOfLinks = str(s.results[0])
    ida = listOfLinks.index('=')+1
    idb = listOfLinks.index('>')
    firstVideoId = listOfLinks[ida:idb]
    video = youTubeLink+firstVideoId
    print("Link Founded : "+video)
    global searchData
    searchData = video
    #input()
    return video
"""
except:
    print("Something went wrong while finding the song pleas make sure that you are connected to the internet"); 
    print("NO INTERNET CONNECTION"); 
    return ""; 
"""

def GetDetails(song):
          
    try:
        songName = song     
        print("Finding Link for : "+songName) 
        if songName.find("http") >=0:
                    songName = songName[songName.index('=')+1:len(songName)-1]
        #print("Finally: "+songName)
        
        s  = Search(songName)
        global MetaData
        youTubeLink = "https://www.youtube.com/watch?v="
        listOfLinks = str(s.results[0])
        ida = listOfLinks.index('=')+1
        idb = listOfLinks.index('>')
        firstVideoId = listOfLinks[ida:idb]
        video = youTubeLink+firstVideoId
        print("Link Founded : "+video)
        global searchData
        searchData = video
        yt = YouTube(video)
            
        return [video,yt.title,yt.author,yt.length]
    except:
        print("NO INTERNET CONNECTION")
          
