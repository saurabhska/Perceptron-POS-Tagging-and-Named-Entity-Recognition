import sys
import os
import re
import random
import pickle
import codecs
import perceplearn

def getTAG(word):
  if '/' in word:
    wordList=word.split('/')
    return wordList[-1]
  return word
  
def getWORD(word):
  if '/' in word:
    wordList=word.split('/')
    lastWord=wordList[-1]
    pos=len(word)-len(lastWord)-1
    return word[:pos]
  return word

def getWordshape(word):
  #print(word)
  word=re.sub('[^A-Za-z0-9 ]+', '-', word)
  #print(word)
  word=re.sub('[a-z]+', 'a', word)
  word=re.sub('[A-Z]+', 'A', word)
  word=re.sub('[0-9]+', '9', word)
  #print(word)
  word=re.sub('[A]+', 'A', word)
  #print(word)
  word=re.sub('[a]+', 'a', word)
  #print(word)
  word=re.sub('[-]+', '-', word)  
  return word
  
def getSuffixString(word):
  suffix3=''
  suffix2=''
  wshape=''
  returnString=''
  wordLength=len(word)
  if wordLength < 3:
    suffix3=word
    suffix2=word
    wshape=getWordshape(word)
  else:
    suffix3=word[-3:]
    suffix2=word[-2:]
    wshape=getWordshape(word)
  returnString='suffix3:'+suffix3+' '+'suffix2:'+suffix2+' '+'wshape:'+wshape
  return returnString
  
def formatTrainingFile(trainingFile):
  infile=open(trainingFile,'r',errors='ignore')
  lines = infile.readlines()
  trainingFileList=list()
  for line in lines:
    line='BEG/BEG '+line+' TER/TER'
    #print(line)
    trainingFileWordList=line.split()
    #print(trainingFileWordList)
    for i in range(1,len(trainingFileWordList)-1):
      printLine=''
      prevWord=trainingFileWordList[i-1]
      curWord=trainingFileWordList[i]
      nextWord=trainingFileWordList[i+1]
      #print('prevWord:'+prevWord+' '+'curWord:'+curWord+' '+'nextWord:'+nextWord)
      #prevWordList=prevWord.split('/')
      #curWordList=curWord.split('/')
      #nextWordList=nextWord.split('/')
      printLine=getTAG(curWord)+' '+'prevWord:'+getWORD(prevWord)+' '+'curWord:'+getWORD(curWord)+' '+'nextWord:'+getWORD(nextWord)
      printLine+=' '+getSuffixString(getWORD(curWord))
      trainingFileList.append(printLine)
  return trainingFileList
         
def main():
  if len(sys.argv) != 3:
    print ('usage: python3 postrain.py trainingFile modelFile')
    sys.exit(1)
  trainingFile = sys.argv[1]
  modelFile = sys.argv[2]
  trainingFileList=formatTrainingFile(trainingFile)
  #print(trainingFileList)
  perceplearn.initializeClassWeights(trainingFileList)
  perceplearn.adjustClassWeights(trainingFileList,modelFile)
  
  
  #print(getTAG('Saurabh/Agrawal/123'))
  #print(getWORD('Saurabh/Agrawal/123'))
  #print(getTAG('Saurabh/Agrawal'))
  #print(getWORD('Saurabh/Agrawal'))
  #print(getTAG('Saurabh/Agrawal/123/xyz'))
  #print(getWORD('Saurabh/Agrawal/123/xyz'))
  #print(getTAG('Saurabh'))
  #print(getWORD('Saurabh'))  
  #print(getWordshape('cats'))
  #print(getWordshape('Cat5'))
  #print(getWordshape('SAurabh@#$$%^&'))
  
  #writeModelFile(modelFile)  

if __name__ == '__main__':
  main()
