#script to generate training file
# Call: python3 generateTraining.py /home/saurabhska/csci544-hw1-tmp/SPAM_training/ /home/saurabhska/csci544-hw1/outputFeb2/spam_training.txt

import sys
import os
import re

def getFileLabel(inputFile):
  fileNameParts=inputFile.split('.')
  return fileNameParts[0]

def getFileNames(inputFilePath):
  fileNames=sorted(os.listdir(inputFilePath))
  return fileNames

def createTrainingFile(fileNames,inputFilePath,outputFilePath):
  #outputFile=outputFilePath+'/'+'spam_training.txt'
  outfile=open(outputFilePath,'w',errors='ignore')
  #inputFilePath+='/'
  #print('Inside createTrainingFile the filenames are')
  #print(fileNames)
  for inputFile in fileNames:
    #print('Working on file '+inputFile)
    trainingFileLine=''
    fileText=''
    fileLabel=''
    fileLabel=getFileLabel(inputFile)
    temp=inputFilePath+'/'+inputFile
    inputFile=temp
    infile=open(inputFile,'r',errors='ignore')
    fileText=infile.read()
    infile.close()
    #fileText=re.sub('[^A-Za-z \n]+', '', fileText)
    fileText=fileText.replace('\n', ' ').replace('\r', '')
    trainingFileLine+=fileLabel
    trainingFileLine+=' '
    trainingFileLine+=fileText
    outfile.write(trainingFileLine)
    outfile.write("\n")
  outfile.close()


def main():
  if len(sys.argv) != 3:
    print ('usage: python3 generateTraining.py input-file-path output-file-path')
    sys.exit(1)

  inputFilePath = sys.argv[1]
  outputFilePath = sys.argv[2]
  fileNames=getFileNames(inputFilePath)  #get file names from path
  createTrainingFile(fileNames,inputFilePath,outputFilePath)          #create 1 training file
  #createTrainingFile(fileNames)
  #print (fileNames)
  #print ("Number of files is: "+str(len(fileNames)))

if __name__ == '__main__':
  main()
