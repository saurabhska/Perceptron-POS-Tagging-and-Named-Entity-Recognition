Develop average perceptron to build a discriminative classifier and apply it to two NLP sequence labeling tasks: 
1) part-of-speech tagging and 
2) named entity recognition.

Link: http://appliednlp.bitbucket.org/hw2/index.html

Running Code & Files:

perceplern.py       : python3 perceplearn.py TRAININGFILE MODELFILE
percepclassify.py   : python3 percepclassify.py MODELFILE < inputFile > outputFile

postrain.py         : python3 postrain.py TRAININGFILE MODELFILE
postag.py           : python3 postag.py MODELFILE < inputFile > outputFile

nelearn.py          : python3 nelearn.py TRAININGFILE MODELFILE
netag.py            : python3 netag.py MODELFILE < inputFile > outputFile

******************************************************************************************
Accuracy of Parts of Speech Tagger:

Total Tags   : 40117
Wrong Tags   : 1639
Correct Tags : 38478
Accuracy     : 38478/40117 = 95.91%
******************************************************************************************
Precision, Recall and F-Score:

LOC: 
    Precision = 0.9837
    Recall    = 0.7997
    F-Score   = 0.8822
    
ORG: 
    Precision = 0.9404
    Recall    = 0.6782
    F-Score   = 0.7880
    
PER: 
    Precision = 0.9938
    Recall    = 0.7962
    F-Score   = 0.8840
    
MISC: 
    Precision = 0.8669
    Recall    = 0.4831
    F-Score   = 0.6204
    
Correct LOC 787.0
Correct PER 973.0
Correct ORG 1153.0
Correct MISC 215.0

Predicted Loc 800.0
Predicted Per 979.0
Predicted Org 1226.0
Predicted Misc 248.0

Actual in Ans Key Loc 984.0
Actual in Ans Key Per 1222.0
Actual in Ans Key Org 1700.0
Actual in Ans Key Misc 445.0

Total Correct Entities 3128
Total Predicted Entities 3253
Total Entities in Answer Key 4351

Avg. Precision : 0.9615
Avg. Recall    : 0.7474 
Avg. F-Score   : 0.8419

******************************************************************************************
Comparing with Naive Bayes Classifier:

Accuracy with Avg. Perceptron:  95.91%
Accuracy with Naive Bayes: 93.56%

Accuracy of Avg. Perceptron is greater than that of Naive Bayes classifier as Naive
Bayes uses Bag of Words features and considers words to be independent of each other 
whereas in Avg. Perceptron we are considering the previous and next words with suffix 
and word shape as feature which gives better accuracy. 
******************************************************************************************
