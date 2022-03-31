# !/usr/bin/python

#Source of Code (before modifications to walking through directories): TutorialsPoint - tutorialspoint.com/python/os_walk.htm

#Source of Code (for getting date/time): programiz.com/python-programming/datetime/current-datetime 

import hashlib
import os
from datetime import date
today = date.today()

def storeData(filename):
    hash = hashlib.sha256(filename.encode())
    time = today.strftime("%b-%d-%Y")
    data = []
    data = [filename, data, time]

    file = open("record.csv", "a+")
    file.write(str(filename) +"," + str(data) + "," + str(time) + "\n")
    file.close()
    
    return

def getData():
    file = open("record.csv", "r")
    csvData = file.read(-1)
    csvDataList = csvData.split(",")
    return csvDataList
    
oldRecord = getData()

for root, dirs, files in os.walk("/", topdown=False):

        
    for name in dirs:
        if("/dev" in os.path.join(root,name)):
            break
        if("/proc" in os.path.join(root,name)):
            break
        if("/run" in os.path.join(root,name)):
            break
        if("/sys" in os.path.join(root,name)):
            break
        if("/tmp" in os.path.join(root,name)):
            break
        if("/var/lib" in os.path.join(root,name)):
            break
        if("/var/run" in os.path.join(root,name)):
            break
        
        storeData(os.path.join(root, name))

    for name in files:
        if("/dev" == os.path.join(root, name)[0:4]):
            break
        if("/proc" in os.path.join(root,name)[0:5]):
            break
        if("/run" in os.path.join(root,name)[0:4]):
            break
        if("/sys" in os.path.join(root,name)[0:4]):
            break
        if("tmp" in os.path.join(root,name)[0:4]):
            break
        if("/var/lib" in os.path.join(root,name)[0:8]):
            break
        if("/var/run" in os.path.join(root,name)[0:8]):
            break

        storeData(os.path.join(root, name))

#Get new data
newRecord = getData()
for oldHash in oldRecord:
    for newHash in newRecord:
        if(oldHash == newHash):
            newRecord.pop(oldHash)
            oldRecord.pop(oldHash)

#At this point, the newRecord contains all the new files and oldRecord contains all the missing files.

#Display stats to users.
print("New/Modified files:\n")
for x in newRecord:
    print(str(x[0]))
print("\nOld Missing Files:\n")
for y in oldRecord:
    print(str(y[0]))
