# Code to find top k closest matching sentences using simple editdistance technique
# As a part of Intelligent system and interfaces project-I


from read import *
from wsd import *

# calculate word level levinstein distance between two sentences
wsd = False
def bottom_up_lev(str1, str2):
	#print str1,str2
	if min( len(str1), len(str2)) == 0:
		return max( len(str1), len(str2))
	minValues = [[]]
	for i in range(0, len(str1)+1):
		minValues.append([])
		for j in range(0, len(str2)+1):
			if i == 0:
				minValues[i].append(j)
			elif j==0: 
				minValues[i].append(i)
			else:	
				minValues[i].append(0)

	for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
					if wsd == True:
						if meaning(i-1, str1) == meaning(j-1, str2):
							minValues[i][j] = min(minValues[i-1][j]+1, minValues[i][j-1]+1, minValues[i-1][j-1])
						else:
							minValues[i][j] = min(minValues[i-1][j], minValues[i][j-1], minValues[i-1][j-1])+1	
					else:
						minValues[i][j] = min(minValues[i-1][j]+1, minValues[i][j-1]+1, minValues[i-1][j-1])
						

			else:
				minValues[i][j] = min(minValues[i-1][j], minValues[i][j-1], minValues[i-1][j-1])+1
	#print minValues 
	return minValues[len(str1)][len(str2)]


# input parameters :
#    inputStr -> the input sentence whose closest match is to be found
#    sentenceRepo -> list of the probable matching sentences for inputStr obtained from IR engine
#    n -> Maximum number of results to be returned
# output : A list of top n sentences
def getTopn(inputStr, sentenceRepo, n):
	inputStr = unicode(inputStr.lower(), "UTF-8")
	if not inputStr:
		return
		#inputStr=unicode("a big fat dog", "UTF-8")
	if not sentenceRepo:
		#sentenceRepo={"the big house with the fat dog":"1", "the big fat dog":"3","a big fat dog":"2"}
		return
	#print "The input sentence whose match is to be found is : ", inputStr
	#print "The possible matching sentence  are: "
	editDistanceDict={};
	probableMatch=[]
	for (sentence, translation) in sentenceRepo.items():
		str1=inputStr.split()
		str2=sentence.lower().split()
		#print str1
		editDistance= bottom_up_lev(str1, str2)
		#print editDistance

		#lev(str1,str2,len(str1)-1,len(str2)-1)
		editDistanceDict[sentence]=editDistance
		#print sentence, " :::: edit distance is : ", editDistance

	count=1;
	#print n, len(editDistanceDict)
	# sort the editDistanceDict and get top n sentences
	for w in sorted(editDistanceDict, key=editDistanceDict.get):
		probableMatch.append((w,sentenceRepo[w],editDistanceDict[w]))
		if count == n:
			return probableMatch
		count+=1
	return probableMatch


def getMatchingSentences(query,n, enableWsd = False):
	query = query.lower()
	wsd = enableWsd
	results=getTopn(query, search(query), n)
	for (i,j,k) in results:
		print i.strip('\n')+"\t"+str(k),j.strip('\n')+"\t"
	return results
#sample usage
#without wsd
#getMatchingSentences('hand-over of West Bank territory to the Palestinian authorities.', 10)
#with wsd
#getMatchingSentences('Bank territory to the Palestinian authorities.', 10, enableWsd = True)
