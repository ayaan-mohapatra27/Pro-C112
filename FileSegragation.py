import os
import shutil
source="C:/Users/ayaan/Downloads"
destination="C:/Users/ayaan/OneDrive/Documents/DownloadedFiles"
fileList=os.listdir(source)
#print(fileList)
for i in fileList:
    root,ext=os.path.splitext(i)
    #print(root)
    #print(ext)
    if(ext==""):
        continue
    if(ext in [".gif", ".png", ".jpg", ".webp", ".jfif"]):
        print("Hello")
        path1=source+"/"+i
        path2=destination+"/"+"ImageFiles"
        path3=path2 + "/" + i
        if(os.path.exists(path2)):
            print("Moving")
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)
    
    if(ext in [".mp3", ".mp4"]):
        path1=source+"/"+i
        path2=destination+"/"+"MediaFiles"
        path3=path2+ "/" + i
        if(os.path.exists(path2)):
            print("Moving")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)
    if(ext in [".zip"]):
        path1=source+"/"+i
        path2=destination+"/"+"ZippedFiles"
        path3=path2+ "/" + i
        if(os.path.exists(path2)):
            print("Moving")
            shutil.move(path1,path3)
        else: 
            os.makedirs(path2)
            print("Moving")
            shutil.move(path1,path3)