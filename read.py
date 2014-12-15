
#from os import *
from whoosh.fields import *
from whoosh.index import create_in
from whoosh.query import *
from whoosh.index import open_dir
from itertools import izip
"""
def create_corpus():
	fdGer = open("lang2.txt",'w')
	fdEng = open("lang1.txt",'w')
	isEnglish = False
	for i in open("de-en").readlines():
		if("") # not a proper sentence
		if("") #english sentences started 
			isEnglish = true
		if isEnglish == True:
			fdEng.write(i.lower())
		else:
			fdGer.write(i.lower())
	fdGer.close()
	fdEng.close()
"""
#creates index and stores in in the folder index/ from the file1 and file2 which contain sentences and their translations in an aligned manner
def create_index(file1, file2):
	#create schema
	schema = Schema(original=TEXT(stored="True"), translation=STORED)
	ix = create_in("index", schema)
	#create index
	ix = open_dir("index")
	#write all the the sentences with their translation into IR index 
	writer = ix.writer()
	with open(file1) as fdOriginal, open(file2) as fdTranslation:
		for i,j in izip(fdOriginal, fdTranslation):
			writer.add_document(original=unicode(i,"UTF-8" ), translation=unicode(j,"UTF-8" ))

		#close everything
	ix.close()	
	writer.commit()
#seach for a query in index and returns the mathing results which is a python dictionatruy of sentences and their translations
def search(query):
	#create query
	ix = open_dir("index")	
	termList = []
	for word in query.lower().split():
		termList.append( Term("original", unicode(word, "UTF-8")  ))

	myquery = Or( termList)
	#search query and store results
	searcher = ix.searcher()
	results = searcher.search(myquery)
	formatted = {}
	for i in results:
		formatted[i['original'] ]= i['translation']
		#print i['original']
	#searcher.close()
	#ix.close()
	return formatted
	
