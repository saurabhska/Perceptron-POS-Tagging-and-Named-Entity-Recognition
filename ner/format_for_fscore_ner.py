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
    print ('usage: python3 computeAccurracy.py devFile outputFile')
    sys.exit(1)
    
  inputFile = sys.argv[1]
  outputFile = sys.argv[2]  
  
  infile=open(inputFile,'r',errors='ignore')
  outfile=open(outputFile,'r',errors='ignore')
  
  lines1=infile.readlines()
  lines2=outfile.readlines()
  
  if len(lines1) != len(lines2):
    print("line count mismatch in 2 files")
  else:
    for i in range(0,len(lines1)):
      l1=lines1[i]
      l2=lines2[i]
      sys.stdout.write(l1)
      sys.stdout.flush()
      sys.stdout.write(l2)
      sys.stdout.flush()
      
  



if __name__ == '__main__':
  main()
