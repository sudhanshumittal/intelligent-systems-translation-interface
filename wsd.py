from text.blob import Word
import difflib
from stopWords import *
stopwords = create_stopword_list('common_words')

def bestMatch(defList1, defList2):
	if len(defList1) == 0:
		return -1, 0 
	defList1 =  remove_stopwords(defList1, stopwords)
	defList2 =  remove_stopwords(defList2, stopwords)
	
	score = 0
	max_def1 = 0
	max_def2 = 0
	i = 0
	j = 0
	for def1 in defList1:
		for def2 in defList2:
			sm=difflib.SequenceMatcher(None,def1.split(),def2.split())
			score1 = max(score, sm.ratio())
			if score1 != score:
				score = score1
				max_def1 = i
				max_def2 = j
			j+=1
		i+=1
		j = 0
	return max_def1, score 
"""
def tagMeaning(sentenceList):
	
	defList = []
	for word in sentenceList:
		word = Word(word)
		defn = word.definitions
		print defn
		defList.append(defn)
	sentenceList[0] += "_"+str()
	for i in range(0, len(sentenceList)-1):
		#first and last word

		i1, score1 = bestMatch(defList[i], defList[i+1])
		#i2, score2 = bestMatch(defList[i], bestMatch[i+1])
		#if score1>score2:
		sentenceList[i] += "_"+str(i1)
		#else:
		#	sentenceList[i] += "_"+str(i2)
	return sentenceList
"""
def meaning(wIndex, sentence):
	if len(sentence) == 0:
		return -1
	#print sentence[wIndex]
	if wIndex <0 or wIndex > len(sentence)-1:
		return -1
	#definitin for givern word
	#word =  
	wordDefinitions = Word(sentence[wIndex]).definitions
	#print wordDefinitions
	bestMeaning = 0
	maxScore = 0
	disambWord  = ""
	for word in sentence:
		if word == sentence[wIndex]:
			continue
		prevWordDefinitions = Word(sentence[wIndex-1]).definitions

		i1, maxScore1 = bestMatch(prevWordDefinitions, wordDefinitions)
		if maxScore1 > maxScore:
			bestMeaning = i1
			maxScore = maxScore1
			disambWord = word
	
	#print maxScore, disambWord, wordDefinitions[bestMeaning]
	return bestMeaning
	"""	
	nextWordDefinitions = []
	prevWordDefinitions = []
	if wIndex > 0:
		prevWordDefinitions = Word(sentence[wIndex-1]).definitions
	if wIndex < len(sentence)-1:
		nextWordDefinitions = Word(sentence[wIndex+1]).definitions
	print prevWordDefinitions,"\n",  wordDefinitions, "\n", nextWordDefinitions
	#definitions for next word
	i1, maxScore1 = bestMatch(prevWordDefinitions, wordDefinitions)
	i2, maxscore2 = bestMatch(nextWordDefinitions, wordDefinitions)
	if maxScore1>maxscore2:
		return i1
	else :
		return i2
	"""
	#definitions for prev word
#print tagMeaning ('this is the river bank new'.split())
#print meaning(0, 'pine cone'.lower().split())