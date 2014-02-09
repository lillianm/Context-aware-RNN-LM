import sys, os
import re 

textFile = open("cesar_data.txt.text")
vocab = open("vocab_list.txt","w+")
vocabulary = set([])

for line in textFile:
	pattern = re.compile("[%<>\-/]z|\n")
	nline = re.sub(pattern, "", line)
	nline = nline.replace("\s{2,}"," ")
	words = set(nline.split(" "))
	vocabulary  = vocabulary | words

for word in vocabulary:
	if word:
		vocab.write(word+"\n")
