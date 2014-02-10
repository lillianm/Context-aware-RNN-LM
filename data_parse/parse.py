import re
import sys,os
#symbols = {"%hes":"err","%spk":"well","%int":"%laugh","noise":""}
symbols = {"%hes":"","%spk":"","%int":"","noise":""}
addition = {"--":" "}
# how to use those 


def parse_txt_file (fileName, dirName):
	file1 = open(fileName)
	file2 = open(dirName + "cesar_data.txt.text","w+")
	file3 = open(dirName + "cesar_data.txt.feat","w+")
	for line in file1:
		text = line.split("\t")[-1]
		feat = line.split("\t")[-2]
		# only extract the text part
		pattern = re.compile("[a-zA-Z\s\^'%()\-'<>]+")
		text = re.search(pattern, text)
		if text:
			text = text.group(0)
			# not useful tags 
			noUseTags = re.compile("<//noise>|\n|[()\^\-<>]|noise")
			text = re.sub(noUseTags , "", text)
			# delete space or tab in the beginning of the sentences
			format = re.compile("^\s+")
			for s in symbols:
				text = text.replace(s,symbols.get(s))
				# delete multiple spaces

			text = text.replace("\s{2,}", " ")
			text = re.sub(format, "",text)
			if text:
				file2.write(text+"\n")
				if feat=="driver":
					 bi_feat = 1;
				else:
					if feat == "copilot":
						bi_feat = 0;
				file3.write(str(bi_feat)+"\n")

def generate_vocabulary(fileName, dirName):
	textFile = open(fileName)
	vocab = open("vocab_" + dirName + ".txt","w+")
	vocabulary = set([])

	for line in textFile:
		pattern = re.compile("[%<>\-/]z|\n")
		nline = re.sub(pattern, "", line)
		nline = nline.replace("\s{2,}"," ")
		words = set(nline.split(" "))
		vocabulary  = vocabulary | words

		v = list(vocabulary)
		v.sort()
		for word in v:
			if word:
				vocab.write(word+"\n")



dir = "../CESAR_data"
fileName = 'data.txt'
for root, dirs, files in os.walk(dir):
	for subDir in dirs:
		path = os.path.join(dir, subDir)
		for r, d, files in os.walk(path):
			if fileName in files:
				print fileName
				parse_txt_file(os.path.join(path,fileName), subDir)
				generate_vocabulary(subDir + "cesar_data.txt.text", subDir)




# file1 = open("data.txt")
# file2 = open("cesar_data.txt.text","w+")
# file3 = open("cesar_data.txt.feat","w+")












