import os

filedirectories=os.listdir()
termFiles=[]
for index in range(len(filedirectories)):
    if "token" in filedirectories[index].lower():
        termFiles.append(filedirectories[index])
#debSta
print("Got all other people's file's name:")
#debSta
print(termFiles)

myFileName="tok.txt" # Name your own file here.
                  # Warning: avoid iclude a substring: "term" 'cuz used as sentinel for other ppl's file
myfile=open(myFileName,"r")
outputFileStream=open("[Log1-A]statisticForPartA.txt","w")

myList=[]

for line in myfile:
    myList.append(line)
myfile.close()
#debSta
print("Got my own file opened and read")

outputFileStream.write("For PART A"+"*"*50+"\n")

for file_ in termFiles:
    pplFile=open(file_,"r")
    pplList=[]
    for line in pplFile:
        pplList.append(line)
    pplFile.close()
    
    #debSta
    print("in Line 29")

    different_items =  [item for item in myList if item not in pplList]
    
    # DebSta
    print("in Line 39")
    outputFileStream.write("-Compared file from: "+ file_+"")
    outputFileStream.write("\n-Shared items length:"+ str(len(myList)-len(pplList)))
    outputFileStream.write("\n-Difference in words: \n")
    for item in different_items:
        outputFileStream.write(item+"\n")
    outputFileStream.write("\n"+"*"+"-"*75+"*"+"\n")

outputFileStream.close()
