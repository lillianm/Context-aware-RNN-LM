import re

symbols = {"%hes":"err","%spk":"well","%int":"%laugh","noise":""}
addition = {"--":"%quad"}
# how to use those symbols


file1 = open("data.txt")
file2 = open("parsedFile.txt","w+")

for line in file1:
	text = line.split("\t")[-1]
	pattern = re.compile("[a-zA-Z\s\^'%()\-'<]+")
	text = re.search(pattern, text)
	if text:
		text = text.group(0)
		noUseTags = re.compile("noise|\n|[()\^<]")
		text = re.sub(noUseTags , "", text)

		for s in symbols:
			text = text.replace(s,symbols.get(s))
		file2.write(text+"\n")








	