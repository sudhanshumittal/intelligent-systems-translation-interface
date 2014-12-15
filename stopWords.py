#import cPickle as pickle
from nltk import PorterStemmer
#from settings import *
def create_stopword_list(stopword_file):
	stopwords = []
	for word in open(stopword_file):
		stopwords.append(word.strip())

	"""with open('stopWords.pik', 'wb') as f:
		pickle.dump(stopwords, f, -1)
	"""
	return stopwords	
def remove_stopwords(wordList, stopwords):

    assert isinstance(wordList, list)
    assert isinstance(stopwords, list)

    return [x for x in wordList if x not in stopwords]

def tokenize(data):

    assert isinstance(data, basestring)
    return re.findall('\w+', data.lower())

def stem(a): #stems string a using porter Stemming
	
	a = PorterStemmer().stem_word(a)
	return a
def sec(word): #hash function for secondary map
	if len(word) <2:
		return word[0]%index_count
	return (ord( word[0])*26+ord(word[1] )) % index_count

