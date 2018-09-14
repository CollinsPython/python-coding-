#displays only words that ends with ".exe" from a file.txt
#By Collins  ===> uses python 3.5
#the file was placed in thesame working directory as python
print('Please Enter your filename') 
fileName = input('Your Filename: ')  #prompt users for filename
with open(fileName) as fileRead:  #open the file and read
    for line in fileRead:  #search for lines in the file
        for word in line.split(): #search for words in the line and cut out white spaces
            if ".exe" in word: # then search for .exe in the words 
                print(word)  #print out words with only ".exe"
