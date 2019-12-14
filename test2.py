import os
import sys
import random
import time
import datetime
pointer = 0
oList = []
tList = []
wrong = []
right = []
nRNums = []
resets = 0
lng = 0
flip = 0
def inText(arg3,arg2,arg1,arg4):
    print("Round "+str(arg3))
    print("Remaining: "+str(arg2)+" ("+str(round((arg2/arg1)*100,2))+"%)")
def check(index):
    global wrong
    global right
    global nRNums
    global resets
    global allOf
    global lng
    print(oList[index])
    ipt = str(input())
    if ipt != tList[index]:
        print(tList[index])
        nRNums.append(index)
        input()
        os.system('cls')
        if resets == 0:
            a2 = allOf-right[len(right)-1]
            a3 = allOf
        else:
            a2 = lng-right[len(right)-1]
            a3 = lng
        inText(resets+1,a2,a3,wrong[len(wrong)-1])
        check(index)
        wrong[len(wrong)-1] += 1
    else:
        right[len(wrong)-1] += 1

def rst():
    global resets
    global wrong
    global right
    global nRNums
    global lng
    print("Right: "+str(right[resets]))
    print("Wrong: "+str(wrong[resets]))
    unique = []
    tUn = 0
    for i in range(len(nRNums)):
        tUn = 0
        for l1 in range(len(unique)):
            if unique[l1] == nRNums[i]:
                tUn = 1
        if tUn != 1:
            unique.append(nRNums[i])
    print("Unique wrong: "+str(len(unique)))
    resets += 1
    wrong.append(0)
    right.append(0)
    print("Next round!")
    random.shuffle(nRNums)
    lng = len(nRNums)
    for i in range(lng):
        check(nRNums[0])
        nRNums.pop(0)
    if wrong[len(wrong)-1] != 0:
        rst()
    input()
if len(sys.argv) >= 2:
    fileRead = sys.argv[1]
else:
    fileRead = str(input("Input: "))
with open(fileRead, "r",encoding="utf-8") as f:
    file = []
    new = 0
    for line in f:
        file.append(line)
    for i in range(len(file)):
        file[i] = file[i].rstrip("\n")
i = 0
while i != len(file):
    oList.append(file[i])
    tList.append(file[i+1])
    i += 2
rNums = list(range(len(oList)))
random.shuffle(rNums)
#flipping
flip = int(input(oList[0]+"->"+tList[0]+". Flip? (0/1): "))
if flip == 1:
    oList,tList = tList,oList
print("Ready")
input()
#print(rNums)
start = time.time()
right.append(0)
wrong.append(0)
allOf = len(rNums)
for i in range(allOf):
    check(rNums[i])
if wrong[len(wrong)-1] != 0: 
    rst()
end = time.time()
print(end-start,"seconds")
print(wrong,"wrong")
print(right,"right")
fileNString = "Test.log"
fullWrong = 0
fileString = "Testing log - "+datetime.datetime.fromtimestamp(end).strftime('%Y-%m-%d %H:%M:%S')+"\nTime: "+str(round(((end-start)/60),2))+" minutes\n"
for i in range(len(right)):
    fileString += ("Round "+str(i+1)+"\n")
    fileString += (str(int(wrong[i]))+" mistakes of "+str(int(right[i]))+" words ("+str(((right[i]-wrong[i])/right[i])*100)+" %)\n")
with open(fileNString, 'a') as the_file:
    the_file.write((fileString+'\n'))
the_file.close()
#
input()