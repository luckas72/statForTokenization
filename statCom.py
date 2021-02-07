import os

filedirectories=os.listdir()
termFiles=[]
for index in range(len(filedirectories)):
    if "term" in filedirectories[index].lower():
        termFiles.append(filedirectories[index])
#debSta
print("Got all other people's file's name:")
#debSta
print(termFiles)

myFileName="t.txt" # Name your own file here.
                  # Warning: avoid iclude a substring: "term" 'cuz used as sentinel for other ppl's file
myfile=open(myFileName,"r")
outputFileStream=open("[Log1]statisticForPartB.txt","w")
outputFileStream2=open("[Log2]frequencyDifferenceDetail.txt","w")

myDict={}

for line in myfile:
    lines=line.split()
    myDict[lines[0]]=lines[1]
myfile.close()
#debSta
print("Got my own file opened and read")

for file_ in termFiles:
    pplFile=open(file_,"r")
    pplDict={}
    for line in pplFile:
        lines=line.split()
        pplDict[lines[0]]=lines[1]
    pplFile.close()
    
    #debSta
    print("in Line 29")

    different_items = { k : pplDict[k] for k in set(pplDict) - set(myDict) }
    
    different_word_frequency={}
    for i in pplDict:
        if i in myDict:
            if int(pplDict[i]) != int(myDict[i]):
                different_word_frequency[i]=int(pplDict[i]) - int(myDict[i])
        else:
            different_word_frequency[i]=int(pplDict[i])
    
    # DebSta
    print("in Line 43")
    outputFileStream.write("-Compared file from: "+ file_+"")
    outputFileStream.write("\n-Shared items length:"+ str(200-len(different_items)))
    outputFileStream.write("\n-Difference in words: \n")
    for item in different_items:
        outputFileStream.write(item+"\n")
    outputFileStream.write("\n"+"*"+"-"*75+"*"+"\n")

    outputFileStream2.write("-Compared file from: "+ file_+"")
    outputFileStream2.write("\nFrequency difference:\n")
    for item in different_word_frequency:
        outputFileStream2.write(item+" "+str(different_word_frequency[item])+"\n")
    outputFileStream2.write("\n"+"*"+"-"*75+"*"+"\n")

outputFileStream.close()
outputFileStream2.close()
