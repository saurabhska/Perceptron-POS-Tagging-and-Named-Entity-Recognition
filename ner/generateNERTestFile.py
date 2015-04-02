import sys
import os

def getNERTAG(word):
  if '/' in word:
    wordList=word.split('/')
    return wordList[-1]
  return word
  
def getPOSTAG(word):
  if '/' in word:
    wordList=word.split('/')
    return wordList[-2]
  return word  
  
def getWORD(word):
  if '/' in word:
    wordList=word.split('/')
    NERTAG=wordList[-1]
    POSTAG=wordList[-2]
    pos=len(word)-len(NERTAG)-1
    word=word[:pos]
    pos=len(word)-len(POSTAG)-1
    word=word[:pos]    
  return word


def main():
  if len(sys.argv) != 3:
    print ('usage: python3 generatePosTestFile.py inputFile outputFile')
    sys.exit(1)
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]
  infile=open(inputFile,'r',errors='ignore')
  outfile=open(outputFile,'w',errors='ignore')  
  lines = infile.readlines()
  for line in lines:
    outputLine=''
    lineWordList=line.split()
    for word in lineWordList:
      outputLine+=getWORD(word)+'/'+getPOSTAG(word)+' '
    outfile.write(outputLine)
    outfile.write('\n')
  infile.close()
  outfile.close()


if __name__ == '__main__':
  main()
