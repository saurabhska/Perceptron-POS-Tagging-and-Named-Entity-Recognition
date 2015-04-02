import sys
import os
import re
import pickle
import codecs

classWeights = dict()

def getNERTAG(word):
  if '/' in word:
    wordList=word.split('/')
    return wordList[-1]
  return word
 
  
def getPOSTAG(word):
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

def findMax(computedValues):
  flag=0
  for key,value in computedValues.items():
    if flag==0:
      max_value=value
      returnLabel=key
      flag=1
    else:
      if value > max_value:
        max_value=value
        returnLabel=key
  return returnLabel
  
def computeClassLabel(feature):
  #print(featureList)
  global classWeights
  computedValues=dict()
  curWord=''
  curPOS=''
  featureList=feature.split()
  for label, weightVector in classWeights.items():
    value=0
    for word in featureList:
      #print('word: '+word)
      wordList=word.split(':')
      #print(wordList)
      if wordList[0]=='curWord':
        curWord=wordList[1]
      if wordList[0]=='curPOS':
        curPOS=wordList[1]        
      if word in weightVector:
        value+=weightVector[word]
    computedValues[label]=value
  #print('computedValues')
  #print(computedValues)
  curWord=curWord+'/'+curPOS+'/'+findMax(computedValues)
  #print('computedValues')
  #print(curWord)
  return curWord
  
def readWeights(modelFile):
  global classWeights
  modelread=open(modelFile,'rb')
  classWeights=pickle.load(modelread)
  modelread.close()
  
def formatInputLine(line):
  #infile=open(testFile,'r',errors='ignore')
  #lines = infile.readlines()
  #infile.close()
  inputLineList=list()
  #for line in lines:
  line='BEG/BEG '+line+' TER/TER'
  #print(line)
  inputLineWordList=line.split()
  #print(trainingFileWordList)
  for i in range(1,len(inputLineWordList)-1):
    printLine=''
    prevWord=inputLineWordList[i-1]
    curWord=inputLineWordList[i]
    nextWord=inputLineWordList[i+1]
    #prevWordList=prevWord.split('/')
    #curWordList=curWord.split('/')
    #nextWordList=nextWord.split('/')
    #print('prevWord:'+prevWord+' '+'curWord:'+curWord+' '+'nextWord:'+nextWord)
    printLine='prevWord:'+getWORD(prevWord)+' '+'curWord:'+getWORD(curWord)+' '+'nextWord:'+getWORD(nextWord)+' '
    printLine+='prevPOS:'+getPOSTAG(prevWord)+' '+'curPOS:'+getPOSTAG(curWord)+' '+'nextPOS:'+getPOSTAG(nextWord)
    printLine+=' '+getSuffixString(getWORD(curWord))
    inputLineList.append(printLine)
  return inputLineList  
      
def main():
  outputLine=''
  if len(sys.argv) != 2:
    sys.stdout.write('usage: python3 neclassify.py modelFile')
    sys.exit(1)
  modelFile = sys.argv[1]
  #testFile = sys.argv[2]
  readWeights(modelFile)
  
  #infile=open(testFile,'r',errors='ignore')
  #lines = infile.readlines()
  #infile.close()
  sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')
  lines = sys.stdin.readlines()
  
  for line in lines:
    flag=0
    outputLine=''
    featureList = formatInputLine(line)
    #featureList=inputData.split()
    #print('featureList...............................')
    #print(featureList)
    #print('..........................................')
    for feature in featureList:
      if flag==0:
        flag=1
        feature+=' '+'prevNER:BEG'
      else:
        feature+=' '+'prevNER:'+getNERTAG(label)
      #print('computing label for feature....'+feature)
      label=computeClassLabel(feature)
      outputLine+=label+' '
      #print('output line is.....'+outputLine)
    sys.stdout.write(outputLine + '\n')
    sys.stdout.flush()
    
if __name__ == '__main__':
  main()
