import sys
import os


def getWORD(word):
  if '/' in word:
    wordList=word.split('/')
    lastWord=wordList[-1]
    pos=len(word)-len(lastWord)-1
    return word[:pos]
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
      word=getWORD(word)
      outputLine+=word+' '
    outfile.write(outputLine)
    outfile.write('\n')
  infile.close()
  outfile.close()


if __name__ == '__main__':
  main()
