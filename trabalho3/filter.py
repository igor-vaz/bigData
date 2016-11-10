import numpy as np


def column():
	pass

data =[]

#leitura de arquivo
file = open('train_file.csv','r')
file = file.read()
lines = file.split("\n")

for lines in lines[1:]:
	data.append(lines.split(","))



print len(data)