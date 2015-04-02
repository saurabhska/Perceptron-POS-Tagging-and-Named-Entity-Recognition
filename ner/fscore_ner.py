import re
import math
import os
import sys

inputPath = sys.argv[1]

f = open(inputPath,"r")
lines = f.readlines()
f.close()
totalCount = 0
mismatchCount = 0

i = 0
original = [] 
result = []
while i<len(lines):
    originalLine = lines[i]
    resultLine = lines[i+1]
    originalLine = re.sub("\n+","",originalLine)
    resultLine = re.sub("\n+","",resultLine)
    originalLine = originalLine.split(" ")
    resultLine = resultLine.split(" ")
    j=0
    while j < len(originalLine):
        originalWords = originalLine[j].split("/")
        originalWord = originalWords[len(originalWords)-1]
        resultWords = resultLine[j].split("/")
        resultWord = resultWords[len(resultWords)-1]
        original.append(originalWord) 
        result.append(resultWord)  
        
        '''if(originalWord != resultWord):
            mismatchCount +=1
        totalCount +=1'''
        j+=1
    i +=2

trueLoc = 0.0
trueOrg = 0.0
truePer = 0.0
trueMisc = 0.0

countLoc = 0.0
countOrg = 0.0
countPer = 0.0
countMisc = 0.0

totalPer = 0.0
totalLoc = 0.0
totalOrg = 0.0
totalMisc = 0.0

k=0
print(str(len(original)))
while k< len(original):
    #print(str(k))
    if(original[k]=='B-ORG'):
        totalOrg+=1
        if(result[k]=='B-ORG'):
            k+=1
            countOrg+=1    
            while original[k]=='I-ORG' and result[k]=='I-ORG':
                k+=1
            if original[k]!='I-ORG' and result[k]!='I-ORG':
                trueOrg+=1
            else:
                while original[k]=='I-ORG':
                    k+=1
        else:
            k+=1
            if original[k]=='I-ORG':
                while original[k]=='I-ORG':
                    k+=1
                
    elif(original[k]=='B-PER'):
        totalPer+=1
        if(result[k]=='B-PER'):
            k+=1
            countPer+=1    
            while original[k]=='I-PER' and result[k]=='I-PER':
                k+=1
            if original[k]!='I-PER' and result[k]!='I-PER':
                truePer+=1
            else:
                while original[k]=='I-PER':
                    k+=1
        else:
            k+=1
            while original[k]=='I-PER':
                k+=1
                
    elif(original[k]=='B-LOC'):
        totalLoc+=1
        if(result[k]=='B-LOC'):
            k+=1
            countLoc+=1    
            while original[k]=='I-LOC' and result[k]=='I-LOC':
                k+=1
            if original[k]!='I-LOC' and result[k]!='I-LOC':
                trueLoc+=1
            else:
                while original[k]=='I-LOC':
                    k+=1
        else:
            k+=1
            while original[k]=='I-LOC':
                k+=1
                
    elif(original[k]=='B-MISC'):
        totalMisc+=1
        if(result[k]=='B-MISC'):
            k+=1
            countMisc+=1    
            while original[k]=='I-MISC' and result[k]=='I-MISC':
                k+=1
            if original[k]!='I-MISC' and result[k]!='I-MISC':
                trueMisc+=1
            else:
                while original[k]=='I-MISC':
                    k+=1
        else:
            k+=1
            while original[k]=='I-MISC':
                k+=1
    else:
        if original[k]!='O':
            print(original[k])
        k+=1

print(str(len(original))) 
print(str(totalLoc+totalOrg+totalMisc+totalPer))
print(str(k))              
print('trueLoc ' + str(trueLoc))
print('truePer ' + str(truePer))
print('trueOrg ' + str(trueOrg))
print('trueMisc '+ str(trueMisc))

print('countLoc ' + str(countLoc))
print('countPer ' + str(countPer))
print('countOrg ' + str(countOrg))
print('countMisc '+ str(countMisc))

print('totalLoc ' + str(totalLoc))
print('totalPer ' + str(totalPer))
print('totalOrg ' + str(totalOrg))
print('totalMisc '+ str(totalMisc))

precisionLoc = trueLoc/countLoc
recallLoc = trueLoc/totalLoc
print('precisionLoc '+str(precisionLoc))
print('recallLoc '+str(recallLoc))

precisionOrg = trueOrg/countOrg
recallOrg = trueOrg/totalOrg
print('precisionOrg '+str(precisionOrg))
print('recallOrg '+str(recallOrg))

precisionPer = truePer/countPer
recallPer = truePer/totalPer
print('precisionPer '+str(precisionPer))
print('recallPer '+str(recallPer))

precisionMisc = trueMisc/countMisc
recallMisc = trueMisc/totalMisc
print('precisionMisc '+str(precisionMisc))
print('recallMisc '+str(recallMisc))

'''print("total : " + str(totalCount))
print("mismatch : " + str(mismatchCount))
print("Accuracy : "+str((totalCount-mismatchCount)/totalCount))
print("Error : " + str(mismatchCount/totalCount))'''


