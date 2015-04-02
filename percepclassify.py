import sys
import os
import re
import codecs
import pickle

classWeights = dict()
  
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
  
def computeClassLabel(featureList):
  global classWeights
  computedValues=dict()
  for label, weightVector in classWeights.items():
    value=0
    for word in featureList:
      if word in weightVector:
        value+=weightVector[word]
    computedValues[label]=value
  return findMax(computedValues)
  
def readWeights(modelFile):
  global classWeights
  modelread=open(modelFile,'rb')
  classWeights=pickle.load(modelread)
  modelread.close()
      
def main():
  if len(sys.argv) != 2:
    print ('usage: python3 percepclassify.py modelFile')
    sys.exit(1)
  modelFile = sys.argv[1]
  readWeights(modelFile)
  
  sys.stdin = codecs.getreader('utf8')(sys.stdin.detach(), errors='ignore')
  lines = sys.stdin.readlines()
      
  for line in lines:
    featureList=line.split()
    #print(featureList)
    outputLabel=computeClassLabel(featureList)
    #outputLine+=computeClassLabel(feature)+' '
    sys.stdout.write(outputLabel + '\n')
    sys.stdout.flush()
    
if __name__ == '__main__':
  main()
