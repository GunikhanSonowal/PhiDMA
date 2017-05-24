# PhiDMA
====================
PhidMF.py
PhidMF.py is small python program which is used to detect phishign site using multiplelayer filters
Developer : Mr.  Gunikhan Sonowal
====================
.. How to use::
$ python PhiDMA.py 

###########################################
.. Details PlateForm :: 
Operating System    : Ubuntu 16.04.1 LTS 64-bit
Processor           : Intel® Core™ i3 CPU 530 @ 2.93GHz × 4 
Script              : Python
##################################################
.. Multilevel FilterS ::
1. Whitelist Filter
2. Url Feature Filter
3. Lexical Signature Filter
4. String Matching Filter
5. Accessibility Score Matching
######################################################
.. FILE Structure::
File name               : Description
PhiDMA.py               : Main file where we start our program
Whitelist.py            : Whitelist file 
whitelist.txt           : list of whitelist
urlFilter.py            : Check the url
urlMatch.py             : Download the page of the url-> webfile.txt
webfile.txt             : Contain the words of the file
tf.py                   : Find the important word from webfile.txt to ->tf.txt
tf.txt                  : Contain the imporntat word of file
DuckDuckGo.py           : Seach engine using duckduckgo.py                 
totallink.txt           : Save all the file of return search engine
StringMatch.py          : Collect from duckduckgo file compare with current url using lcs.py, editDistance.py
lcs.py                  : Helping the StringMatch
editDistance            : Helping the editDistance
googleSimilarUrls.txt   : Save the matching file to this file
AccessibilityScore.py   : Collect the from googleSimilarUrls.txt and evalauate the score and save to mydata.txt
mydata                  : Score of Accessibility
Standard Divistion      : Find the standard devision of the scores
Confuse_Matrix          : Find the Accuracy and Confusion of our model
Result_Legitimate       : Result of the legitimate site
Result_Phishing         : Result of Phishing site
Result_final.csv        : Final result which run by confusion_matrix
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ENJOY THE CODE @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
