import sys
import os

def getMismatch(line1,line2):
  wordlist1=line1.split()
  wordlist2=line2.split()    
  count=0
  for i in range(0,len(wordlist1)):
    if wordlist1[i] != wordlist2[i]:
      count+=1
      print('mismatch: '+wordlist1[i]+' : '+ wordlist2[i])
  return count


def main():
  if len(sys.argv) != 3:
    print ('usage: python3 computeAccurracy.py testFile outputFile')
    sys.exit(1)
    
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]  
  
  infile=open(inputFile,'r',errors='ignore')
  outfile=open(outputFile,'r',errors='ignore')
  
  lines1=infile.readlines()
  lines2=outfile.readlines()
  
  inputWordList=list()
  outputWordList=list()  
  
  for line in lines1:
    wordList=line.split()
    for word in wordList:
      inputWordList.append(word)
     
  for line in lines2:
    wordList=line.split()
    for word in wordList:
      outputWordList.append(word)
  
  mismatchCount=0
  for i in range(0,len(lines1)):
    l1=lines1[i]
    l2=lines2[i]
    #print(l1)
    #print('--------------------------------')
    #print(l2)
    mismatchCount+=getMismatch(lines1[i],lines2[i])
      
  print('Total words in input file: '+str(len(inputWordList)))
  print('Total words in outputput file: '+str(len(outputWordList)))  
  print('Total words mismatch/wrongly classified: '+str(mismatchCount))
  correct=len(inputWordList)-mismatchCount
  accurracy=correct/len(inputWordList)
  print('Accuracy: '+str(accurracy))
      
  



if __name__ == '__main__':
  main()
