# project 3 ITS 5900 by Collins Ojo.  ===> uses python 3.5
#linux OS was used hence the file path
import os
directoryName = os.listdir(input("Directory Path: ")) #directory to examine
fileInput = input("file name: ") #prompt for a part of the file name e.g ".exe" or ".EXE"
for fileName in directoryName: #retrieve a listing of the files
    for word in fileName.split():
        if fileInput.lower() in word: #look for files that ends with a ".exe"
            print(word)
        if  fileInput.upper() in word: #look for files that ends with a ".EXE"
            print(word)
