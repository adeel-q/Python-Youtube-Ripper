from __future__ import unicode_literals
import youtube_dl
import os
from dl_link import downloadlinks
from shutil import copyfile

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}


with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	try:
		ydl.download(downloadlinks)
	except:
		print(" couldn't download one of them, copyhing anyway ");

curpath = os.getcwd()

# get the new mp3 files.
lss = [f for f in os.listdir(os.getcwd()) if f.endswith('.mp3')]
#copy new mp3 files to folder


#purge curpath
for f in lss:
	try:
		print("copying new file over{}",f)
		copyfile(f, curpath+'\\beats\\'+f)
		os.remove(f)
	except:
		print("couldn't remove file {}, doesn't exist?",f)
#end for