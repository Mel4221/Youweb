"""
Copyright (c) <2024> <Melquiceded Balbi Villanueva>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
import eyed3,io
import os
from eyed3.id3.frames import ImageFrame
from pathlib import Path


def PrintStatus(download_location,status,message):
        with open(download_location+"status.text", 'w', encoding="utf-8") as file:
                pass
        with open(download_location+"status.number", 'w', encoding="utf-8") as file:
                pass
        print(message.encode("utf-8"))
        text_status = open(download_location+"status.text","w",encoding="utf-8")
        number_status = open(download_location+"status.number","w",encoding="utf-8")
        text_status.write(message)
        number_status.write(status)
        text_status.close()
        number_status.close()


def HasIcon(song):
        try:
                m = eyed3.load(os.path.normpath(song))
                l = len(m.tag.images)
                if l == 0:
                        return False
                else:
                        return True
        except:
                return False



def GetSongIcon(song,download_location,tempId):
        song = Path(song).read_text()
        icon = download_location+tempId+".png"
        if HasIcon(song) == False:
                print("Failed no icon..: "+song)
                return
        m = eyed3.load(os.path.normpath((song)))
        img = io.BytesIO(m.tag.images[0].image_data)   
        #print(img)
        #print(m.tag.images[0].mime_type)
        with open(icon, 'wb') as file:
                file.write(img.getvalue())
                print("Icon Saved..: "+icon)
                return   
  




def Status(current,goal):
        return str(round(float(current/goal)*100))
        