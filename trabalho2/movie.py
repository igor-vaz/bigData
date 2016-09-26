import matplotlib.pyplot as plt
import numpy as np
import re

data =[]
oneType = 0
twoTypes = 0

#leitura de arquivo
arq = open('movie_metadata.csv','r')
arq = arq.read()
lines = arq.split("\n")

for lines in lines[1:]:
  data.append(lines.split(","))

print(data[0])