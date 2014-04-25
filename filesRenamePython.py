import os
from os import rename, listdir

directory = "C:\\inetpub\\wwwroot\\XXX"
for filename in os.listdir(directory):
    path = os.path.join(directory, filename)
    target = os.path.join(directory, filename.replace(" ", "")+".midi")
    os.rename(path, target)
