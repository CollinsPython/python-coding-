# Project 1 
print("file Size in MB")   
fileSize = input()  #prompt for file size in MB
print("Transfer Speed in MB/s")
transferSpeed = input() #prompt for estimated transfer speed in MB/s
print("file transfer time in seconds is: ")
timeInSeconds = (8000000*fileSize)/(8000000*transferSpeed) #conversion from MB to bits
print(round(timeInSeconds, 2))   #Display file transfer in seconds to two decimal place
if timeInSeconds >= 60:  #if times takes longer than a minute
    print("time in minute: ")
    Add_Decimal = float(timeInSeconds) 
    print(round(Add_Decimal/60, 2)) #display time in minutes to 2 decimal place

