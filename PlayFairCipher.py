#PlayFair Cipher Coded by Prateek Mahajan
#
#Enter plainText in the 'plainText.txt' file
#Enter key which is a single word
#CipherText is displayed and saved in file cipherText.txt
#Test Case:
#
#plainText:     Cryptography
#
#key:   goodmorning
#
# playFair Table:
#
#   ['G', 'O', 'D', 'M', 'R']
#   ['N', 'J', 'A', 'B', 'C']
#   ['E', 'F', 'H', 'K', 'L']
#   ['P', 'Q', 'S', 'T', 'U']
#   ['V', 'W', 'X', 'Y', 'Z']
#
#cipherText:    LCVTQMOGNSKX

def removeRepeatChars(word):
    returnList=[]
    for x in word:
        if x not in returnList:
            returnList.append(x)
    return returnList

def makeLetterBox(letterBox):

    if 'I' in letterBox:
        letterBox[letterBox.index('I')]='J'
    for i in range(26):
        if chr(i+65)=='I':
            continue
        if chr(i+65) in letterBox:
            continue
        else:
            letterBox.append(chr(i+65))
    return letterBox

def makeMatrix5x5(letterBox):
    tempList=[]
    returnList=[]
    indexCount=0
    for i in range(5):
        for j in range(5):
            tempList.append(letterBox[indexCount])
            indexCount+=1
        returnList.append(tempList)
        tempList=[]
    return returnList

def removeAllSpacesAndI(plainText):
    returnText=""
    for i in plainText:
        if i==" ":
            continue
        elif i=="I":
            returnText+="J"
        elif ord(i)>64 and ord(i)<=90: #just choose Capital Alphabets
            returnText+=i
    return returnText

def addDummyChars(plainText):
    returnText=""
    if len(plainText)%2:
        plainText+="X"
    count=0
    while count<(len(plainText)):
        if count==len(plainText)-1:
            returnText+=plainText[count]+'X'
        elif plainText[count]==plainText[count+1]:
            returnText+=plainText[count]+'X'
            count-=1
        else:
            returnText+=plainText[count]+plainText[count+1]
        count+=2
    if len(returnText)%2:
        returnText+='X'
    if returnText[-1]==returnText[-2]:
        returnText=returnText[0:-2]
    return returnText

def getReplaceChars(a,b,letterBox):
    x1,y1,x2,y2=0,0,0,0
    indexPt=0
    for i in range(5):
        for j in range(5):
            if a==letterBox[i][j]:
                x1=i
                y1=j

            if b==letterBox[i][j]:
                x2=i
                y2=j

    #following the rules of PlayFair Cipher:
    #1. if both letters letters of plainText are present in the
        #in the same row of the table then the letters are
        #replaced by the letter to their right with the leftmost
        #letter circularly following the rightmost letter
    if x1==x2:
        return letterBox[x1][(y1+1)%5], letterBox[x2][(y2+1)%5]
    #2. if both the letters of the plainText are present in the
        # same column of the table then they are replaced with
        # bottom letters of the same column with the topmost
        #letter circularly following the bottommost letter
    if y1==y2:
        return letterBox[(x1+1)%5][y1],letterBox[(x2+1)%5][y2]
    #3. generally when both the letters are present in different
        #rows and columns replace the letters with the letter
        # of the same row but the column of the other letter
    return letterBox[x1][y2], letterBox[x2][y1]

key=list(input("Enter the key: ").split())[0].upper() #take the key

letterBox=removeRepeatChars(key)

letterBox=makeLetterBox(letterBox)
letterBox=makeMatrix5x5(letterBox)

#uncomment to view PlayFair table
for i in range(5):
    print(letterBox[i])
plainText=""

#read plainText
try:
    file=open("plainText.txt","r")
    plainText=file.read()
    file.close()
except:
    file=open("plainText.txt","w+")
    file.write("Cryptography")
    plainText="Cryptography"
    file.close()
    print("plainText.txt is created plaese enter the plainText in the file")

plainText = removeAllSpacesAndI(plainText.upper())#make upperCase and remove special chars
plainText=addDummyChars(plainText.upper()) #add dummy chars if there are pairs with repeating letters

cipherText=""

for i in range(0,len(plainText)-1,2):
    a,b=getReplaceChars(plainText[i],plainText[i+1],letterBox)

    cipherText+=a+b

print("The plainText is : "+plainText)
print("The cipherText is : "+cipherText)

file=open("cipherText.txt","w+")
file.write(cipherText)
file.close()
