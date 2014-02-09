import re

symbols = {"%hes":"err","%spk":"well","%int":"%laugh","noise":""}
addition = {"--":"%quad"}
# how to use those symbols


file1 = open("data.txt")
file2 = open("cesar_data.txt.text","w+")
file3 = open("cesar_data.txt.feat","w+")

for line in file1:
	text = line.split("\t")[-1]
	feat = line.split("\t")[-2]
	pattern = re.compile("[a-zA-Z\s\^'%()\-'<>]+")
	text = re.search(pattern, text)
	if text:
		text = text.group(0)
		noUseTags = re.compile("<//noise>|\n|[()\^\-<>]|noise")
		text = re.sub(noUseTags , "", text)
		format = re.compile("^\s+")
		for s in symbols:
			text = text.replace(s,symbols.get(s))
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








	