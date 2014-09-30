import os
from os import rename, listdir

directory = "C:\\Users\\zhuol\\Google Drive\\HP&&Code\\zhuoSong\\img"
index=1
for filename in os.listdir(directory):
	if filename.endswith(".jpg"):
		path = os.path.join(directory, filename)
		target = os.path.join(directory, "bg"+str(index)+".jpg")
		print target
		os.rename(path, target)
		index+=1
