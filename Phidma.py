#############################################
#########Title : PhiDMA ######################
###############################################
import sys
import time
from whitelist import CheckInWhiteList # whitelist matching file
from urlFilter import url_score # url feature extract file
from urlMatching import urlMatch # google, tf file
from StringMatch import checkUrlMatch # url matching 
from AccessibilityScore import mainAccessibleFunction # accessibility score evaluation
from StandardDeviation import standardDeviation # comparison between errors
from tf import tfmain # tf find
from DuckDuckGo import duckduckgoSearch
whitelist = open("whitelist.txt", "a+")
sd = open("standardValue.txt", "a+")
result = open("Ham_result4.txt", "a+")
fp = open("Phishing_dataset.txt","r")
# start from 324,1,http://www.seesaa.net

def phidMA(line1):
	row = line1.strip()
	line = row.split(',')  
	print "Checking in Whitelist ...", line[2]
	if CheckInWhiteList(line[2]):
		print "Legitimate site\n"
		result.write(line[0]+","+"0"+","+line[2]+"\n")
		return "Legitimate Site."
	else:
		print "!Not in Whitelist **** Url Filter Filter:", line[2]
		urlscore = url_score(line[2])
		if urlscore >= 3:
			print "Warning!  Phising site\n"
			result.write(line[0]+","+"1"+","+line[2]+"\n")
			return "Warning!  Phishing Site"			        
		else:        
			print "!No Phishing Feature **** Lexical Features checking........"
			if urlMatch(line[2]) == False:
				print "Webpage Downlaod Fail"
				result.write(line[0]+","+"2"+","+line[2]+"\n")
				return "Warning! Phishign Site"
			else:
				tfmain("webfile.txt", line[2]) # find the tf of the webpage
				time.sleep(2)
				duckduckgoSearch()
				if checkUrlMatch(line[2])==False:
					result.write(line[0]+","+"1"+","+line[2]+"\n")
					return "Warning! Phishing Site"
		
				else:
					print "Accessibility Filter Checking"

					if mainAccessibleFunction() == False:
						
						result.write(line[0]+","+"2"+","+line[2]+"\n")
						return "Suspicious Url" 
					else:     
						value = standardDeviation()  
						sd.write(line[0]+","+ str(value)+"\n")
						if value < 7.5:
						    print "It is genuine site"
						    result.write(line[0]+","+"0"+","+line[2]+"\n")   
						    whitelist.write(line[0]+"\n")      
						    return "Legitimate Site"	
						else:
						    print "Phishing"
						    result.write(line[0]+"\n")  
						    result.write(line[0]+","+"1"+","+line[2]+"\n") 
						    return "Warning! Phishing Site"  
if __name__ == "__main__":
    for line in fp:
        print line
        phidMA(line)
  
  
        										
