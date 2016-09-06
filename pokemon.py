import matplotlib.pyplot as plt
import numpy as np
import re

data =[]
oneType = 0
twoTypes = 0

#leitura de arquivo
arq = open('Pokemon.csv','r')
arq = arq.read()
lines = arq.split("\n")

for lines in lines[1:]:
	data.append(lines.split(","))

del data[len(data)-1]

#cria dicionarios
dict_type = {}
dict_total = {}

#armazena dados
for char in data:
	if char[3] == '':
		key = char[2]
		oneType +=1
	else:
		key=char[2]+"/"+char[3]
		twoTypes +=1

	if key in dict_total.keys():
		dict_total[key] += 1.0
	else:
		dict_total[key] = 1.0

	if key in dict_type.keys():
		dict_type[key] += float(int(char[4]))
	else:
		dict_type[key] = float(int(char[4]))

types = dict_type.keys()
for key in dict_type.keys():
	result = re.match('.*/.*', key)
	if result:
		types.remove(result.group())

mean = {}

for key in dict_type.keys():
	mean[key] = dict_type[key]/dict_total[key]

def printNumType():
	print("Pokemons com um tipo: "+ str(oneType))
	print("Pokemons com dois tipos: "+str(twoTypes))

def printMean():
	print("Media dos pontos totais por tipos: ")
	for key in dict_type.keys():
		print(key+': '+str(mean[key]))

def compareOneTwo(type):
	print("Media do tipo "+type+": "+str(mean[type]))
	has = 0
	bigger = 0
	for key in dict_type.keys():
		result = re.match('.*'+type+'.*', key)
		if result:
			has +=1
			if mean[result.group()] > mean[type]:
				bigger+=1
	print("Numero total de tipos que contem "+type+": "+str(has))
	print("Numero de tipos com media maior que "+type+": "+str(bigger))

	print("Media dos tipos que contem "+type+": ")
	for key in dict_type.keys():
	 	result = re.match('.*'+type+'.*', key)
	  	if result:
	  		print(result.group()+": "+str(mean[result.group()]))
printNumType()

for t in types:
	compareOneTwo(t)